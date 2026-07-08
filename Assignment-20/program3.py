import threading

def Even(num):
    sum_even = 0
    evens = []
    for no in num:
        if no % 2 == 0:
            evens.append(no)
            sum_even += no
    print("Even Elements are:", *evens)
    print("Addition of even is:", sum_even)


def Odd(num):
    sum_odd = 0
    odds = []
    for x in num:
        if x % 2 != 0:
            odds.append(x)
            sum_odd += x
    
    print("Odd Elements are:", *odds)
    print("Addition of odd is:", sum_odd)


def main():
    number = int(input("Enter how many numbers: "))
    arr = []

    for i in range(number):
        val = int(input(f"Enter number {i+1}: "))
        arr.append(val)

    
    t_even = threading.Thread(target=Even, args=(arr,))
    t_odd = threading.Thread(target=Odd, args=(arr,))

    
    t_even.start()
    t_odd.start()

    
    t_even.join()
    t_odd.join()


if __name__ == "__main__":
    main()
