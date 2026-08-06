import pandas as pd

#############################
#step 1 : Load the dataset
#############################

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



