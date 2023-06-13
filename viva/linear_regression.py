import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

x = np.array([5, 15 ,22, 25, 35,42, 45, 55, 60, 67]).reshape((-1, 1))
y = np.array([5,12,17, 20, 14, 32, 22, 38, 40,43])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

model = LinearRegression().fit(x, y)

y_pred=model.predict(x_test)
print('predicted response:', y_pred)

print('intercept:\n', model.intercept_)
print("Coefficients: \n", model.coef_)
print("R^2 score:",r2_score(y_test, y_pred))

plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, y_pred, color="blue")

plt.show()





