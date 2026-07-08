def Display(data):
  for i in range(data,0,-1):
      for j in range(i):
            print("*",end= " ")
      print()    
    

def main():
  num = int(input("Enter a number:"))

  Display(num)

if __name__ == "__main__":
  main()

   