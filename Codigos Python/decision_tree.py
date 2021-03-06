# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:49:48 2020

@authors: Rafael, Lucas
"""

import pandas as pd
from sklearn import tree
from sklearn.model_selection import  cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


# Importar os dados da base
print("Decision Tree")
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
clfa = tree.DecisionTreeClassifier(criterion='gini',splitter='best', max_depth=9, min_samples_leaf=30, min_samples_split=2)

# Treinamento do classificador
clfa = clfa.fit(X_train, y_train)

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
clfb = tree.DecisionTreeClassifier(max_depth=10, min_samples_leaf=1, min_samples_split=30)

# Treinamento do classificador
folds=10
result = cross_val_score(clfb, X, y, cv=folds)

# Resultados numericos
print("\nResultado da validacao cruzada com %d folds:" % folds)
print("Acuracia media: %.4f" % result.mean())
print("Desvio Padrao: %.4f" % result.std())

# Matriz de confusao
Z = cross_val_predict(clfb, X, y, cv=folds)
cm=confusion_matrix(y, Z)
print("Matriz de confusao:")
print(cm)




