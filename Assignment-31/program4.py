import schedule
import time

def Display():

  timestamp = time.ctime()

  log = "MarvellousLog%s.log"%(timestamp)
  

  print("Log files gets created succesfully",log)

  log = log.replace(" ","_") 
  log = log.replace(":","_")

  fobj = open(log,"w")

  print("cretation time:",time.time())
  

def main():
 
 schedule.every(15).seconds.do(Display)
 
 while True:
   schedule.run_pending()
   time.sleep(1)



if __name__ == "__main__":
   main()