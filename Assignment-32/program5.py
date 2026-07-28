import schedule
import os
import time


def DeleteFiles(Directory):
  Ret = os.path.exists(Directory)
  if(Ret == False):
    print("Marvellous Automation Errror : There is no such directory with name",Directory)
    return
  
  Ret = os.path.isdir(Directory)

  if(Ret == False):
    print("Marvellous Automation Errror : It is not a directory with name",Directory)
    return
  
  timestamp = time.ctime()
  LogFileName = "Marvellous%s.log"%(timestamp)
  LogFileName = LogFileName.replace(" ","_")
  LogFileName = LogFileName.replace(":","_")

  fobj = open(LogFileName,"w")

  
  for FolderName,Subfolder,filename in os.walk(Directory):
    for fname in filename:
      fname = os.path.join(FolderName,fname)

      if (os.path.getsize(fname) == 0):
        fobj.write(f"empty files are:{fname} in bytes\n")
    
      if(os.path.getsize(fname) == 0):
        os.remove(fname)
        fobj.write(f"deleted files are : {fname}")
        print("Files deleted succesfully...")
        

  fobj.close()      


def main():
  foldername = input("Enter folder name:")

  schedule.every(10).seconds.do(DeleteFiles,foldername)

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
  main()    