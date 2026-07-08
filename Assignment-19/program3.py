from functools import reduce

def greter(data):
 return data >= 70 and data <= 90

def increse(data):
 return data + 10

def product(data,data2):
  return data * data2


def main():
  number = int(input("Enter the size of list:"))
  result = []

  for i in range(number):
    val = int(input("Enter Numbers:"))
    result.append(val)

  Fret = list(filter(greter,result))
  print(Fret) 

  Mret = list(map(increse,Fret))
  print(Mret)

  rret = reduce(product,Mret)
  print(rret) 


if __name__ == "__main__":
  main()