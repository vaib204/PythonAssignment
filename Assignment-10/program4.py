def evenodd(data):
  for i in range(1,data + 1):
    if (i % 2 == 0):
      print("Even numbers are:",i)


def main():
  num = int(input("Enter a number:"))

  ret = evenodd(num)

if __name__ == "__main__":
  main()