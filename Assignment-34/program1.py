import sys
import schedule
import os
import psutil
import time

def Process_id():
   list = []
   for proc in psutil.process_iter():
      info = proc.as_dict(attrs=["name","pid","username"])
      list.append(info)

   return list   

def DisplayInfo(FolderName):
   ret = False

   ret = os.path.exists(FolderName)

   if(ret == True):
      ret = os.path.isdir(FolderName)
      if(ret == False):
         print("unable to procces as a directory name is existing but its not a directory ")
         return
   else:
      os.mkdir(FolderName)
      print("Directory for the log file gets created ..")

   timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

   Filename = os.path.join(FolderName,"marvellous_%s.log"%timestamp)

   fobj  = open(Filename,"w")

   print(f"Log file gets created with name {Filename}")  

   rs = Process_id()

   for data in rs:
      fobj.write(f"{data}\n")

   fobj.close()   

   
def main():
  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "H"):
        print("This automation script is used to perform ")
        print("1 : It fetch the information of running processess")

    if(sys.argv[1] == "--u" or sys.argv[1] == "u"):
        print("Use the automation script as : ")
        print(f"python {sys.argv[0]} Time_Interval Folder_Name")
        print("Time_Interval : Time in minutes for periodic execution")
        print("Folder_Name : Name of folder for the log file creation")

  elif(len(sys.argv) == 3):

       print("schedular started succesfully...")
       print("press ctr + c abort the script")

       schedule.every(int(sys.argv[1])).minutes.do(DisplayInfo,sys.argv[2])

       while True:
          schedule.run_pending()
          time.sleep(1)   

  else:
        print("Invalid number of argumenst")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

        print("-------------------------------------------------")
        print("--- Thank you for using our automation System ---")
        print("-------------------------------------------------")      


if  __name__ == "__main__":
   main()
            
       
