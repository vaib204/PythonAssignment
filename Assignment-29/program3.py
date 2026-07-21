import sys

def main():
    if len(sys.argv)!= 1:
       print("You have to enter like program3.py file_name")
       return
    
    try:
      filename = sys.argv[1]

      fobj = open(filename,"r")
      rs = fobj.read()

      cobj = open("demo.txt","w")
      cobj.write(rs)

      print("File copied succesfully..")

      fobj.close()
      cobj.close() 
    
    except FileNotFoundError as fobj:
       print(fobj)

if __name__  == "__main__":
  main()  