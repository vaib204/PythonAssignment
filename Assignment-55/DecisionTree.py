import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score


######################################################
# Step 1 : Load the Dataset
#####################################################

df = pd.read_csv("Customer_Loan_Approval.csv")

print(df.head())

######################################################
# Step 2 : Check the missing values
#####################################################

print("Missing values:")
print(df.isnull().sum())

######################################################
# Step 3 : Seprate the input  and output Variable
#####################################################

X = df.drop("LoanApproved",axis=1)
Y = df["LoanApproved"]

print("Xshape:",X.shape)
print("Yshape:",Y.shape)

######################################################
# Step 4 : Split the dataset into training and testing data
#####################################################

X_train,X_test,Y_train,Y_test = train_test_split(
  X,
  Y,
  test_size=0.2,
  random_state=42
)

######################################################
# Step 5: Train the model
#####################################################

model = DecisionTreeClassifier(max_depth=3,random_state=42)

model = model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("Actual ans:")
print(Y_test)

print("Predicted ans:")
print(Y_pred)

print("Accuracy score:")
print(accuracy_score(Y_test,Y_pred))
