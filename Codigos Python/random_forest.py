# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:49:48 2020

@authors: Rafael, Lucas
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# Importar os dados da base
print("Random Forest")
xcsvfile = "X_2015_numbers.csv"
ycsvfile = "y_2015_numbers.csv"
datasetx = pd.read_csv(xcsvfile,header = None)
datasety = pd.read_csv(ycsvfile,header = None)
print(datasetx.shape)
print(datasety.shape)
X = datasetx
y = datasety

"""
Testes usando Holdout
"""

# Separacao da base em treinamento (70% da base) e teste (30% da base)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3, random_state=42, stratify=y)

# Criacao do classificador
clfa = RandomForestClassifier(n_estimators = 400, max_depth = 39, min_samples_split = 2, min_samples_leaf = 2, max_features = 'auto', random_state=0)

# Treinamento do classificador
clfa = clfa.fit(X_train, y_train.values.ravel())

# Resultados dos testes
predicted=clfa.predict(X_test)

# Porcentagem de acuracia 
score=clfa.score(X_test, y_test)

# Criacao da matriz de confusao
matrix = confusion_matrix(y_test, predicted)
print("Accuracia = %.4f " % score)
print("Matriz de confusao:")
print(matrix)

"""
Testes usando Validacao Cruzada com 10 folds
"""

# Criacao do classificador
clfb = RandomForestClassifier(n_estimators = 400, max_depth = 39, min_samples_split = 2, min_samples_leaf = 2, max_features = 'auto', random_state=0)

# Treinamento do classificador
folds=10
result = cross_val_score(clfb, X, y.values.ravel(), cv=folds)

# Resultados numericos
print("\nResultado da validacao cruzada com %d folds:" % folds)
print("Acuracia media: %.4f" % result.mean())
print("Desvio Padrao: %.4f" % result.std())

# Matriz de confusao
Z = cross_val_predict(clfb, X, y.values.ravel(), cv=folds)
cm=confusion_matrix(y, Z)
print("Matriz de confusao:")
print(cm)

