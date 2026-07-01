def square(data):
 square = data * data
 return square

def main():
  number = int(input("Enter A Number:"))

  ret = square(number)

  print("Square is :",ret)

if  __name__ == "__main__":
  main()