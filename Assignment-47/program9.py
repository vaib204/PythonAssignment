import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def Linear():
  X = [[1,7],[2,6],[3,7],[4,6],[5,8]]
  
  Y = [50,55,60,65,70]

  print("Independent Variables are:")
  print(X)

  print("Dependent Variables:")
  print(Y)

  ######################################## 
  
  print("Split the dataset")
  X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
  )

  ######################################
  print("Train the model")

  model = LinearRegression()

  model = model.fit(X_train,Y_train)

  Y_pred = model.predict(X_test)

  print("Expected results:")
  print(Y_pred)

  print("Actual results:")
  print(Y_test)

  ########################################

  print("Coefficient :")
  print(model.coef_)
  
  print("Intercept:")
  print(model.intercept_)

def main():
  Linear()

if __name__ == "__main__":
  main()