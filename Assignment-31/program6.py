import schedule
import time

def Mon():
   print("Starts your weekly goals")

def wed():
  print("Review your weekly progress")

def fri():
  print("week work completed..")     


def main():

 schedule.every().monday.at("9.00").do(Mon)

 schedule.every().wednesday.at("5.00").do(wed)

 schedule.every().friday.at("6.00").do(fri)
 
 while True:
   schedule.run_pending()
   time.sleep(1)



if __name__ == "__main__":
   main()