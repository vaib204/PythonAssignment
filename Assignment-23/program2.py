import multiprocessing
import os
import time

def Odd(no):
  sum = 0
  print("process is runnig with PID :",os.getpid())
  for i in range(1,no+1):
   if (i % 2 != 0):
     sum = sum + i

  return sum

def main():
  start_time = time.perf_counter()

  Arr = []
  val = int(input("Enter the size of list:"))
 
  for i in range(val):
    no = int(input("Enter numbers:"))
    Arr.append(no)

  pobj = multiprocessing.Pool()

  Arr = pobj.map(Odd,Arr)

  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print("sum of odd are:",Arr)

  print(f"Execution time is :{end_time - start_time:.4f}")

if __name__ == "__main__":
  main()
        