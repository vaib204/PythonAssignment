import multiprocessing
import os

def prime(no):
  print("process is runnig with PID :",os.getpid())
  for i in range(2,no+1):
    if (i % 1 == 0 and )
   

  return fact

def main():
  Arr = []
  val = int(input("Enter the size of list:"))
 
  for i in range(val):
    no = int(input("Enter numbers:"))
    Arr.append(no)

  pobj = multiprocessing.Pool()

  Arr = pobj.map(prime,Arr)

  pobj.close()
  pobj.join()

  print("Result is:")
  print(Arr)

if __name__ == "__main__":
  main()
        