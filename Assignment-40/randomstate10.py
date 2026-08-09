import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
  border = "-"*60

  print(border)
  print("Step 1: Load the dataset")
  print(border)

  datapath = "student_performance_ml.csv"

  df = pd.read_csv(datapath)

  print(df.head())

##########################################################################

  print(border)
  print("Step 2: Decide dependent and independent variable")
  print(border)

  feature_col = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
  ]

  X = df[feature_col]
  Y = df["FinalResult"]

  print("X shape :",X.shape)
  print("Y shape :",Y.shape)
######################################################
  print(border)
  print("Step 3:Split the dataset for train and test")
  print(border)  

  X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=10)

  print("Dataset split activity done")
  print("X shape",X.shape)  #30,5
  print("Y shape",Y.shape)  # 30,

  print("X_train:",X_train.shape) # 15,5
  print("X_test:",X_test.shape)   #15,5

  print("Y_train",Y_train.shape)   #15,
  print("Y_test",Y_test.shape)     #15,

######################################################
  print(border)
  print("Step 4:Build the model")
  print(border) 

  model = DecisionTreeClassifier(max_depth=3)

  print("model gets created succesfully")

######################################################
  print(border)
  print("Step 5:train the model")
  print(border)   

  model = model.fit(X_train,Y_train)
  print("Model train succesfully..")

######################################################
  print(border)
  print("Step 6:test the model")
  print(border) 

  Y_pred = model.predict(X_test)

  print("Actual ans :")
  print(Y_test)

  print("Predicted ans:")
  print(Y_pred)

  accuracy = accuracy_score(Y_pred,Y_test)

  print("Acuuracy score is:",accuracy*100)


  
  
   
if __name__ == "__main__":
  main()  

