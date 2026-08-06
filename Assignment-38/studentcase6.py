import pandas as pd
import matplotlib.pyplot as plt

#############################
#step 1 : Load the dataset
#############################
cnt = 0
print("_____________________________________________________________")
print("step 1 : Load the dataset")
print("_____________________________________________________________")

dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)

print("first 5 entries :")
print(df.head())

print("Last 5 records:")
print(df.tail(5))

print("Total numbers of colum are:")
print(len(list(df.columns)))

print("Total numbers of rows are:")
print(len(df))

print("name  of colum are:")
print((list(df.columns)))

print("data type of colum are:")
for x in df:
  print(type(x))


#############################
#step 2 : Display total number of students
#          count how many student passed
#          count howw many student fail
#############################
print("_____________________________________________________________")
print("step 2 : 1]Display total number of students 2]count how many student passed 3]count how many student fail")
print("_____________________________________________________________")

print("Total number of student in the dataset:")
print(len(df))

print("passed student count is:")
pass_student = (df["FinalResult"] == 1).sum()
print(pass_student)

print("Failed  student count is:")
pass_student = (df["FinalResult"] == 0).sum()
print(pass_student)

##############################################
#step 3 :1] Average study hours 2]Average Attendence 3]Maximum previous score 4]MaximumSleephour
##############################################
print("_____________________________________________________________")
print("step 3 :1] Average study hours 2]Average Attendence 3]Maximum previous score 4]MaximumSleephour")
print("_____________________________________________________________")

print("Average study hours:")

Avg = df["StudyHours"]

total_sum = sum(Avg)
count = len(Avg)
Average = total_sum / count

print(Average)

print("Average Attendence:")

Avg = df["Attendance"]

total_sum = sum(Avg)
count = len(Avg)
Average = total_sum / count

print(Average)

print("Maximum previous score")

Max = df["PreviousScore"]

max = 0

for i in Max:
  if i > max:
    max = i
print(max)

print("Maximum sleep hour")

Max = df["SleepHours"]

max = 0

for i in Max:
  if i > max:
    max = i

print(max)

##############################################
#step 4 :use values_count() to analyze the distribution of final result calculate the percentage of pass and fail student is the dataset balanced?justify your ans?
##############################################
print("_____________________________________________________________")
print("step 4 :use values_count() to analyze the distribution of final result calculate the percentage of pass and fail student is the dataset balanced?justify your ans?")
print("_____________________________________________________________")

print("Total percentage of :")

per1 = df["FinalResult"].value_counts(1)
final = per1 * 100
print(final)
print("Unbalanced dataset because it shows 60 and 40 percent ")

##############################################
#step 5 :Analyze:
#higher studyhours increase the chance of passing
#higher Attendance improves FinalResult write Your observation in 4- 5 lines
##############################################
print("_____________________________________________________________")
print("step 5 :Analyze:1] higher studyhours increase the chance of passing 2 ]higher Attendance improves FinalResult write Your observation in 4- 5 lines")
print("_____________________________________________________________")

##############################################
#step 6 : Plot Histogram Of Study Hours
##############################################
print("_____________________________________________________________")
print("step 6 : Plot Histogram Of Study Hours")
print("_____________________________________________________________")

plt.hist(df["StudyHours"],bins=20,color="skyblue",edgecolor = "black")

plt.title("Total Study Hours")

plt.show()




