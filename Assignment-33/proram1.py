import os
import sys
import hashlib
import schedule
import time

def CalculateCheckSum(filename):     
   fobj = open(filename,"rb")


   hobj = hashlib.md5()

   Buffer = fobj.read(1024)

   while (len(Buffer) > 0):
      hobj.update(Buffer)
      Buffer = fobj.read(1024)

   fobj.close()

   return hobj.hexdigest()  
########################################################################################

def FindDuplicate(Directory):
   Border = "_"*70
   timestamp = time.ctime()
       
   LogFileName = "Marvellous%s.log"%(timestamp)
   LogFileName = LogFileName.replace(" ","_")
   LogFileName = LogFileName.replace(":","_")
       
   fobj = open(LogFileName,"w")
     
   print("Log file gets created succesfully")
   Ret = False

   Ret = os.path.exists(Directory)

   if(Ret == False):
        print("Path is invalid")
        return

   Ret = os.path.isdir(Directory)

   if(Ret == False):
        print("It is not a directory")

   Duplicate = {}

   unique = 0
   same = 0

   for FolderName,SubFolderName,FileName in os.walk(Directory):
     for fname in FileName:
      fname = os.path.join(FolderName,fname)

      checksum = CalculateCheckSum(fname)

      if checksum in Duplicate:
        same = same + 1
        Duplicate[checksum].append(fname)
      else:
        unique = unique + 1
        Duplicate[checksum] = [fname]

   return Duplicate,same,unique
    
#############################################################################################

def RemoveDuplicate(DirectoryName):
  Border = "_"*70
  timestamp = time.ctime()

  LogFileName = "Marvellous%s.log"%(timestamp)
  LogFileName = LogFileName.replace(" ","_")
  LogFileName = LogFileName.replace(":","_")

  fobj = open(LogFileName,"w")

  fobj.write(Border+"\n")

  fobj.write(" MARVELLOUS AUTOMATION SCRIPT \n ")
  fobj.write(Border+"\n")

  Mydict,same,unique = FindDuplicate(DirectoryName)

  fobj.write(Border+"\n")
  fobj.write(f"same files are:{same}\n")
  fobj.write(f"Unique files are : {unique}\n")
    
  fobj.write(Border+"\n")

  result = list(filter(lambda x : len(x) > 1,Mydict.values()))

  count = 0
  TotalDeleted = 0

  for value in result:
    for subvalue in value:
      count = count + 1
      if(count > 1):
        os.remove(subvalue)
        TotalDeleted = TotalDeleted +  1
        fobj.write(f"[{timestamp}] Deleted {subvalue}\n")
    count = 0

  fobj.write(Border+"\n")
  fobj.write(f"Total deleted files {TotalDeleted}\n")    
  fobj.write(Border+"\n")     

###################################################################################
def main():
  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation script used to travel the directory")
      print("For better usage please check --u Flag")

    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("Please execute the script as ")
      print("Python Filename.py DirectoryName time interval")
      print("Directory name should be absolute path")

  elif(len(sys.argv)== 3):
     directory = sys.argv[1]
     interval = int(sys.argv[2])
     schedule.every(interval).seconds.do(RemoveDuplicate,directory)

     while True:
       schedule.run_pending()
       time.sleep(1)

  else:
    print("Invalid Number of arguments..")
    print("please use --h or --u for better information")     

      
if __name__ == "__main__":
  main()
