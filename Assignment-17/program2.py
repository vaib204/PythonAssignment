def Display(data):
  for i in range(data):
    print(" * " * data)
    

def main():
  num = int(input("Enter a number:"))

  Display(num)

if __name__ == "__main__":
  main()