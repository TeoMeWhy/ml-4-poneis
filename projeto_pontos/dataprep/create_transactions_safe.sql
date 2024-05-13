DROP TABLE IF EXISTS tb_transactions_safe;
CREATE TABLE IF NOT EXISTS tb_transactions_safe AS
WITH customer AS (
    SELECT
        uuid AS idCustomer,
        Name
    FROM tb_customers
    WHERE Name <> 'teomewhy'
),

transactions AS (

    SELECT t1.*,
        t2.UUID As idTransaction,
        date(substr(t2.dtTransaction,0,11)) AS dtTransaction,
        t2.Points,
        t3.UUID AS idCart,
        t3.Product,
        t3.Quantity

    FROM customer AS t1

    INNER JOIN tb_transactions AS t2
    ON t1.idCustomer = t2.idCustomer

    INNER JOIN tb_transactions_cart AS t3
    ON t2.UUID = t3.idTransaction

)

select * from transactions
;
