def CountDigit(data):
  digit = 0
  rev = 0
  while (data != 0):
    digit = data % 10
    rev = rev * 10 + digit
    data = data // 10
   
  return rev

  
def main():
 number = int(input("Enter Number:"))

 ret = CountDigit(number)

 print("reverse digits:",ret)

if __name__ == "__main__":
  main()