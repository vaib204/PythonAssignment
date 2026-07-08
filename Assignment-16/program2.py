def ChkNum(data):
  if (data % 2 == 0):
    print(f"{data} : is Even")
  else:
    print(f"{data}: odd")  

def main():
  num = int(input("Enter a number:"))

  ret = ChkNum(num)

if __name__ == "__main__":
  main()    