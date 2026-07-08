def Max(data):
  max = 0
  for i in data:
    if(i > max):
     max = i
  return max 

def main():
  number = int(input("Enter a number:"))
  result = []

  for i in range(number):
    val = int(input("Enter Numbers:"))
    result.append(val)

  print("Elements of the data",result)  

  ret = Max(result)  
  print("Maximum Element is:",ret)
  


if __name__ == "__main__":
  main()