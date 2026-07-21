import os

def main():
  FileName = input("Enter a File name :")

  ret = os.path.exists(FileName)

  if(ret == True):
    print("File is present in current directory")
  else:
    print("File is not present in current directory")

if __name__ == "__main__":
  main()
