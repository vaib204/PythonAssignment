
length = lambda val: len(val) > 5
def main():
 data = []

 number = int(input("Enter the String:"))

 for i in range(number):
    value= input("enter list:")
    data.append(value)

 data = list(filter(length,data))  
 print("list of string with length greter than 5 :",data)

 
if __name__ == "__main__":
  main()