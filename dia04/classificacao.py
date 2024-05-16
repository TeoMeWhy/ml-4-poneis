# %%

import pandas as pd

df = pd.read_excel("../data/dados_cerveja_nota.xlsx")
df

# %%

df['Aprovado'] = df["nota"] >= 5

features = ['cerveja']
target = 'Aprovado'
# %%
from sklearn import linear_model
reg = linear_model.LogisticRegression(penalty=None,
                                      fit_intercept=True)

# aqui o modelo aprende
reg.fit(df[features], df[target])

# aqui o modelo prevê
reg_predict = reg.predict(df[features])
reg_predict

# %%

from sklearn import metrics

reg_acc = metrics.accuracy_score(df[target], reg_predict)
print("Acurácia Reg Log.:", reg_acc)

reg_precision = metrics.precision_score(df[target], reg_predict)
print("Precisão Reg Log.:", reg_precision)

reg_recall = metrics.recall_score(df[target], reg_predict)
print("Recall Reg Log.:", reg_recall)

reg_conf = metrics.confusion_matrix(df[target], reg_predict)
reg_conf = pd.DataFrame(reg_conf,
                        index=['False', 'True'],
                        columns=['False', 'True'],)

print(reg_conf)

# %%
from sklearn import tree
arvore = tree.DecisionTreeClassifier(max_depth=3)

# aqui o modelo aprende
arvore.fit(df[features], df[target])

# aqui o modelo prevê
arvore_predict = arvore.predict(df[features])
arvore_predict

arvore_acc = metrics.accuracy_score(df[target], arvore_predict)
print("Acurácia Árvore:", arvore_acc)

arvore_precision = metrics.precision_score(df[target], arvore_predict)
print("Precisão Árvore:", arvore_precision)

arvore_recall = metrics.recall_score(df[target], arvore_predict)
print("Recall Árvore:", arvore_recall)

arvore_conf = metrics.confusion_matrix(df[target], arvore_predict)
arvore_conf
# %%

from sklearn import naive_bayes
nb = naive_bayes.GaussianNB()

# aqui o modelo aprende
nb.fit(df[features], df[target])

# aqui o modelo prevê
nb_predict = nb.predict(df[features])
nb_predict

nb_acc = metrics.accuracy_score(df[target], nb_predict)
print("Acurácia Naive Bayes:", nb_acc)

nb_precision = metrics.precision_score(df[target], nb_predict)
print("Precisão Naive Bayes:", nb_precision)

nb_recall = metrics.recall_score(df[target], nb_predict)
print("Recall NB:", nb_recall)

nb_conf = metrics.confusion_matrix(df[target], nb_predict)
nb_conf

# %%
nb_proba = nb.predict_proba(df[features])[:,1]
nb_predict = nb_proba > 0.2

nb_acc = metrics.accuracy_score(df[target], nb_predict)
print("Acurácia Naive Bayes:", nb_acc)

nb_precision = metrics.precision_score(df[target], nb_predict)
print("Precisão Naive Bayes:", nb_precision)

nb_recall = metrics.recall_score(df[target], nb_predict)
print("Recall NB:", nb_recall)

# %%
import matplotlib.pyplot as plt

roc_curve = metrics.roc_curve(df[target], nb_proba)
plt.plot(roc_curve[0], roc_curve[1] )
plt.grid(True)
plt.plot([0,1], [0,1], '--')
plt.show()

# %%

roc_auc = metrics.roc_auc_score(df[target], nb_proba)
roc_auc