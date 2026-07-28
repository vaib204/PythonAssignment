import schedule
import time
import os

def display(name):
 try:
  fobj = open(name,"r")
  Ret = os.path.exists(name)

  if(Ret == True):
      print("file is exist")

  if(os.path.getsize(name) == 0):
          print("File is empty")
         
 except FileNotFoundError as fobj:
    print("file does not exist..")
    print("permission denied")
    print("file can not be opened")
   
    
def main():

  name = input("Enter a file name:")

  schedule.every(5).seconds.do(display,name)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()