# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:40:55 2020

@author: Rafael
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:38:17 2020

@author: Rafael
"""

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

xcsvfile = "Test_2015_X.csv"
ycsvfile = "Test_2015_Y.csv"
datasetx = pd.read_csv(xcsvfile,header = None)
datasety = pd.read_csv(ycsvfile,header = None)

print(datasetx.shape)
print(datasety.shape)
colm1 = ColumnTransformer([('encoder', OneHotEncoder(), [0,1,4,5,6,7,8,9,10,11,12])], remainder='passthrough',sparse_threshold=0)
colm2 = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough',sparse_threshold=0)
X = np.array(colm1.fit_transform(datasetx), dtype = np.str)
y=datasety


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3, random_state=42, stratify=y)


clfa = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

clfa = clfa.fit(X_train, y_train)

predicted=clfa.predict(X_test)

score=clfa.score(X_test, y_test)

matrix = confusion_matrix(y_test, predicted)

print("Accuracy = %.2f " % score)
print("Confusion Matrix:")
print(matrix)

clfb = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
folds=10
result = cross_val_score(clfb, X, y, cv=folds)
print("\nCross Validation Results %d folds:" % folds)
print("Mean Accuracy: %.2f" % result.mean())
print("Mean Std: %.2f" % result.std())

Z = cross_val_predict(clfb, X, y, cv=folds)
cm=confusion_matrix(y, Z)
print("Confusion Matrix:")
print(cm)

