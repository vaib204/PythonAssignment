class Arithmatic:

  def __init__(self,A,B):
    self.no1 = A
    self.no2 = B

  def Accept(self):
    self.val1 = self.no1
    self.val1 = self.no2

  def Addition(self):
    return self.no1 + self.no2
  
  def Substraction(self):
    return self.no1 - self.no2
      
  def Multiplication(self):
    return self.no1 * self.no2

  def Division(self):
    return self.no1 / self.no2

def main():
  no1 = int(input("Enter first number:"))

  no2 = int(input("Enter second number:"))

  aobj = Arithmatic(no1,no2)
  aobj.Accept()
  ret = aobj.Addition()
  print("Addition is :",ret)

  ret = aobj.Substraction()
  print("Substraction is:",ret)

  ret = aobj.Multiplication()
  print("Multiplication is:",ret)

  ret  = aobj.Division()
  print("Division is:",ret)

if __name__ == "__main__":
  main()
