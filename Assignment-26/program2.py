class Circle:
  PI = 3.14

  def __init__(self,A,B,C):
    self.Radius = A
    self.area = B
    self.cir = C

  def Accept(self,Radius):
    
    self.Radius = Radius 

  def CalculateArea(self):
    area = 0.0  

    area = self.PI * self.Radius * self.Radius

    print("Area of circle is:",area)

  def Circumference(self):
    cir = 0.0

    cir = 2 * self.PI * self.Radius

    print("Circumference of circle is:",cir)

  def Display(self):
    self.CalculateArea()
    self.Circumference()  

def main():

  radius = int(input("Enter a radius :"))
  cobj1 = Circle(0,0.0,0.0)

  cobj1.Accept(radius)  
  cobj1.Display()

if __name__ == "__main__":
  main()


    