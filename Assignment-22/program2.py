import multiprocessing
import os

def factoral(no):
  print("process is runnig with PID :",os.getpid())
  fact = 1
  for i in range(1,no+1):
   fact = fact * i

  return fact

def main():
  Arr = []
  val = int(input("Enter the size of list:"))
 
  for i in range(val):
    no = int(input("Enter numbers:"))
    Arr.append(no)

  pobj = multiprocessing.Pool()

  Arr = pobj.map(factoral,Arr)

  pobj.close()
  pobj.join()

  print("Result is:")
  print(Arr)

if __name__ == "__main__":
  main()
        