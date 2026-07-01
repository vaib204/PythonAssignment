def Display(data):
  isum = 0
  for i in range(1,data+1):
    isum = isum + i
  return isum


def main():
 no = int(input("Enter a number:"))

 ret = Display(no)

 print("Addition is :",ret)

if __name__ == "__main__":
  main()