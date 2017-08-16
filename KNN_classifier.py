from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class KNN():
    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions
    def closest(self, row):
        best_d = euc(row, self.X_train[0])
        best_i = 0
        for i in range(1, len(self.X_train)):
            e = euc(row, self.X_train[i])
            if e < best_d:
                best_d = e
                best_i = i
        return self.Y_train[best_i]
    
import sys
import numpy as np
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
Y = iris.target

from sklearn.cross_validation import train_test_split
X_train , X_test , Y_train, Y_test = train_test_split(X, Y, test_size=0.5)

c = KNN()
c.fit(X_train, Y_train)

predict = c.predict(X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(Y_test, predict)

