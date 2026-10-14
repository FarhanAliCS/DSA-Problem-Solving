def cal_power(a,b):
    if b == 0:
        return 1

    return a * cal_power(a,b - 1)

print(cal_power(2,3))