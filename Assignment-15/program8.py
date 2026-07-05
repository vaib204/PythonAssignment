
divisible = lambda val: (val % 3 == 0 or val % 5 == 0)
def main():
 data = []

 number = int(input("Enter the number:"))

 for i in range(number):
    value= int(input("enter numbers:"))
    data.append(value)

 data = list(filter(divisible,data))  
 print("number is divisble by 5 and 3 :",data)

 
if __name__ == "__main__":
  main()