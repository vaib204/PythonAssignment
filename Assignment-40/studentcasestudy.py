import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


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

  X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=45)

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

######################################################
  print(border)
  print("Step 7:Model feature importance")
  print(border) 

  imax = 4.5
  print("Study Hours of those student whose getting chanses of pass is more")
  t1 = df[feature_col[0]]
  for i in t1:
    if (i > imax):
      imax = i
      print(imax)

  print(border)
  
  print("Attendence and studyhour most predicting final result")

  print("Assinment completed feature contribute the least")

  ##################################################  
  
  print(border)
  print("Step 8:Remove the column sleephour from the dataset")
  print(border)

  df = df.drop(columns=["SleepHours"])

  print(df.head())

  model = model.fit(X_train,Y_train)

  Y_pred = model.predict(X_test)

  accuracy = accuracy_score(Y_test,Y_pred)

  print("Accuracy score is:",accuracy*100)

  
##################################################
  print(border)
  print("Step 8:Train the model using only study hour attendance")
  print(border)

  df = df.drop(columns=["PreviousScore"])
  df = df.drop(columns = ["AssignmentsCompleted"])
  
  print(df.head())

  model = model.fit(X_train,Y_train)

  Y_pred = model.predict(X_test)

  accuracy = accuracy_score(Y_test,Y_pred)

  print("Accuracy score is:",accuracy*100)

######################################################
  print(border)
  print("Step 8 : Without using accuracy_score")
  print(border)

  model = model.fit(X_train, Y_train)
  Y_pred = model.predict(X_test)

  correct = 0
  for i in range(len(Y_test)):
      if Y_test.iloc[i] == Y_pred[i]:
          correct += 1

  
  total = len(Y_test)  
  accuracy = (correct / total) * 100
  print("Accuracy is :", accuracy)

###################################################
  print(border)
  print("Step 8 :Identify students")
  print(border)

  model = model.fit(X_train, Y_train)
  Y_pred = model.predict(X_test)

  check = (Y_test.to_numpy() != Y_pred)
  print(df.loc[X_test.index][check])

###################################################
  print(border)
  print("Step 9 :Visualize")
  print(border)

  plt.figure(figsize=(8,7))
  plot_tree(
    model,
    filled=True,
    feature_names=X_train.columns,   # actual feature names
    class_names=["Fail", "Pass"]     # actual target labels
)
  plt.show()
  
  
   
if __name__ == "__main__":
  main()  

