def checkdivisible(data):
  if(data % 3 == 0 and data % 5 == 0):
    return True
  else:
    return False
  
def main():
  num = int(input("Enter a number:"))

  ret = checkdivisible(num)

  if(ret == True):
    print(num," : It is divisible by 3 and 5")
  else:
    print(num," : It is not divisible by 3 and 5")  

if __name__ == "__main__":
  main()