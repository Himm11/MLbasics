import matplotlib.pyplot as plt
import numpy as np

def estimate_coef(x,y):
    n=np.size(x)

    mean0fx=np.mean(x)
    meanOfy=np.mean(y)

    SS_xy=np.sum(x*y) - n*meanOfy*mean0fx
    SS_xx=np.sum(x*x) - n*mean0fx*mean0fx

    #sum of cross section about x
    b[1]= SS_xy / SS_xx
    b[0]= meanOfy - b[1] *mean0fx

    return (b[0],b[1])

def RegressionLine(x,y,b):
    #predicted response vector
    prv = b[0] + b[1]*x
    #regression line
    plt.scatter(x,y,prv)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,0,12])
import matplotlib.pyplot as plt
import numpy as np

def estimate_coef(x,y):
    n=np.size(x)

    mean0fx=np.mean(x)
    meanOfy=np.mean(y)

    SS_xy=np.sum(x*y) - n*meanOfy*mean0fx
    SS_xx=np.sum(x*x) - n*mean0fx*mean0fx

    #sum of cross section about x
    b[1]= SS_xy / SS_xx
    b[0]= meanOfy - b[1] *mean0fx

    return (b[0],b[1])

def RegressionLine(x,y,b):
    #predicted response vector
    prv = b[0] + b[1]*x
    #regression line
    plt.scatter(x,y,prv)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,0,12])
b=np.arange(2)
b=estimate_coef(x,y)
RegressionLine(x,y,b)
b=estimate_coef(x,y)
RegressionLine(x,y,b)
