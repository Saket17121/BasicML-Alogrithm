import numpy as np
from sklearn.model_selection import train_test_split

X=Y=[]
data = np.genfromtxt("linearRegression.csv", delimiter=",")
for i in range(len(data)):
    X.append(data[i][0])
    Y.append(data[i][1])

x_train, y_train, x_test, y_test = train_test_split(X,Y, random_state=30)

print(type(x_train), x_train[0])
m=0.5
c=0.1
alpha = 0.0005
n= 1000
for i in range(n):
    slope=0
    intercept = 0
    random_index = np.random.randint(len(X))
    intercept = intercept + ((m*x_train[random_index:random_index+1]+c) - y_train[random_index:random_index+1])
    slope=slope+((m*x_train[random_index:random_index+1]+c)-y_train[random_index:random_index+1])*x_train[random_index:random_index+1]
    c = c - alpha*(intercept / len(X))
    m = m - alpha*(slope / len(X))


print(f"Slope : {m}")
print(f"Intercept : {c}")

y_pred = np.dot(m[0] * x_test) + c[0]

print(f"Predicted value : {y_pred}")