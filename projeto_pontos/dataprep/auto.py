# %%

import pandas as pd
import sqlalchemy
import datetime

engine = sqlalchemy.create_engine("sqlite:///../../data/database_upsell.db")

from tqdm import tqdm

def read_query(path):
    with open(path, 'r') as open_file:
        return open_file.read()
    
def range_date(start, stop):

    dates = []
    dt_start = datetime.datetime.strptime(start, "%Y-%m-%d")
    dt_stop = datetime.datetime.strptime(stop, "%Y-%m-%d")

    while dt_start <= dt_stop:
        dates.append(dt_start.strftime("%Y-%m-%d"))
        dt_start += datetime.timedelta(days=1)

    return dates

# %%    

# Constroi a Feature Store
dates = range_date('2024-03-01', '2024-04-25')
query = read_query("etl_feature_store.sql")

for i in tqdm(dates):
    df = pd.read_sql(query.format(date=i), engine)
    df.to_sql("tb_feature_store", engine, index=False, if_exists='append')

# %%

# Constroi a ABT
query = read_query("etl_abt.sql")
with engine.connect() as con:
    for q in query.split(";"):
        con.execute(sqlalchemy.text(q))
    con.execute(sqlalchemy.text("DROP TABLE IF EXISTS tb_feature_store;"))


df = pd.read_sql_table("tb_abt_churn", engine)
df.to_csv("../../data/abt_pontos.csv", index=False, sep=";")
# %%
