#------------------------------------------------
# Step 1 : Import the Libraries
#-----------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network  import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import log_loss

#------------------------------------------------
# Step 2 : Load the dataset
#-----------------------------------------------
df = pd.read_csv("Employee_Attrition.csv")
print("Display 5 rows:")
print(df.head())

print("Display shape:")
print(df.shape)

print("Coumn names:")
print(df.columns)

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 3 : Data Analysis
#-----------------------------------------------

print("Check missing values:")
print(df.isnull().sum())

print("Catagorical columns:")
df.select_dtypes(include=['object','string','category']).columns  

print("Numerical columns:")
print(df.select_dtypes(include=['int64','float64']).columns)

print("Labelencoding For OverTime:")
le = LabelEncoder()

# Loop through categorical columns and overwrite them directly
for col in df.select_dtypes(include=['object','string','category']).columns:
    df[col] = le.fit_transform(df[col])   # modifies df in place

print(df.head())

print("Labelencoding For Attrition:")
le = LabelEncoder()

# Encode all categorical columns directly in the DataFrame
for col in df.select_dtypes(include=['object','string','category']).columns:
    df[col] = le.fit_transform(df[col])

print(df.head())

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 4 : Preprocessing
#-----------------------------------------------
print("Seprate the Features:")
X = df.drop(['Attrition'],axis=1)
print("Features:",X.shape)

print("Label:")
Y = df["Attrition"]
print("Label:",Y.shape)

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 5 : Apply Train-Test-Split
#-----------------------------------------------
print("Apply Train test split method")
X_train,X_test,Y_train,Y_test = train_test_split(
                                       X,
                                       Y,
                                       test_size=0.30,
                                       random_state=42
)

print("Shape of Training X_train:",X_train.shape)
print("Shape of Testing X_test:",X_test.shape)

print("Shape of Training Y_train:",Y_train.shape)
print("Shape of Testing Y_test:",Y_test.shape)

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 5 : Apply stndard scaler
#-----------------------------------------------
print("Apply standard scaler:")

scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

print("Scaled trained data:")
print(X_test_scale[:5])

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 6 : Design a MLP model 
#-----------------------------------------------

print("Design a MLP Model:")

model = MLPClassifier(
    hidden_layer_sizes=(15,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print(model)

print("Train the model:")

model.fit(X_train_scale,Y_train)

print("Model Traning completed")

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 7 : Model Evaluation
#-----------------------------------------------

print("Model Evaluation:")

Y_pred = model.predict(X_test_scale)

Accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is :",Accuracy*100)

confusion = confusion_matrix(Y_test,Y_pred)
print("Confusion matrix:")
print(confusion)

print("Plot the loss curve:")
Y_pred_proba = model.predict_proba(X_test_scale)
loss = log_loss(Y_test, Y_pred_proba)

print("Log Loss:", loss)

print("--------------------------------------------------------------------")

print("Test New Records:")

new_Employe = pd.DataFrame([[41,60000,8,63,45,4,3,1,6,6]],columns=['Age','MonthlyIncome','YearsAtCompany','TotalWorkingYears','DistanceFromHome','JobSatisfaction','WorkLifeBalance','OverTime','NumCompaniesWorked','TrainingTimesLastYear'])

new_Employe2 = pd.DataFrame([[42,67304,6,15,44,2,1,1,4,6]],columns=['Age','MonthlyIncome','YearsAtCompany','TotalWorkingYears','DistanceFromHome','JobSatisfaction','WorkLifeBalance','OverTime','NumCompaniesWorked','TrainingTimesLastYear'])

new_Employe_scaled = scaler.transform(new_Employe)
new_Employe_scaled2 = scaler.transform(new_Employe2)


new_predicition = model.predict(new_Employe_scaled)
new_predicition2 = model.predict(new_Employe_scaled2)

new_probablity = model.predict_proba(new_Employe_scaled)
new_probablity2 = model.predict_proba(new_Employe_scaled2)

print("New Employe Data :")
print(new_Employe)
print("Prediction probablity:",new_probablity)

if new_predicition[0] == 1:
  print("Prediction : Yes")
else:
  print("Prediction : No")

print("-------------------------------------------------------------------")

print("New Employe Data 2 :")
print(new_Employe2)
print("Prediction probablity:",new_probablity2)

print("Employe 2:")
if new_predicition2[0] == 1:
  print("Prediction : Yes")
else:
  print("Prediction : No")





