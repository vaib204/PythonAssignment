from ast import arg
import threading

def Sum(data):
  sumx = 0
  for i in range(len(data)):
      sumx = sumx + data[i]

  print("Addition  is:",sumx)


def product(data):
  pr = 1
  for i in range(len(data)):
     pr = pr * data[i]

  print("product is:",pr)

  
def main(): 
   num = int(input("Enter size of Array:"))
   arr = []

   for i in range(num):
     val = int(input("Enter numbers:"))
     arr.append(val)


   t1 = threading.Thread(target=Sum,args=(arr,))

   t2 = threading.Thread(target=product,args=(arr,))


   t1.start()
   t2.start()
  
   t1.join()
   t2.join()
  
if __name__ == "__main__":
  main()
  