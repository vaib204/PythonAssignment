import numpy as np

X = [1,2,3,4,5]
Y = [3,4,2,4,5]

mean_Y = np.mean(Y)

n = len(X)
j  = len(Y)

m = 0.4
b = 2.4

#Y = mx + c

print("Regression  euqation Y = ",m,"X +",b)

x = 6
Y_pred = m * x + b

print(f"Predicted Y for X = ",Y_pred)

#yp = mx + b
print(" YC Values : ")
result = []
for i in X:
  yp = m*i + b
  result.append(yp)
print(result)  

mscnum = []
print(" Residual error:")  
for i in range(j):
  y_yp = Y[i] - result[i]
  mscnum.append(y_yp)
print(mscnum)


#msc = sumy_yp2 / n

print("MSC:")
Num = 0
for i in mscnum:
  Num += (i**2)

print("MSC is : " \
"")
print(Num/5)

#R2 = 1 - (sum(y - yp)2 / sum(y - ymean)2)

print("R2 score:")

yminusyp = 0
for i in range(n):
 yminusyp +=(Y[i] - result[i])**2
print(f"Sum((Y-Yp)**2) : ",yminusyp)

yminusbar = 0
for i in range(n):
  yminusbar += (Y[i] - mean_Y)**2
print(f"sum((Y-Y_mean)**2)",yminusbar)

r2 = 1 - (yminusyp / yminusbar)

print("R2 : ",r2)
