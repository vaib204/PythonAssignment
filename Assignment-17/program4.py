 # 12 = 1 2 3 4 6
def facotrs(num):
  sum = 0
  for i in range(1,num):
    if num % i == 0:
      sum = sum + i
  print("Addition is :",sum)



def main():
  num = int(input("Enter a number:"))

  facotrs(num)

if __name__ == "__main__":
  main()  