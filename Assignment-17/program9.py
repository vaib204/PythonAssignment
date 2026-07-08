def Count(num):
  cnt = 0
  digit = 0
  while num != 0:
    digit = num % 10
    cnt = cnt + 1
    num = num // 10
  return cnt  


def main():
  num = int(input("Enter a number:"))

  ret = Count(num)

  print("Total count is :",ret)

if __name__ == "__main__":
  main()