# %%

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/dados_cerveja_nota.xlsx")
df
# %%
# Criando gráfico de cervejas

plt.plot(df["cerveja"], df["nota"], 'o')
plt.grid(True)
plt.title("Relação Nota vs Cerveja")
plt.ylim(0, 11)
plt.xlim(0, 11)
plt.xlabel("Cerveja")
plt.ylabel("Nota")
plt.show()

# %%

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(df[["cerveja"]], df["nota"])

# %%
a, b = reg.intercept_, reg.coef_[0]
print(f"a={a}; b={b}")

# %%
X = df[["cerveja"]].drop_duplicates()
y_estimado = reg.predict(X)
y_estimado

plt.plot(df["cerveja"], df["nota"], 'o')
plt.plot(X, y_estimado, '-')
plt.grid(True)
plt.title("Relação Nota vs Cerveja")
plt.ylim(0, 11)
plt.xlim(0, 11)
plt.xlabel("Cerveja")
plt.ylabel("Nota")
plt.show()

# %%

from sklearn import tree
arvore = tree.DecisionTreeRegressor(max_depth=2)
arvore.fit(df[["cerveja"]], df["nota"])

y_estimado_arvore = arvore.predict(X)

plt.figure(dpi=500)
plt.plot(df["cerveja"], df["nota"], 'o')
plt.plot(X, y_estimado, '-')
plt.plot(X, y_estimado_arvore, '-')
plt.grid(True)
plt.title("Relação Nota vs Cerveja")
plt.ylim(0, 11)
plt.xlim(0, 11)
plt.xlabel("Cerveja")
plt.ylabel("Nota")
plt.legend(["Observações", "Regressão Linear", "Árvore de Decisão"])
plt.show()
# %%
