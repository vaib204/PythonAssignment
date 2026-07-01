def Palindrome(data):
  start = data
  digit = 0
  rev = 0
  while (data != 0):
    digit = data % 10
    rev = rev * 10 + digit
    data = data // 10
  
  return start == rev
  
def main():
 number = int(input("Enter Number:"))

 ret = Palindrome(number)

 if Palindrome(number):
  print(number,":is palindrome")
 else:
   print(number,":not palindrome") 


if __name__ == "__main__":
  main()