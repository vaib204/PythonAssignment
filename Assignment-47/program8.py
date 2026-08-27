import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def Linear():
  StudyHours = [[1],[2],[3],[4],[5]]
  Marks = [50,55,60,65,70]

  print("Independent Variables are:")
  print(StudyHours)

  print("Dependent Variables:")
  print(Marks)

  ######################################## 
  
  print("Split the dataset")
  X = StudyHours
  Y = Marks

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

  new_data = [[6]]

  Y_pred = model.predict(new_data)

  print("Expected results:")
  print(Y_pred)

  ########################################

  print("Coefficient :")
  print(model.coef_)
  
  print("Intercept:")
  print(model.intercept_)

def main():
  Linear()

if __name__ == "__main__":
  main()