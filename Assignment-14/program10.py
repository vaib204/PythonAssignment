Add = lambda no1, no2, no3: no1 if (no1 >= no2 and no1 >= no3) else (no2 if no2 >= no3 else no3)

def main():
    num1 = int(input("Enter 1 number: "))
    num2 = int(input("Enter 2 number: "))
    num3 = int(input("Enter 3 number: "))

    ret = Add(num1, num2, num3)
    print("Maximum is:", ret)

if __name__ == "__main__":
    main()
