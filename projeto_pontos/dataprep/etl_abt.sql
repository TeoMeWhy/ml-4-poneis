DROP TABLE IF EXISTS tb_abt_churn;
CREATE TABLE IF NOT EXISTS tb_abt_churn AS
WITH tb_eventos AS (

    SELECT DISTINCT
        idCustomer,
        dtTransaction

    FROM tb_transactions_safe

),

tb_fs AS (
    
    SELECT idCustomer,
           dtRef

    FROM tb_feature_store
),

tb_flag_active AS (

    SELECT t1.idCustomer,
        t1.dtRef,
        count(distinct t2.idCustomer) AS flActive

    FROM tb_fs AS t1

    LEFT JOIN tb_eventos AS t2
    ON t1.idCustomer = t2.idCustomer
    AND t1.dtRef < t2.dtTransaction
    AND t1.dtRef > date(t2.dtTransaction, '-15 day')

    GROUP BY 1,2
    ORDER BY 2,1

),

tb_rn AS (

    select *,
            row_number() OVER (PARTITION BY idCustomer ORDER BY RANDOM()) AS rn

    from tb_flag_active
    order by 1,2

)

SELECT t1.*,
       t2.flActive

FROM  tb_feature_store AS t1

LEFT JOIN tb_rn AS t2
ON t1.idCustomer = t2.idCustomer
AND t1.dtRef = t2.dtRef

WHERE rn <= 2
ORDER BY 2,1