from functools import reduce

Minimum= lambda sum1,min : sum1 if sum1 < min else min

def main():
 data = []

 number = int(input("Enter the numbers:"))

 for i in range(number):
   value = int(input("Enter values:"))
   data.append(value)

 data = reduce(Minimum,data)  
 print("Maximum is:",data)

 
if __name__ == "__main__":
  main()