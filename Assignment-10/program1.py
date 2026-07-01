def table(data):
  for i in range(1,11):
    result = i * data
    print(result)
   

def main():
  num = int(input("Enter the number:"))

  table(num)

  
  
if __name__ == "__main__":
  main()
