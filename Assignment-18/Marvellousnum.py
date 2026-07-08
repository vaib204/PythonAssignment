def Prime(data):
    total = 0
    for no in data:
        if no <= 1:
            continue
        if no == 2:
            total += no
            continue
        
        is_prime = True
        for i in range(2, no):
            if no % i == 0:
                is_prime = False
                break

        if is_prime:
            total += no

    return total