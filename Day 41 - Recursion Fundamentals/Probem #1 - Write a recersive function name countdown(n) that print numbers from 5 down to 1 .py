def coutdown(n):
    if n == 0 :
        print("Down")
        return
    print(n)
    return coutdown(n - 1)

n=int(input("Enter number to start countdown :"))
coutdown(n)