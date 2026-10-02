import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

border = "-"*50
#----------------------------------------------------------
# Step 1 : Load the dataset
#----------------------------------------------------------

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

Y = ([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

column = ["Age","Monthly Charge","Tenure","Complaints","Support calls"]
df = pd.DataFrame(X,columns=column)

df["outcome"] = Y

#----------------------------------------------------------------
# Step 2 : Clean the dataset
#-----------------------------------------------------------------


print("Print first 5 rows")
print(df.head())

print("print column names:")
print(df.columns)

print("Check Shape:")
print(df.shape)

print("Statistical memory:")
print(df.describe())

print(border)
#-----------------------------------------------------------------
# Step 3: Train test split the data
#-----------------------------------------------------------------
X_train,X_test,Y_train,Y_test = train_test_split(
                       X,
                       Y,
                       test_size=0.3,
                       random_state=42

)

print("Shape of traning dataset:",X_train.shape)
print("Shape of testing dataset:",X_test.shape)

print(border)
#-----------------------------------------------------------------
# Step 4 : Feature scaling
#-----------------------------------------------------------------
scaler = StandardScaler()

X_train_Scaled = scaler.fit_transform(X_train)
X_test_Scaled = scaler.transform(X_test)

print("Scaled data:")
print(X_test_Scaled[:5])

print(border)

#-----------------------------------------------------------------
# Step 5 : Train FNN Model
#-----------------------------------------------------------------
model = MLPClassifier(
  hidden_layer_sizes=(5,3),
  activation='relu',
  solver='adam',
  max_iter=500,
  random_state=42
)

print(model)

print("Model train")

model.fit(X_train_Scaled,Y_train)

print("Model Training completed")

print(border)

#---------------------------------------------------------
# Step 6 : Predict the output
#---------------------------------------------------------
Ypred = model.predict(X_test_Scaled)

print("Actual Ans:")
print(Y_test)

print("Predicted Ans:")
print(Ypred)

print(border)

#------------------------------------------------------
# Step 7: Evaluate Accuracy
#-----------------------------------------------------

accuracy = accuracy_score(Y_test,Ypred)
print("Accuracy score:",accuracy)

print(border)

#-------------------------------------------------------
# Step 7 : Data for testing
#------------------------------------------------------

new_customer = pd.DataFrame([[46,1450,5,6,9]],columns = ["Age","Monthly Charge","Tenure","Complaints","Support calls"])

new_customer_scaled = scaler.transform(new_customer)

new_pred = model.predict(new_customer_scaled)

new_customer_prob = model.predict_proba(new_customer_scaled)

print("New Student Data:")
print(new_customer)

print("prediction probablity:")
print(new_customer_prob)

prob = new_customer_prob[0][1]

if prob >= 0.5:
  print("Customer will leave")
else:
  print("Customer will Stay")  

print(border)

