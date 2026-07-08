def ChkNum(data):
  if (data % 5 == 0):
    print(f"{data} : is divisible by 5")
  else:
    print(f"{data}: is not divisible by 5")  

def main():
  num = int(input("Enter a number:"))

  ret = ChkNum(num)

if __name__ == "__main__":
  main()    