def Min(data):
  min = data[0]
  for i in data:
    if(i < min):
     min = i
  return min

def main():
  number = int(input("Enter a number:"))
  result = []

  for i in range(number):
    val = int(input("Enter Numbers:"))
    result.append(val)

  print("Elements of the data",result)  
  
  ret = Min(result)  
  print("Minimum Element is:",ret)
  


if __name__ == "__main__":
  main()