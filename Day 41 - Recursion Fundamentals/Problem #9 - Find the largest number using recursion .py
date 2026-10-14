def largest_num(n):
    if 0 <= n <= 9:
        return n
    num=n%10
    if largest_num(n//10) > num:
        num=largest_num(n//10)
    return num

print(largest_num(1290))