# %%
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection
from sklearn import pipeline

from feature_engine import imputation

import pandas as pd

import scikitplot as skplot

# %%

df = pd.read_csv("../../data/dados_pontos.csv", sep=";")
df

# %%

# %%
features = df.columns.tolist()[3:-1] # Isso é uma lista
target = 'flActive'                  # Isso é uma string (texto)

X = df[features] # Isso é um DataFrame (linha, coluna)
y = df[target]   # Isso é uma Série (linha)

# %%

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                    train_size=0.8,
                                                                    random_state=42,
                                                                    stratify=y)

print("Acurácia Train:", y_train.mean())
print("Acurácia Test:", y_test.mean())

# %%
X_train.isna().sum()

# %%
imput_recorrencia = imputation.ArbitraryNumberImputer(variables=['avgRecorrencia'],
                                                      arbitrary_number=X_train['avgRecorrencia'].max())

imput_0_vars = list(set(features) - set(imput_recorrencia.variables))
imput_0 = imputation.ArbitraryNumberImputer(variables=imput_0_vars,
                                            arbitrary_number=0)

clf = ensemble.RandomForestClassifier(random_state=42)

params = {
    "max_depth":[3,5,10,10,15,20],
    "n_estimators":[50,100,200,500,1000],
    "min_samples_leaf":[10,20,50,100],
}

grid = model_selection.GridSearchCV(clf,
                                    param_grid=params,
                                    scoring='roc_auc',
                                    n_jobs=-1,
                                    verbose=3,
                                    cv=3)

model = pipeline.Pipeline([
    ('imput 0',imput_0),
    ('imput recorrencia',imput_recorrencia),
    ('model', grid)]
)

model.fit(X_train, y_train)

# %%

y_test_pred = model.predict(X_test)
y_test_proba = model.predict_proba(X_test)

# %%
auc = metrics.roc_auc_score(y_test, y_test_proba[:,1])
print("AUC:", auc)

auc_curve = metrics.roc_curve(y_test, y_test_proba[:,1])

plt.plot(auc_curve[0], auc_curve[1])
plt.grid(True)
plt.title("Curva Roc")
plt.legend([f"AUC: {auc:.4f}"])
plt.show()

# %%
skplot.metrics.plot_ks_statistic(y_test, y_test_proba)

# %%
skplot.metrics.plot_lift_curve(y_test, y_test_proba)

# %%
skplot.metrics.plot_cumulative_gain(y_test, y_test_proba)

# %%

model_s = pd.Series({
    "model": model,
    "features": features,
    "auc_test": auc
     })

model_s.to_pickle("modelo_rf.pkl")