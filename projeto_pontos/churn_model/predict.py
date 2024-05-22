# %%

import pandas as pd
import sqlalchemy

model = pd.read_pickle("modelo_rf.pkl")
model
# %%

dt = '2024-05-08'
with open("etl_model.sql", 'r') as open_file:
    query = open_file.read()

query = query.format(date=dt)

engine = sqlalchemy.create_engine("sqlite:///../../data/database_upsell.db")
# %%

df = pd.read_sql_query(query, engine)
df
# %%

proba = model['model'].predict_proba(df[model['features']])[:,1]
proba


df['proba_active'] = proba
(df[['Name', 'proba_active']].sort_values(by='proba_active', ascending=False)
                             .head(25)
 )