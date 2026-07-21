import schedule
import time

def Display():
  print("Jay Ganesh.. Namaskar")

def main():

  schedule.every().day.at("9.00").do(Display)

  while True:
    schedule.run_pending()
    time.sleep(60)

if __name__ == "__main__":
  main()