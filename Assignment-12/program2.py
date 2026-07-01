def factors(data):
  for i in range(1,data+1):
    if ((data % i )== 0):
      print("factors are:",i)

def main():
  number = int(input("Enter a number:"))

  ret = factors(number)

if __name__ == "__main__":
  main()