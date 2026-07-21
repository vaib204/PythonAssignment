import schedule
import shutil
import datetime
import time
import os

def Display():
   
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    shutil.copy("Demo.txt", f"Marvellous/backup_{timestamp}.txt")

    LogFileName = f"Backup completed successfully at {timestamp}.log"
    print(LogFileName)

def main():
    schedule.every(1).hours.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
