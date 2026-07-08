#5 = 5 * 4* 3* 2* 1
def factorial(data):
  fact = 1
  for i in range(1,data+1):
    fact = fact * i
  return fact
  


def main():
  num = int(input("Enter a number:"))

  ret = factorial(num)

  print("factorial is:",ret)

if __name__ == "__main__":
  main()  