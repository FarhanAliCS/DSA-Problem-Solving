def reverse_num(n,reversed_num=0):
    if n == 0:
        return reversed_num
    return reverse_num(n//10,reversed_num=reversed_num*10+n%10)
    

    
print(reverse_num(1231))