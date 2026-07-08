import threading

def EvenFactors(num):
  sum1 = 0
  for i in range(1,num+1):
   if num % i == 0:
      if i % 2 == 0:
       sum1 = sum1 + i
  print("summation of even is :",sum1) 


def OddFactor(num):
  sum2 = 0
  for i in range(1,num+1):
   if num % i == 0:
      if i % 2 != 0:
       sum2 = sum2 + i
  print("Summation of odd is:",sum2) 
    
  

def main():
  number = int(input("Enter a number:"))

  tobj1 = threading.Thread(target=EvenFactors,args=(number,))


  tobj2 = threading.Thread(target=OddFactor,args=(number,))

  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()


if __name__ == "__main__":
  main()