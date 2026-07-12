import multiprocessing
import os
import time

def Even(no):
  sum = 0
  for i in range(1,no+1):
   if (i % 2 == 0):
     sum = sum + i

  return sum

def main():
  print("process is runnig with PID :",os.getpid())
  start_time = time.perf_counter()

  Arr = []

  val = int(input("Enter the size of list:"))
 
  for i in range(val):
    no = int(input("Enter numbers:"))
    Arr.append(no)

  pobj = multiprocessing.Pool()

  Arr = pobj.map(Even,Arr)

  print("Data  = ",Arr)

  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print("Sum of Even Number:",Arr)

  print(f"Execution time is :{end_time - start_time:.4f}")

if __name__ == "__main__":
  main()
        
