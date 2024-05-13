# %%
import pandas as pd

df = pd.read_excel("../data/dados_cerveja.xlsx")
df

# %%
## Como podemos fazer a máquina aprender?

features = ["temperatura","copo","espuma","cor"]
target = "classe"

X = df[features]
y = df[target]

# %%

X = X.replace({
    "mud":1, "pint":0,
    "sim":1, "não":0,
    "escura":1, "clara":0,    
})

X

# %%
from sklearn import tree

arvore = tree.DecisionTreeClassifier(random_state=42)
arvore.fit(X, y)

# %%

import matplotlib.pyplot as plt

plt.figure(dpi=600)

tree.plot_tree(arvore,
               class_names=arvore.classes_,
               feature_names=features,
               filled=True)

# %%
# "temperatura","copo","espuma","cor"

probas = arvore.predict_proba([[-5, 1, 0, 1]])[0]

pd.Series(probas, index=arvore.classes_)
# %%
