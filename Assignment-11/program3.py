def CountDigit(data):
  digit = 0
  sum = 0
  while (data != 0):
    digit = data % 10
    data = data // 10
    sum = sum + digit
  return sum

  
def main():
 number = int(input("Enter Number:"))

 ret = CountDigit(number)

 print("sum of digits is:",ret)

if __name__ == "__main__":
  main()