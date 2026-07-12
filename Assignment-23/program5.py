import multiprocessing
import os
import time

def Fact(no):
  Fact = 1
  for i in range(1,no+1):
   Fact = Fact * i
   
  return Fact

def main():
  print("process is runnig with PID :",os.getpid())
  start_time = time.perf_counter()

  Arr = []
  val = int(input("Enter the size of list:"))
 
  for i in range(val):
    no = int(input("Enter numbers:"))
    Arr.append(no)

  pobj = multiprocessing.Pool()

  Arr = pobj.map(Fact,Arr)

  print("Data = ",Arr)

  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print("Factorials are:",Arr)

  print(f"Execution time is :{end_time - start_time:.4f}")

if __name__ == "__main__":
  main()
        