def count_digit(digit, n):
    if n <= 9:
        return 1 if n == digit else 0

    return (n % 10 == digit) + count_digit(digit, n // 10)


result = count_digit(2, 12232)
print(result)