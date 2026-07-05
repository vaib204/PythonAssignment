odd = lambda no:(no % 2  != 0)

def main():
 data = []

 number = int(input("Enter the numbers:"))

 for i in range(number):
   value = int(input("Enter values:"))
   data.append(value)

 data = list(filter(odd,data))   

 print("odd numbers are:",data)

if __name__ == "__main__":
  main()