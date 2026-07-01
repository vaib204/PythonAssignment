def prime(data):
 if data <= 0:
  data = -data

 cnt = 2
 if(data == 2):
  return True
 
 if( data % cnt == 0 ):
  return False
 else:
  return True


def main():
 num = int(input("Enter a number:"))

 ret = prime(num)

 if(ret == True):
  print(ret,":is prime")
 else:
  print(ret,": is not prime number") 

if  __name__ == "__main__":
 main()
