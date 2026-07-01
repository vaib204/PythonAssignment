def Area(len,wid):
 result = len * wid
 return result

def main():
 length = int(input("Enter the length:"))

 width = int(input("Enter the width:"))

 ret = Area(length,width)

 print("Area is:",ret)

if __name__ == "__main__":
 main()
