def ChkNum(data):
 if (data >= 1):
   print("Number is positive")
 elif(data < 0):
   print("Number is negative") 
 else:
   print("Number is zero")   

def main():
  num = int(input("Enter a number:"))

  ret = ChkNum(num)

if __name__ == "__main__":
  main()    