def Checkgreater(no1,no2):
  if(no1 > no2):
    print("greter Number is :",no1)
  else:
    print("greter number is:",no2)  

def main():
  no1 = int(input("Enter first number:"))
  no2 = int(input("Enter seconed number:"))

  Checkgreater(no1,no2)

if __name__ == "__main__":
  main()