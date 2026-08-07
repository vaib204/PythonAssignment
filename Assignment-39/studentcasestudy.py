print("----------------------------------------------------------------------------------")
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
  accuracy_score,
  confusion_matrix,
  classification_report,
)

Border = "_"*60

print(Border)
print("Step 1 : Load the dataset")
print(Border)

datapath = "student_performance_ml.csv"

df = pd.read_csv(datapath)

print("Dataset Loaded succesfully")
print("Initial entries from dataset are:")
print(df.head())

##############################################################################

print(Border)
print("Step 2 : Data Anyalysis")
print(Border)

print("Shape of dataset:")
print(df.shape)

print("Colum names:")
print(list(df.columns))

print("Missing values per colom:")
print(df.isnull().sum())

print("Class distribution (FinalResult)")
print(df["FinalResult"].value_counts())

print("Statistical report of dataset:")
print(df.describe())

##################################################################################

print(Border)
print("Step 3 : Data Visualization")
print(Border)



# Scatter plot
plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"], temp["FinalResult"], label=f"Result {sp}")

plt.title("Marvellous Student Performance Study")
plt.xlabel("Study Hours")
plt.ylabel("Final Result (0=Fail, 1=Pass)")
plt.legend()
plt.grid(True)
plt.show()

##################################################################################

print(Border)
print("Step 4 : Decide dependent independent variable")
print(Border)

# X - Independent Variable / feature 
# Y - Dependent Variable   / labels

feature_col = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

X = df[feature_col]
Y = df["FinalResult"]

print("X shape:",X.shape)
print("Y shape:",Y.shape)

#########################################################################################

print(Border)
print("Step 5 : split the dataset for Train - test - split ")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting activity done")

print("X:",X.shape)
print("Y:",Y.shape)

print("X_train:",X_train.shape) # 30,5
print("X_test:",X_test.shape) # 30,5

print("Y_train:",Y_train) #30,
print("Y_test:",Y_test) #30,

##############################################################################################

print(Border)
print("Step 6 : Model training")
print(Border)

Model = DecisionTreeClassifier(max_depth=1)

print("Model gets created succesfully..")

##################################################################################################

print(Border)
print("Step 7 : train the model")
print(Border)

Model.fit(X_train,Y_train)

print("Model trained succesfully")

###################################################################################################

print(Border)
print("Step 8 : test the model")
print(Border)

Y_pred = Model.predict(X_test)
print("Model testing done")

print("Expectes ans:")
print(Y_test)

print("predicted ans:")
print(Y_pred)

###################################################################################################

print(Border)
print("Step 9 : Accuarcy calculation")
print(Border)

accuracy =  accuracy_score(Y_test,Y_pred)
print("Accuracy of model is:",accuracy*100)

#####################################################################################################

print(Border)
print("Step 10 : Confusion matrix")
print(Border)

matrix =  confusion_matrix(Y_test,Y_pred)
print(matrix)

#####################################################################################################

print(Border)
print("Step 11 : conclusion classification report")
print(Border)

print("Classification report:")
print(classification_report(Y_test,Y_pred))


print("----------------------------------------------------------------------------------")
