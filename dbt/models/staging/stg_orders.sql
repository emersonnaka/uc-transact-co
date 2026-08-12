select
    cast(order_id as bigint)            as order_id,
    cast(customer_id as bigint)         as customer_id,
    cast(product_id as bigint)          as product_id,
    cast(quantity as integer)           as quantity,
    cast(unit_price as decimal(12, 2))  as unit_price,
    cast(discount as decimal(12, 2))    as discount,
    cast(total_amount as decimal(12, 2)) as total_amount,
    cast(status as varchar)             as order_status,
    cast(channel as varchar)            as channel,
    cast(ordered_at as timestamptz)     as ordered_at,
    cast(updated_at as timestamptz)     as updated_at,
    cast(ingested_at as timestamptz)    as ingested_at

from {{ source('raw', 'orders') }}
