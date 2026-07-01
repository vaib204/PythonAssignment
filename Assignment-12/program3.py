def Addition(no1,no2):
     sum = no1 + no2
     return sum

def substraction(no1,no2):
   sub = no1 - no2
   return sub

def Multiplication(no1,no2):
   mult = no1 * no2
   return mult

def Division(no1,no2):
   div = no1 / no2
   return div


def main():
 number1 = int(input("Enter a number 1:"))
 number2 = int(input("Enter a number 2:"))

 ret1 = Addition(number1,number2)
 print("Addition is :",ret1)

 ret2 = substraction(number1,number2)
 print("Substraction is :",ret2)

 ret3 = Multiplication(number1,number2)
 print("Multiplication is :",ret3)

 ret4 = Division(number1,number2)
 print("Division is :",ret4)



if __name__ == "__main__":
  main()