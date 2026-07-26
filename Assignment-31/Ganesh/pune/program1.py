import schedule
import time

def Display(name):
   print(name)


def main():
 name = input("Enter a message :")
 Time = int(input("Enter time interval in second:"))


 schedule.every(Time).seconds.do(Display,name)
 
 while True:
   schedule.run_pending()
   time.sleep(1)



if __name__ == "__main__":
   main()