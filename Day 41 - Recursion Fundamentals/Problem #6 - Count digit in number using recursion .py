def count_digit(n):
    if 0 <= n <= 9:
        return 1
    
    return 1 + count_digit(n//10)
digit=int(input("Enter digit :"))
result=count_digit(digit)
print(result)