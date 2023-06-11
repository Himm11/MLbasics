import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.read_csv('iris.data')

x = df[['sepal length']]
y= df['class']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.7)
from sklearn.neighbors import KNeighborsClassifier

neigh2 = KNeighborsClassifier(n_neighbors=20,p=2)
neigh2.fit(x_train, y_train)
y_pred=neigh2.predict(x_test)
print(y_pred)
ac=accuracy_score(y_test,y_pred)
print('accuracy:',ac)