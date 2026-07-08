from functools import reduce

def Even(data):
  return data % 2 == 0

def square(data):
  return data * data

def addition(data,data2):
  return data + data2


def main():
  num = int(input("Enter size of list:"))
  result = []

  for i in range(num):
    val = int(input("Enter Numbers:"))
    result.append(val)

  Fret = list(filter(Even,result))  
  print("Even numbers list :",Fret)

  Mret  = list(map(square,Fret))
  print("square of each number :",Mret)  

  Rret = reduce(addition,Mret)
  print("Addition is :",Rret)
  
if __name__ == "__main__":
  main()