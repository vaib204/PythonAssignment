import sys
def display(no):
  print(type(no))
  print(id(no))
  print(sys.getsizeof(no))

def main():
  num = int(input("Enter a number:"))
  display(num)

if __name__ == "__main__":
  main()
