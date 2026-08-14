{{ config(materialized='view') }}

-- Capture-clock measurement: captured payment amounts by the UTC calendar day
-- of paid_at. D2 (which event recognizes income) is unresolved and owned by
-- Finance, so this model does not claim capture is that event.
--
-- The warehouse session timezone is America/Sao_Paulo, so the UTC day is stated
-- explicitly: 1,186 payments fall on a different calendar day otherwise.
-- Refunded payments are reported by stg_returns_refunds, never subtracted here.
select
    cast(paid_at at time zone 'UTC' as date)  as captured_date_utc,
    count(*)                                  as captured_payment_count,
    sum(amount)                               as captured_payment_amount
from {{ source('raw', 'payments') }}
where status = 'captured'
group by 1
