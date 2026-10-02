import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

border = "-"*50
#-------------------------------------------------------------------
# Step 1: load the dataset
#-----------------------------------------------------------------

X = np.array([
    [25000, 600, 200000, 10000],
    [40000, 700, 300000, 8000],
    [60000, 750, 500000, 12000],
    [20000, 550, 150000, 15000],
    [80000, 800, 700000, 10000],
    [35000, 650, 250000, 9000],
    [18000, 500, 100000, 12000],
    [90000, 850, 800000, 15000],
    [30000, 580, 200000, 14000],
    [70000, 780, 600000, 10000]
])

# Labels (Y)
Y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

column = ["Income","CreditScore","LoanAmount","ExistingEMI",]
df = pd.DataFrame(X,columns=column)

df["EmployeMentStatus"] = Y

#----------------------------------------------------------------------------
# Step 2 : Clean the dataset
#-------------------------------------------------------------------------

print("Print first 5 rows")
print(df.head())

print("print column names:")
print(df.columns)

print("Check Shape:")
print(df.shape)

print("Statistical memory:")
print(df.describe())

print(border)

#-------------------------------------------------------------------------
# Step 3: Train test split the data
#------------------------------------------------------------------------


X_train,X_test,Y_train,Y_test = train_test_split(
                       X,
                       Y,
                       test_size=0.30,
                       random_state=42

)

print("Shape of traning dataset:",X_train.shape)
print("Shape of testing dataset:",X_test.shape)

print(border)
#------------------------------------------------------------------------------
# Step 4 : Feature scaling
#---------------------------------------------------------------------------


scaler = StandardScaler()

X_train_Scaled = scaler.fit_transform(X_train)
X_test_Scaled = scaler.transform(X_test)

print("Scaled data:")
print(X_test_Scaled[:5])

print(border)

#---------------------------------------------------------------------------------
# Step 5 : Train FNN Model
#-------------------------------------------------------------------------------

model = MLPClassifier(
hidden_layer_sizes=(12,4),
activation='relu',
solver='adam',
random_state=42,
max_iter=1000
)


print(model)

print("Model train")

model.fit(X_train_Scaled,Y_train)

print("Model Training completed")

print(border)

#----------------------------------------------------------------
# Step 6 : Predict the Output
#--------------------------------------------------------------

Ypred = model.predict(X_test_Scaled)

print("Actual Ans:")
print(Y_test)

print("Predicted Ans:")
print(Ypred)

print(border)

#-----------------------------------------------------------
# Step 7: Evaluate Accuracy
#-----------------------------------------------------------

accuracy = accuracy_score(Y_test,Ypred)
print("Accuracy score:",accuracy)

print(border)

#---------------------------------------------------------------
# Step 7 : Data for testing
#-----------------------------------------------------------------

new_customer = pd.DataFrame([[55000,720,400000,10000,]],columns = ["Income","CreditScore","LoanAmount","ExistingEMI"])

new_customer_scaled = scaler.transform(new_customer)

new_pred = model.predict(new_customer_scaled)

new_customer_prob = model.predict_proba(new_customer_scaled)

print("New Student Data:")
print(new_customer)

print("prediction probablity:")
print(new_customer_prob)

prob = new_customer_prob[0][1]

if prob >= 0.5:
  print("Loan  Approved")
else:
  print("Loan not Approved")  

print(border)
