def cube(data):
 cube = data * data * data
 return cube

def main():
  number = int(input("Enter A Number:"))

  ret = cube(number)

  print("cube is :",ret)

if  __name__ == "__main__":
  main()