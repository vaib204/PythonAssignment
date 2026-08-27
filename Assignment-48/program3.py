import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

#############################
print("create the dataset:")

X = [[1],[2],[3],[4],[5]]
Y = [20000,25000,30000,35000,40000]

X_train,X_test,Y_train,Y_test = train_test_split(
  X,
  Y,
  test_size= 0.2,
  random_state=42
)

############################
print("Select the model")

model = LinearRegression()

model = model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("Predicted data:")
print(Y_pred)

print("Actual data:")
print(Y_test)

New_data = [[6]]

Y_pred_new = model.predict(New_data)
print("Predicted data:")
print(Y_pred_new)
plt.plot(
      X,
      Y,
      marker= "o",
      linestyle= "--",
      linewidth= 2,
      markersize= 7,
      label= "salary"
  )

plt.title("Marvellous Tree")
plt.ylabel("Salary")
plt.xlabel("Experience")
plt.grid(True)
plt.show()