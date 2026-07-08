def prime(num):
  if(num == 2):
    return True
  
  if (num % 2 != 0 and num != 1):
    return True
  else:
    return False



def main():
  num = int(input("Enter a number:"))

  ret = prime(num)

  if(ret == True):
    print("Number is prime")
  else:
    print("Number is not prime")  


if __name__ == "__main__":
  main()  