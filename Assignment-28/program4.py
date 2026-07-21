import copy

def count(file,newfile):
  cnt = 0
  try:
    fobj = open(file,"r")
    rs = fobj.read()
    print("File is found")

    cobj = open(newfile,"w")
    print("file is found")

    cobj.write(rs)

    print(f"contents of {file} is copied into {newfile} ")

  except FileNotFoundError as fobj:
    print("File is not present in current directory")  


def main():
  filename = input("Enter a file name:")

  newfile = input(f"Enter a new file name to copy the {filename} file data:")

  count(filename,newfile)


if __name__ == "__main__":
  main()
