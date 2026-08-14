{{ config(materialized='view') }}

-- Two counted sides placed beside each other. D3 (whether refunds reduce a
-- total, and in which period) is unresolved and owned by Finance, so nothing
-- here is netted against anything.

with returned_orders as (

    select
        count(*)           as returned_order_count,
        sum(total_amount)  as returned_order_amount
    from {{ ref('stg_orders') }}
    where order_status = 'returned'

),

refunded_payments as (

    select
        count(*)      as refunded_payment_count,
        sum(amount)   as refunded_payment_amount
    from {{ source('raw', 'payments') }}
    where status = 'refunded'

)

select
    returned_orders.returned_order_count,
    returned_orders.returned_order_amount,
    refunded_payments.refunded_payment_count,
    refunded_payments.refunded_payment_amount
from returned_orders
cross join refunded_payments
