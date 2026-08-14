import numpy as np

def euc(P1,P2):
  eculidian = np.sqrt((P1['StudyHours']- P2['X'])**2 + (P1['Attendance'] - P2['Y'])**2)
  return eculidian

def passfail(k = 3):
  border = "-"*60

  print(border)
  print("Student details:")

  data = [
    {'StudyHours' : 2,'Attendance':60,'Result':'Fail'},
    {'StudyHours' : 5,'Attendance':80,'Result':'Pass'},
    {'StudyHours' : 6,'Attendance':85,'Result':'Pass'},
    {'StudyHours' : 1,'Attendance':50,'Result':'Fail'}
  ]

  print(border)
  print("Marvellous KNN classifier:")
  for i in data:
    print(i)
  print(border)

  study_hour = int(input("Enter Study_Hour:"))
  percentage = int(input("Enter Percentage"))

  new_point = {'X':study_hour,'Y':percentage}

  print("Distance of all points")
  for d in data:
    d['distance'] = euc(d,new_point)

  for d in data:
    print(d)  

  print(border)   

  sorted_dist = sorted(data,key=lambda item : item['distance'])

  for i in sorted_dist:
    print(i)

  print(border)  

  nearest_sorted = sorted_dist[:3]

  for i in nearest_sorted:
    print("Nearest 3 members:")
    print(i)

  print(border)   

  values = {}

  for neighbors in nearest_sorted:
    Result = neighbors['Result']
    values[Result] = values.get(Result,0)+1

  print(border)
  print("Vote Result is:")
  print(border)

  for i in values:
    print('Result:',i," student number is:",values[i])

  print(border)

  imax = 0
  name = ""

  for i in values:
    if(values[i] > imax):
      imax = values[i]
      name = i

  print("Final Result is:",name)

  print(border)        




def main():
  passfail()

if __name__ == "__main__":
  main()