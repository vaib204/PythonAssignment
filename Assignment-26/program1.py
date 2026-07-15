class Demo:
  value = 0

  def __init__(self,A,B):
    self.no1 = A
    self.no2 = B

  def Fun(self):
    print("Value of Fun:",self.no1)
    print("Value of Fun:",self.no2)

  def Gun(self):
  
   print("Value of Gun:",self.no1)
   print("Value of Gun:",self.no2)

def main():
  obj1 = Demo(11,21)
  obj2 = Demo(51,101)

  obj1.Fun()
  obj2.Fun()
  
  print("__________________________________")
   
  obj1.Gun()
  obj2.Gun()


if __name__ == "__main__":
  main()
    
