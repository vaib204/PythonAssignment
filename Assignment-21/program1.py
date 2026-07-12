import threading

def display(data):
  print("Non prime numbers:")
  result  = []
  for i in range(len(data)):
    if i % data[i] == 0:
      result.append(i)
  print(*result)


def nonprime(data):
  print("Prime numbers are:")
  result  = []
  for i in range (len(data)):
    if i % data[i] != 0 and i % 2 == 0:
      result.append(i)
  print(*result)
  



def main(): 
   num = int(input("Enter size of Array:"))
   arr = []

   for i in range(num):
     val = int(input("Enter numbers:"))
     arr.append(val)


   t1 = threading.Thread(target=display,args=(arr,))

   t2 = threading.Thread(target=nonprime,args=(arr,))


   t1.start()
   t2.start()
  
   t1.join()
   t2.join()
  
if __name__ == "__main__":
  main()
  
