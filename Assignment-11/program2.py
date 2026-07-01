def CountDigit(data):
  digit = 0
  count = 0
  while (data != 0):
    digit = data % 10
    data = data // 10
    count = count+1
  return count

  
def main():
 number = int(input("Enter Number:"))

 ret = CountDigit(number)

 print("count of digits are:",ret)

if __name__ == "__main__":
  main()