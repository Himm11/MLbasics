mport sklearn
from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
x,y=datasets.load_iris(return_X_y=True)

x=x[:,:2]

train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.1,random_state=42)
isolated_tree_classifier=ensemble.IsolationForest()

isolated_tree_classifier.fit(train_x,train_y)

scatter=plt.scatter(x[:,0], x[:,1], c=y, s=20,edgecolor="k")
handles,labels= scatter.legend_elements()
plt.axis("square")
plt.legend(handle=handles, label= ["outliers","inliers"], title="true class")

