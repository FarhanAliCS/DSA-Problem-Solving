def add_digits(n):
    if 0 <= n <= 9:
        return n
    last=n%10
    return last + add_digits(n//10)

print(add_digits(1234))