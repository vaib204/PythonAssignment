Sum = lambda no1,no2: no1 + no2

def main():
  num1 = int(input("Enter 1 number:"))
  num2 = int(input("Enter 2 number:"))

  ret = Sum(num1,num2)

  print("Addition is:",ret)

if __name__ == "__main__":
  main()