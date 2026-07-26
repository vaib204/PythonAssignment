import schedule
import time
import os
import datetime

def CheckDirectory():
 timestamp = time.ctime()
 totalfile = 0
 totalsubfolder = 0 
 for FolderName,SubFolder,FileName in os.walk("Ganesh"):
   totalfile = totalfile + len(FileName)
   totalsubfolder = totalsubfolder + len(SubFolder)

 print("Folder name is:",os.path.abspath("Ganesh"))
 print("Total files are:",totalfile)
 print("Total subfolders are:",totalsubfolder)
 print("scan time is:",timestamp)

   
def main():
  
  schedule.every(5).seconds.do(CheckDirectory)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()