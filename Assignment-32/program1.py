import schedule
import time
from datetime import date

def display():
  timestamp = time.ctime()

  log = "File%s.txt"%(timestamp)

  log = log.replace(" ","_")
  log = log.replace(":","_")

  fobj = open(log,"w")

  fobj.write(f"file name is:{log}\n")
  fobj.write(f"creation date:{date.today()}\n")
  fobj.write(f"creation time:{time.ctime()}\n")


def main():

  schedule.every(5).seconds.do(display)

  while True:
    schedule.run_pending()
    time.sleep(5)

if __name__ == "__main__":
  main()
