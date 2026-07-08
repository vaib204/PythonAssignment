import threading

def Even(num):
  result = []
  for i in range(1,num+1):
   if i % 2 == 0:
     result.append(i)
  print("Even numbers are:",*result) 


def Odd(num):
  result = []
  for i in range(1,num+1):
   if i % 2 != 0:
     result.append(i)
  print("Odd numbers are:",*result) 
   
  

def main():
  number = int(input("Enter a number:"))

  tobj1 = threading.Thread(target=Even,args=(number,))


  tobj2 = threading.Thread(target=Odd,args=(number,))

  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()


if __name__ == "__main__":
  main()
