Mult = lambda num1,num2 : (num1 * num2)

def main():
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter seconed number:"))

  ret = Mult(num1,num2)

  print("Multiplication is:",ret)

if __name__ == "__main__":
  main()