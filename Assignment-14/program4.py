max = lambda num1,num2 : num1 < num2 == num1 or num2 > num1 == num1


def main():
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))

  ret = max(num1,num2)
  if (ret == True):
    print("minimum number is:",num1)
  else:
    print("minimum is :",num2)  

if __name__ == "__main__":
  main()  