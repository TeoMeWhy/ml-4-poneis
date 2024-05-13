WITH transactions AS (

    SELECT *

    FROM tb_transactions_safe

    WHERE dtTransaction < '{date}'
    AND dtTransaction > date('{date}', '-30 day')

    ORDER BY dtTransaction

),

summary_general AS (

    SELECT 
        idCustomer,
        Name,

        MIN(julianday('{date}') - julianday(dtTransaction)) AS qtdeRecencia,
        COUNT(DISTINCT dtTransaction) AS freqDias,
        COUNT(DISTINCT idTransaction) AS freqTransacoes,
        COUNT( DISTINCT CASE WHEN Product = 'Lista de presença' THEN idTransaction END) qtdListaPresença,
        COUNT( DISTINCT CASE WHEN Product = 'ChatMessage' THEN idTransaction END) qtdChatMessage,
        COUNT( DISTINCT CASE WHEN Product = 'Troca de Pontos StreamElements' THEN idTransaction END) qtdTrocaPontos,
        COUNT( DISTINCT CASE WHEN Product = 'Resgatar Ponei' THEN idTransaction END) qtdResgatarPonei,
        COUNT( DISTINCT CASE WHEN Product = 'Presença Streak' THEN idTransaction END) qtdPresençaStreak,

        1.0 * COUNT( DISTINCT CASE WHEN Product = 'Lista de presença' THEN idTransaction END) / COUNT(DISTINCT idTransaction) AS pctListaPresença,
        1.0 * COUNT( DISTINCT CASE WHEN Product = 'ChatMessage' THEN idTransaction END) / COUNT(DISTINCT idTransaction) AS pctChatMessage,
        1.0 * COUNT( DISTINCT CASE WHEN Product = 'Troca de Pontos StreamElements' THEN idTransaction END) / COUNT(DISTINCT idTransaction) AS pctTrocaPontos,
        1.0 * COUNT( DISTINCT CASE WHEN Product = 'Resgatar Ponei' THEN idTransaction END) / COUNT(DISTINCT idTransaction) AS pctResgatarPonei,
        1.0 * COUNT( DISTINCT CASE WHEN Product = 'Presença Streak' THEN idTransaction END) / COUNT(DISTINCT idTransaction) AS pctPresençaStreak,

        SUM(CASE WHEN Points > 0 THEN Points ELSE 0 END) AS qtdePontosGanhos,
        SUM(CASE WHEN Points < 0 THEN Points ELSE 0 END) AS qtdePontosGastos,
        SUM(Points) AS qtdePontosSaldo

    FROM transactions AS t1

    GROUP BY 1,2
),

tb_daily AS (
    SELECT DISTINCT
        idCustomer,
        dtTransaction
    FROM transactions
),

tb_lag AS (
    SELECT *,
            LAG(dtTransaction) OVER (PARTITION BY idCustomer ORDER BY dtTransaction) AS lagDtTransaction
    FROM tb_daily
),

tb_avg_recorrencia AS (
    SELECT idCustomer,
        avg(julianday(dtTransaction)-julianday(lagDtTransaction)) AS avgRecorrencia

    FROM tb_lag
    WHERE lagDtTransaction IS NOT NULL
    GROUP BY 1
)

SELECT 
       '{date}' AS dtRef,
       t1.*,
       t2.avgRecorrencia

FROM summary_general AS t1

LEFT JOIN tb_avg_recorrencia AS t2
ON t1.idCustomer = t2.idCustomer

