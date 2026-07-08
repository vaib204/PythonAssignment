def Count(num):
  Sum = 0
  digit = 0
  while num != 0:
    digit = num % 10
    Sum = Sum + digit
    num = num // 10
  return Sum 


def main():
  num = int(input("Enter a number:"))

  ret = Count(num)

  print("Total Addition is :",ret)

if __name__ == "__main__":
  main()