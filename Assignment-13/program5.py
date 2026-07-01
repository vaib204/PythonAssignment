def Display(Marks):
  if (Marks >= 75):
    print("Distinction")
  elif(Marks >= 60):
    print("First class")
  elif(Marks >= 50):
    print("second class")
  else:
    print("Fail")     

def main():
  Mar = int(input("Enter Marks:"))

  ret = Display(Mar)

if __name__ == "__main__":
  main()