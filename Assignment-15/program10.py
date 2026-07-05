even = lambda no: no % 2 == 0   

def main():
    data = []
    cnt = 0
    number = int(input("Enter the numbers: "))

    for i in range(number):
        value = int(input("Enter values: "))
        data.append(value)

   
    evens = list(filter(even, data))

    for i in evens:
     cnt+=1

    print("Even numbers count is:", cnt)

if __name__ == "__main__":
    main()
