{{ config(materialized='view') }}

-- Daily gross ordered amount, named by its physical basis.
-- Business meaning for this number is owned by Finance, not by this model.
-- The warehouse session timezone is America/Sao_Paulo, so the UTC day has to be
-- stated rather than assumed: 557 orders fall on a different calendar day.
select
    cast(ordered_at at time zone 'UTC' as date)  as ordered_date_utc,
    count(*)                                     as order_count,
    sum(total_amount)                            as gross_ordered_amount
from {{ ref('stg_orders') }}
where order_status <> 'cancelled'
group by 1
