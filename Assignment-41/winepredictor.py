import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def main():
  border  = "-"*70

  datapath = "WinePredictor.csv"

  print(border)
  print("step 1 : Load the Dataset")
  print(border)

  df = pd.read_csv(datapath)

  print(border)
  print(df.head())
  print(border)

#########################################################################################

  print(border)
  print("step 2 : Clean the Dataset")
  print(border)

  df.dropna(inplace=True)

  print("Shape of dataset:",df.shape)
  print("Total records:",df.shape[0])
  print("Total colom:",df.shape[1])

  print(border)

###########################################################################################  

  print(border)
  print("step 3 : Seprate Independent and dependent variable")
  print(border)

  X = df.drop(columns=['Class'])
  Y = df['Class']

  print("Shape of X:",X.shape)
  print("Shape of Y:",Y.shape)

  print(border)
  print("Input coloms:",X.columns.to_list())
  print("Output coloms:","Class")
  print(border)
##############################################################################################

  print(border)
  print("step 4 : Split the dataset for training and testing")
  print(border)  

  X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

  print("X_train",X_train.shape)
  print("X_test",X_test.shape)
  print("Y_train",Y_train.shape)
  print("Y_test",Y_test.shape)

##############################################################################################

  print(border)
  print("step 5 : Build the Model")
  print(border)  

  Model = KNeighborsClassifier(n_neighbors=5)

##############################################################################################
 
  print(border)
  print("step 5 : Train the Model")
  print(border)  

  Model = Model.fit(X_train,Y_train)

  print("Model trainig completed")

###############################################################################################

 
  print(border)
  print("step 6 : Test the Model")
  print(border)  

  Y_pred = Model.predict(X_test)

  accuracy = accuracy_score(Y_test,Y_pred)
  print("Model accuracy is:",accuracy*100)

  print(border)

if __name__ == "__main__":
  main()
