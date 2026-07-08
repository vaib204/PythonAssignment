from functools import reduce

def Prime(data):
  if data == 2:
    return True
  
  for i in range(3,data):
    if i % data == 0:
      return False
    else:
      return True

def multiply(data):
  return data * 2

def max(data,b):
  return data if data > b else b
def main():
  num = int(input("Enter size of list:"))
  result = []

  for i in range(num):
    val = int(input("Enter Numbers:"))
    result.append(val)

  Fret = list(filter(Prime,result))  
  print("Prime numbers list :",Fret)

  Mret  = list(map(multiply,Fret))
  print(" multiply by 2  each number :",Mret)  

  Rret = reduce(max,Mret)
  print("max element is :",Rret)
  
if __name__ == "__main__":
  main()