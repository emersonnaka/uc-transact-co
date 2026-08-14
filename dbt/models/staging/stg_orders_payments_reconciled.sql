{{ config(materialized='view') }}

-- Physical reconciliation, one row per order. At most one payment exists per
-- order_id, so the join does not fan out. Orders with no payment row keep null
-- payment columns and has_payment says so explicitly, because a zero would read
-- as a measured amount rather than an absent one.
select
    orders.order_id,
    orders.order_status,
    orders.total_amount,
    orders.ordered_at,
    payments.payment_id,
    payments.amount                   as payment_amount,
    payments.method                   as payment_method,
    payments.status                   as payment_status,
    payments.paid_at,
    payments.payment_id is not null   as has_payment
from {{ ref('stg_orders') }} as orders
left join {{ source('raw', 'payments') }} as payments
    on orders.order_id = payments.order_id
