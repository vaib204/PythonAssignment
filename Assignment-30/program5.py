import schedule
import time
import datetime

def Display():
 fobj = open("Demo.txt","a")

 cs = datetime.datetime.now()

 fobj.write(str(cs)+"\n")

 
def main():

  schedule.every(5).minutes.do(Display)

  while True:
    schedule.run_pending()
    time.sleep(60)

if __name__ == "__main__":
  main()