import multiprocessing
import os
import time

def power(no):
  sum = 0
  print("process is runnig with PID :",os.getpid())
  for i in range(1,no+1):
   sum = sum +  i ** 5

  return sum

def main():
  start_time = time.perf_counter()

  Arr = []
  val = int(input("Enter the size of list:"))
 
  for i in range(val):
    no = int(input("Enter numbers:"))
    Arr.append(no)

  pobj = multiprocessing.Pool()

  Arr = pobj.map(power,Arr)

  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print("Result is:")
  print(Arr)

  print(f"Execution time is :{end_time - start_time:.4f}")

if __name__ == "__main__":
  main()
        