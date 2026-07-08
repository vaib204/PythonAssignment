def Sum(data):
  sum = 0
  for i in data:
    sum = sum + i
  return sum  

def main():
  number = int(input("Enter a number:"))
  result = []

  for i in range(number):
    val = int(input("Enter Numbers:"))
    result.append(val)

  iret = Sum(result)  
  print("Addition is :",iret)


if __name__ == "__main__":
  main()
