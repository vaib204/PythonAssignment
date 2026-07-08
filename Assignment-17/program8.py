def Display(data):
  for i in range(1,data+1):
      for j in range(1,i+1):
            print(j,end= " ")
      print()    
    

def main():
  num = int(input("Enter a number:"))

  Display(num)

if __name__ == "__main__":
  main()

   