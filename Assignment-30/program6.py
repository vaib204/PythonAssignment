import schedule
import time
import datetime


def LunchTime():
  print("Lunch Time..")

def WrapUpWork():
  print("Wrap your work")


def main():
  
  schedule.every().day.at("13.00pm").do(LunchTime)
  schedule.every().day.at("18:00pm").do(WrapUpWork)

  while True:
    schedule.run_pending()
    time.sleep(60)

if __name__ == "__main__":
  main()  