from functools import reduce

product = lambda data,product : (data * product)

def main():
 
 data = []

 number = int(input("Enter the numbers:"))

 for i in range(number):
   value = int(input("Enter values:"))
   data.append(value)

 data = reduce(product,data)  
 print("product  is:",data)

 
if __name__ == "__main__":
  main()