import threading
import time

def display():
  print("Numbers from 1 to 50")
  for i in range(1,51,1):
    print(i,end=" ")
  
def reverse():
 time.sleep(2)
 print("Numbers from 50 to 1")
 for j in range(50,0,-1):
   print(j,end=" ")



def main():


  t1 = threading.Thread(target=display)

  t2 = threading.Thread(target=reverse)


  t1.start()
  t2.start()
  
  t1.join()
  t2.join()
  
if __name__ == "__main__":
  main()
  