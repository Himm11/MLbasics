import pandas as pd
import numpy as np

df=pd.read_csv('breast-cancer-wisconsin.data')

x=np.array(df[['Clump']])
y=np.array(df['Class'])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)

from sklearn import svm

clf = svm.SVC(kernel='linear')

clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

print(y_pred)

