WITH customers_with_a_and_b AS (
    SELECT customer_id
    FROM orders
    WHERE product_name = 'A'

    INTERSECT

    SELECT customer_id
    FROM orders
    WHERE product_name = 'B'
)

SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM customers_with_a_and_b
)
AND customer_id NOT IN (
    SELECT customer_id
    FROM orders
    WHERE product_name = 'C'
)
ORDER BY CUSTOMER_NAME asc