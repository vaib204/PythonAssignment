def count(file):
  cnt = 0
  try:
    fobj = open(file,"r")
    print("File is found")

    count = fobj.readlines()

    for i in range(len(count)):
      cnt = cnt + i
      
    return cnt

  except FileNotFoundError as fobj:
    print("File is not present in current directory")  


def main():
  filename = input("Enter a file name:")

  ret = count(filename)

  print("Total lines in file is:",ret)


if __name__ == "__main__":
  main()
