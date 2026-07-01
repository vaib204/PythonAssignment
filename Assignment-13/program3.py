def perfect(num):
 sum = 0
 for i in range(1,num+1,1):
   if (i % num == 0):
    sum = sum + num
   
 return sum == num


def main():
 number = int(input("Enter The Number:"))

 ret = perfect(number)

 if(ret == True):
   print("number is perfect")
 else:
   print("number is not perfect")  

if __name__ == "__main__":
  main()