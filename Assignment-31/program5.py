import schedule
import time
import os

def CheckDirectory(name):
 totalfile = 0
 timestamp = time.ctime()
 
 log = "Marvellous%s.txt"%(timestamp)

 log = log.replace(" ","_")
 log = log.replace(":","_")

 fobj = open(log,"w")

 for FolderName,SubFolder,FileName in os.walk(name):
   for f in FileName: 
     totalfile = totalfile + len(FileName)
     fobj.write("files:"+f+"\n")
 fobj.write(f"numbers of files:{totalfile}\n")
 fobj.write(f"{timestamp}")

 print("infoemation gets stored succesfully...")
   

def main():

  Dirname = input("Enter a directory name:")
  
  schedule.every(5).seconds.do(CheckDirectory,Dirname)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()