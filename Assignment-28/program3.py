def count(file):
  cnt = 0
  try:
    fobj = open(file,"r")
    print("File is found")

    display = fobj.readlines()
    
    for i in display:
       print(i)

  except FileNotFoundError as fobj:
    print("File is not present in current directory")  


def main():
  filename = input("Enter a file name:")

  count(filename)

  


if __name__ == "__main__":
  main()
