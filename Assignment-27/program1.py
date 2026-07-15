class Bookstore:
  NoofBooks = 0

  def __init__(self,A,B):
    Bookstore.NoofBooks+=1
    self.BookName = A
    self.Author= B

  def Display(self):
    print(f"{self.BookName}By{self.Author}No  of Books:{self.NoofBooks}")
   

def main():
  BookName = input("Enter a bookname:")
  Author = input("Enter a Author name:")

  obj1 = Bookstore(BookName,Author)
  obj1.Display()

  BookName = input("Enter a bookname:")
  Author = input("Enter a Author name:")

  obj2 = Bookstore(BookName,Author)
  obj2.Display()

if __name__ == "__main__":
  main()

    
