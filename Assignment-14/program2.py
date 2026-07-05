cube = lambda no : (no * no * no)

def main():
  number = int(input("Enter a number:"))

  ret = cube(number)

  print("cube is :",ret)

if __name__ == "__main__":
  main()