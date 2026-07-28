import schedule
import time
import os
from datetime import datetime


def display():
  timestamp = time.ctime()

  log = "Filesizelog%s.txt"%(timestamp)

  log = log.replace(" ","_")
  log = log.replace(":","_")

  fobj = open("demo.txt","r")
  cobj = open(log,"w")

  Ret = False

  Ret = os.path.exists("demo.txt")
  if(Ret == False):
    print("Marvellous Automation Errror : There is no such file with name","demo.txt")
    return

  cobj.write(f"{os.path.abspath("demo.txt")}\n")
  cobj.write(f"{timestamp}\n")
  cobj.write(f"{os.path.getsize("demo.txt")}")



def main():

  schedule.every(5).seconds.do(display)

  while True:
    schedule.run_pending()
    time.sleep(5)

if __name__ == "__main__":
  main()