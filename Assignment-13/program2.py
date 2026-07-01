def Area(red):
 radius = 3.14*red*red
 return radius

def main():
 radius = int(input("Enter the radius of circle:"))

 ret =   Area(radius)

 print("Area of circle is:",ret)


if __name__ == "__main__":
 main()