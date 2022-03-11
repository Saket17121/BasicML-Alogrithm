import numpy as np

X=Y=[]
data = np.genfromtxt("linearRegression.csv", delimiter=",")
for i in range(len(data)):
    X.append(data[i][0])
    Y.append(data[i][1])

xtest=int(input("Enter the value for predict : "))
m=0.5
c=0.1
alpha = 0.0005
n= 1000
for i in range(n):
    slope=0
    intercept = 0
    random_index = np.random.randint(200)
    intercept = intercept + ( (m*X[random_index]+c) - Y[random_index])
    slope = slope+( (m * X[random_index]+c)-Y[random_index]) * X[random_index]
    c = c - alpha*(intercept / len(X))
    m = m - alpha*(slope / len(X))


print(f"Slope : {m}")
print(f"Intercept : {c}")

y_pred = m*xtest + c

print(f"Predicted value : {y_pred}")