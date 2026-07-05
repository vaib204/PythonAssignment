even = lambda num : (num % 2 == 0)

def main():
  number = int(input("Enter number:"))

  ret = even(number)

  if(ret == True):
    print("number is even:",ret)
  else:
    print("number is odd:",ret)

if __name__ == "__main__":
  main()