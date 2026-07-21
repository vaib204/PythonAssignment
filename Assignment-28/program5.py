def count(file,filename):
  word_count= 0
  try:
    fobj = open(file,"r")
    print("File is found")

    for i in fobj:
     count = i.split()  
    
     if filename in i:
       return True
     else:
       return False

  except FileNotFoundError as fobj:
    print("File is not present in current directory")  
 


def main():
  filename = input("Enter a file name:")

  newfile = input("Enter a word to find:")

  ret = count(filename,newfile)

  if(ret == True):
    print("Word is present")
  else:
    print("word is not present")  

if __name__ == "__main__":
  main()
