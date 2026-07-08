Mult = lambda no1,no2 : no1 * no2

def main():
  number1 = int(input("Enter first number:"))
  number2 = int(input("Enter second number"))

  iret =  Mult(number1,number2)

  print(f" Multiplication of {number1,number2} is:",iret)

if __name__ == "__main__":
  main()
