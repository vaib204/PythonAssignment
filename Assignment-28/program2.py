def count(file):
  word_count= 0
  try:
    fobj = open(file,"r")
    print("File is found")

    for i in fobj:
     count = i.split()  
    
     word_count = word_count + len(count)

    return word_count

  except FileNotFoundError as fobj:
    print("File is not present in current directory")  
 


def main():
  filename = input("Enter a file name:")

  ret = count(filename)

  print("Total words in file is:",ret)


if __name__ == "__main__":
  main()
