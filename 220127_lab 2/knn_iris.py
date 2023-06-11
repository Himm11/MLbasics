# Using iris data set

import pandas as pd

df = pd.read_csv('iris.data')

x_train = df[['sepal length']]
y_train = df['class']

from sklearn.neighbors import KNeighborsClassifier

neigh2 = KNeighborsClassifier(n_neighbors=2)
neigh2.fit(x_train, y_train)

print(neigh2.predict([[4.9]]))

print(neigh2.predict_proba([[4.9]]))
