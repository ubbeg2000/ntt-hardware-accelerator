def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


i = 1

while True:
    if (is_prime(i+1)):
        print(i+1)

    i = i << 1

    # if i > (1 << 30) + 100:
    #     break
