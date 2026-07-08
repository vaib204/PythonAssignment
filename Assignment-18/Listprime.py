from Marvellousnum import Prime

def main():
    number = int(input("Enter how many numbers: "))
    result = []

    for i in range(number):
        val = int(input("Enter number: "))
        result.append(val)

    print("Elements of the data:", result)  

    ret = Prime(result)  
    print("Addition of prime numbers is:", ret)


if __name__ == "__main__":
    main()
