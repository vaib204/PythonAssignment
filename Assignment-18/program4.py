def Frequency(data,val):
  cnt = 0
  for no in data:
    if (no == val):
      cnt = cnt + 1
  return cnt  

  
def main():
  number = int(input("Enter a number:"))
  search = int(input("Enter a number to count frequency:"))
  result = []

  for i in range(number):
    val = int(input(f"Enter Numbers{i}:"))
    result.append(val)

  print("Elements of the data",result)  
  
  ret = Frequency(result,search)  
  print(f"Frequency of {search} is:",ret)
  


if __name__ == "__main__":
  main()