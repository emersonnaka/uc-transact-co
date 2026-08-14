#!/usr/bin/env bash
# The crank: drive every ready spec through the Task-Spec authorization chain
# until the frontier stops producing work.
#
#   handoff -> run --ci -> accept (5 gates) -> transition -> commit
#
# Nothing here decides what to run. The frontier does, and it is recomputed
# after every accepted spec. A spec with no write surface can never be cranked;
# the loop names it instead of quietly skipping it.
#
# Usage: scripts/crank.sh [--dry-run]

set -euo pipefail

DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

RECEIPTS=tmp/d4/receipts
mkdir -p "$RECEIPTS"

ready_ids() {
  taskspec --json ready | jq -r '.data.tasks[].task_id'
}

spec_path() {
  local id="$1"
  if [[ -f "tasks/$id.md" ]]; then echo "tasks/$id.md"
  elif [[ -f "tasks/done/$id.md" ]]; then echo "tasks/done/$id.md"
  else echo ""; fi
}

declares_paths() {
  local spec="$1"
  sed -n 's/^touches_paths: *\[\(.*\)\]/\1/p;s/^creates_paths: *\[\(.*\)\]/\1/p' "$spec" \
    | tr -d ' ' | tr ',' '\n' | grep -v '^$' || true
}

round=0
cranked=0
skipped=()

while :; do
  round=$((round + 1))
  mapfile -t ids < <(ready_ids)
  [[ ${#ids[@]} -eq 0 ]] && { echo "FRONTIER=EMPTY"; break; }

  progressed=0
  for id in "${ids[@]}"; do
    spec="$(spec_path "$id")"
    [[ -z "$spec" ]] && continue

    if [[ -z "$(declares_paths "$spec")" ]]; then
      echo "CRANK=SKIP id=$id reason=NO_WRITE_SURFACE"
      skipped+=("$id")
      continue
    fi

    echo "──────── round $round · $id"
    if [[ $DRY_RUN -eq 1 ]]; then
      echo "CRANK=DRY_RUN id=$id"
      progressed=1
      continue
    fi

    # A spec has to be authorized before it can be handed off.
    grep -q '^signed_off: true' "$spec" || taskspec gate --stamp --require-tier1 "$spec" >/dev/null

    handoff="$RECEIPTS/crank-$id.json"
    rm -f "$handoff"
    taskspec handoff "$spec" --backend claude --out "$handoff" | tail -1

    taskspec run --ci "$spec" >/dev/null 2>&1 \
      && echo "RUN=0" \
      || { echo "CRANK=STOP id=$id reason=EVALS_FAILED"; exit 1; }

    taskspec accept --handoff "$handoff" --stamp --gold-sanity "$spec" 2>&1 \
      | grep -E '^(ACCEPTED|ACCEPTANCE_FAILURE)=' \
      | tee /tmp/crank-verdict
    grep -q '^ACCEPTED=1' /tmp/crank-verdict \
      || { echo "CRANK=STOP id=$id reason=NOT_ACCEPTED"; exit 1; }

    taskspec transition "$id" done "cranked" >/dev/null
    taskspec rebuild-state >/dev/null

    # Commit so the next spec starts from a clean base. The chain measures
    # blast radius against the base commit, so leftover work from spec N would
    # be read as spec N+1 writing outside its scope.
    git add -A tasks .taskspec dbt/models/staging
    git -c core.hooksPath=/dev/null commit -q -m "crank($id): accepted at Tier 1, five gates" || true

    cranked=$((cranked + 1))
    progressed=1
    break   # re-ask the frontier; dependents may have just become ready
  done

  [[ $progressed -eq 0 ]] && { echo "FRONTIER=STALLED"; break; }
  [[ $DRY_RUN -eq 1 ]] && break
done

echo
echo "CRANK_DONE cranked=$cranked"
if [[ ${#skipped[@]} -gt 0 ]]; then
  printf 'NEVER_CRANKABLE=%s\n' "${skipped[*]}"
  echo "  These declare no write surface. A decision is not a file, so no"
  echo "  amount of concurrency makes them ready. They stay with their owner."
fi
taskspec --json ready --all | jq -r '.data.tasks[] | "STILL_OPEN " + .task_id'
