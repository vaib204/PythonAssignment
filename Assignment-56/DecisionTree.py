import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score

#############################################
# Step 1: Load the Dataset
#############################################

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print(df.head())

#############################################
# Step 2: Select the features and columns
#############################################

X = df.drop("Fraud",axis=1)

Y = df["Fraud"]

print("X shape:",X.shape)
print("Y shape:",Y.shape)

#############################################
# Step 3: Train the dataset
#############################################

X_train,X_test,Y_train,Y_test = train_test_split(
  X,
  Y,
  test_size= 0.2,
  random_state=42
)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)

#############################################
# Step 4: Select the Model
#############################################

model  = DecisionTreeClassifier()

model =  model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("Actual Ans :")
print(Y_test)

print("Predicted Ans:")
print(Y_pred)

#############################################
# Step 5: Evaluate the model
#############################################

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is:",accuracy)


confusion = confusion_matrix(Y_test,Y_pred)
print("Confusion is:")
print(confusion)

precsion = precision_score(Y_test,Y_pred)
print("Precision is:",precsion)

recall = recall_score(Y_test,Y_pred)
print("Recall is:",recall)

f1 = f1_score(Y_test,Y_pred)
print("f1_score is:",recall)
