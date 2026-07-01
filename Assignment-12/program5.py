def factors(data):
  for i in range(data,0,-1):
      print(i)
   
def main():
  number = int(input("Enter a number:"))

  ret = factors(number)

if __name__ == "__main__":
  main()