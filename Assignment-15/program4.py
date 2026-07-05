from functools import reduce

addition = lambda sum1,sum2 : (sum1 + sum2)

def main():
 data = []

 number = int(input("Enter the numbers:"))

 for i in range(number):
   value = int(input("Enter values:"))
   data.append(value)

 data = reduce(addition,data)  

 print("Addition is:",data)

if __name__ == "__main__":
  main()