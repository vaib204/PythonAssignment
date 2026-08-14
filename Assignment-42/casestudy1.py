import numpy as np

def CalculateEuc(P1,P2):
  Ans = np.sqrt((P1['X']-P2['X'])**2 + (P1['Y']-P2['Y'])**2)
  return Ans


def ColorDataset(k = 3):
  border = "-"*60

  print(border)

  Data = [
    {'Point':'A','X':1,'Y':2,'label':'Red'},
    {'Point':'B','X':2,'Y':3,'label':'Red'},
    {'Point':'C','X':3,'Y':1,'label':'Blue'},
    {'Point':'D','X':6,'Y':5,'label':'Blue'}
  ]

  print(border)
  print("Knn classifier")

  for i in Data:
    print(i)

  print(border)

  newpointx = int(input("Enter for X value:"))
  newpointy = int(input("Enter for Y value:"))

  newpoint = {'X' : newpointx,'Y':newpointy}

  print("distance of all points:")
  for d in Data:
    d['distance'] = CalculateEuc(d,newpoint)  

  for d in Data:
    print(d)

  print(border)    

  sorted_data = sorted(Data,key= lambda item : item['distance'])

  print(border)
  print("Sorted data:")
  print(border)

  for d in sorted_data:
    print(d)

  print(border)

  nearest = sorted_data[:k]
  print(border)
  print("Nearest 3 members:")
  print(border)

  for d in nearest:
    print(d)

  print(border)

  votes = {}

  for neighbours in nearest:
    label = neighbours['label']
    votes[label] = votes.get(label,0)+1

  print(border)
  print("Vote result is:")
  print(border)

  for d in votes:
    print("name:",d,"number of votes:",votes[d])

  print(border)

  imax = 0
  name = ""

  for d in votes:
    if(votes[d] > imax):
           imax = votes[d]
           name = d
  print("final prediction is name:",name)         



def main():
  ColorDataset()

if __name__ == "__main__":
  main()
