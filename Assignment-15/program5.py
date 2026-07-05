from functools import reduce

Maximum = lambda sum1,max: sum1 if sum1 > max else max

def main():
 data = []

 number = int(input("Enter the numbers:"))

 for i in range(number):
   value = int(input("Enter values:"))
   data.append(value)

 data = reduce(Maximum,data)  
 print("Maximum is:",data)

 
if __name__ == "__main__":
  main()