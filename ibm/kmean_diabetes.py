import pandas as pd
import numpy as np
data=pd.read_csv('diabetes.csv')
data.head()
data.isnull()
z=['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for i in z:
    data[i]=data[i].replace(0,np.NaN)
    mean=int(data[i].mean(skipna=True))
    data[i]=data[i].replace(np.NaN,mean)
print(data.shape)
print(data.head())
x=data.iloc[:,0:8]
print(x)
y=data.iloc[:,[8]]
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.neighbors import KNeighborsClassifier
alg=KNeighborsClassifier(n_neighbors=27,p=2,metric='euclidean')
alg.fit(x_train,y_train)
y_pred=alg.predict(x_test)
print(y_pred)
from sklearn.metrics import confusion_matrix
cf=confusion_matrix(y_test,y_pred)
print(cf)
from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print(ac)