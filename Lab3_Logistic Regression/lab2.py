#Logistic Regression

from sklearn.linear_model import LogisticRegression
import pandas as pd

df=pd.read_csv('User_Data.csv')
X = df[['Age']]
y = df['Purchased']
clf = LogisticRegression(random_state=0).fit(X,y)
print(clf.predict([[19]]))
print(clf.predict_proba([[19]]))

score=clf.score(X, y)
print(score)