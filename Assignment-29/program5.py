def main():
 word_count = 0
 filename = input("Enter a file name:\n")
 Name = input("Enter a string:\n")

 try:
    fobj = open(filename,"r")
   
    rs = fobj.read()

    print(rs)

    hs = rs.split()
  
    for w in hs:
      if w == Name:
        word_count = word_count + 1

    print(f"word count is: {word_count}")    

 except:
    print("File is not present in current directory")  

   
if __name__ == "__main__":
  main()