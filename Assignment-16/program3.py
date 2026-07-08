def Add(data1,data2):
  sum = 0
  sum = data1 + data2
  return sum

def main():
  num1 = int(input("Enter a number:"))

  num2 = int(input("Enter a number:"))

  ret = Add(num1,num2)

  print("Addition is :",ret)

if __name__ == "__main__":
  main()    