from Arithmatic import Add,Sub,Mult,Div

def main():
  no1 = int(input("Enter first number:"))
  no2 = int(input("Enter second number:"))

  ret1 = Add(no1,no2)
  print("Addition is :",ret1)

  ret2 = Sub(no1,no2)
  print("Substraction is :",ret2)

  ret3 = Mult(no1,no2)
  print("Multiplication is :",ret3)

  ret4 = Div(no1,no2)
  print("Division is :",ret4)

if __name__ == "__main__":
  main()
