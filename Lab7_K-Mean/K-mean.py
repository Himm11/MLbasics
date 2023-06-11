import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('iris.data')
data.head()
data.isnull()
z=['sepal length','sepal width','petal length','petal width']
for i in z:
    data[i]=data[i].replace(0,np.NaN)
    mean=int(data[i].mean(skipna=True))
    data[i]=data[i].replace(np.NaN,mean)

x=data.iloc[:,0:4]
y=data.iloc[:,[4]]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
alg=KNeighborsClassifier(n_neighbors=27,p=2,metric='euclidean')
alg.fit(x_train,y_train)
y_pred=alg.predict(x_test)
print(y_pred)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print(ac)

