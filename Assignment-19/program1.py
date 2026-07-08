square = lambda no : no ** 2

def main():
  number = int(input("Enter a number:"))

  iret =  square(number)

  print(f"power of {number} is:",iret)

if __name__ == "__main__":
  main()
