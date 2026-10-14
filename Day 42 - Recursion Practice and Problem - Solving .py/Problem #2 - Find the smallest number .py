def smallest_digit(num):
    if 0 <= num <= 9:
        return num
    smallest=num % 10
    digit=smallest_digit(num // 10)

    if digit < smallest:
        smallest=digit

    return smallest

print(smallest_digit(12345))