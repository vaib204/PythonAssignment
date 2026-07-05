square = lambda no:(no * no)

def main():
 data = []

 number = int(input("Enter the numbers:"))

 for i in range(number):
   value = int(input("Enter values:"))
   data.append(value)

 data = list(map(square,data))   

 print("square of numbers are:",data)

if __name__ == "__main__":
  main()
