divisible = lambda num : (num % 5 == 0)

def main():
 number = int(input("Enter a number:"))

 ret = divisible(number)

 if(ret == True):
   print("Number is divisible by: 5")
 else:
     print("Number is not divisible by: 5")

if __name__ == "__main__":
  main()