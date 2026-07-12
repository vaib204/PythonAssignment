import multiprocessing
import os

def square(no):
  sum = 0
  for i in range(no):
    sum = sum + i*i

  return sum 

def main():
  Arr = []
  val = int(input("Enter the size of list:"))
 
  for i in range(val):
    no = int(input("Enter numbers:"))
    Arr.append(no)

  pobj = multiprocessing.Pool()

  Arr = pobj.map(square,Arr)

  pobj.close()
  pobj.join()

  print("Result is:")
  print(Arr)

if __name__ == "__main__":
  main()
        
