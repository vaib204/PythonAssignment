import numpy as np

X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)

print("Calculate the Mean:")

X_mean = sum(X)/len(X)
print(X_mean)

Y_mean = sum(Y)/len(Y)
print(Y_mean)

print("Slope of m")
Num = 0
den = 0

for i in range(n):
  Num +=(X[i] - X_mean)*(Y[i] - Y_mean)
  den +=(X[i] - X_mean)**2

m = Num/den
print(m)

print("Intercept:")

#b = Y - mx

b = Y_mean - m * X_mean

print(b)

print("Regression equation")

#Y = mx + c

print("Regression  euqation Y = ",m,"X +",b)

x = 6
Y_pred = m * x + b

print(f"Predicted Y for X = ",Y_pred)
