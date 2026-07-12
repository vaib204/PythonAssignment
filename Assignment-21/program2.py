import threading

def Maximum(data):
  max = 0
  for i in range(len(data)):
      if (data[i] > max):
        max = data[i]

  print("max element is:",max)


def minimum(data):
  min = data[0]
  for i in range(len(data)):
      if (data[i] < min):
        min = data[i]

  print("min element is:",min)

  

def main(): 
   num = int(input("Enter size of Array:"))
   arr = []

   for i in range(num):
     val = int(input("Enter numbers:"))
     arr.append(val)


   t1 = threading.Thread(target=Maximum,args=(arr,))

   t2 = threading.Thread(target=minimum,args=(arr,))


   t1.start()
   t2.start()
  
   t1.join()
   t2.join()
  
if __name__ == "__main__":
  main()
  