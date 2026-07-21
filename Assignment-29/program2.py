def main():
  filename = input("Enter a file name:")
  try:
    fobj = open(filename,"r",encoding = "utf-8")

    print(fobj.read())

  except:
    print("File is not present in current directory")  


if __name__  == "__main__":
  main()  