def Checkvowel(str):
  if(str == "a"or str == "e" or str == "i"or str == "o"or str == "u"):
    print("it is vowel")
  else:
    print("it is not vowel")  


def main():
  char = input("Enter a charchter:")

  ret = Checkvowel(char)

if __name__ == "__main__":
  main()
