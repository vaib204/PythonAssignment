class Number:
  def __init__(self,A):
    self.value = A

  def CheckPrime(self):
     for i in range(2,self.value):
       if(self.value % i == 0):
         return True
    
     return False
  
  def Checkperfect(self):
    sum = 0
    for i in range(1,self.value):
      if(self.value % i == 0):
        sum = sum + i 
        
    if(sum == self.value):
        print("Number is perfect")   
    else:
       print("Number is not perfect")  

  def DisplayFactor(self):
    for i in range(1,self.value+1):
      if ( self.value % i == 0):
        print("Factors are:",i)  

  def DisplaySumFactor(self):
    sum = 0
    for i in range(1,self.value+1):
      if ( self.value % i == 0):
        sum = sum  + i
    print("Sum of all factor is :",sum)         
         

  
def main():
  num = int(input("Enter number:"))

  nobj1 = Number(num)

  ret = nobj1.CheckPrime()

  if (ret == True):
    print("Number is Not Prime")
  else:
    print("Number is prime")  

  nobj1.Checkperfect() 
  nobj1.DisplayFactor() 
  nobj1.DisplaySumFactor()

if __name__ == "__main__":
  main()

    