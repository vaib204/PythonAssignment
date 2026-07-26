import schedule
import time

def DisplayMessage(Name):
  print(Name)


def main():
  name = input("Enter a message :")

  schedule.every(5).seconds.do(DisplayMessage,name)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()