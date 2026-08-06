import pandas as pd

#############################
#step 1 : Load the dataset
#############################
cnt = 0
print("____________________")
print("step 1 : Load the dataset")
print("____________________")

dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)

print("first 5 entries :")
print(df.head())

print("_______________________________")

print("Last 5 records:")
print(df.tail(5))

print("______________________________  ")

print("Total numbers of colum are:")
print(len(list(df.columns)))

print("Total numbers of rows are:")
print(len(df))

print("name  of colum are:")
print((list(df.columns)))

print("data type of colum are:")
for x in df:
  print(type(x))

print("_________________________________")

#############################
#step 2 : Display total number of students
#          count how many student passed
#          count howw many student fail
#############################

print("____________________")
print("step 2 : 1]Display total number of students 2]count how many student passed 3]count how many student fail")
print("____________________")

print("Total number of student in the dataset:")
print(len(df))

print("passed student count is:")
pass_student = (df["FinalResult"] == 1).sum()
print(pass_student)

print("Failed  student count is:")
pass_student = (df["FinalResult"] == 0).sum()
print(pass_student)

