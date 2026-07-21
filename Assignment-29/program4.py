import sys

def main():
    if len(sys.argv) != 3:
       print("You have to enter like program3.py file_name1 file_name2")
       return
      
    try:
      filename1 = sys.argv[1]
      filename2 = sys.argv[2]

      fobj = open(filename1,"r")
      
      cobj = open(filename2,"r")
  
      
      if(fobj.readlines() == cobj.readlines()):
         print("success")
      else:
         print("Failure")   
      
      fobj.close()
      cobj.close() 
    
    except FileNotFoundError as fobj:
       print(fobj)

if __name__  == "__main__":
  main()  