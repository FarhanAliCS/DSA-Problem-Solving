arr = [2, 2, 1, 1, 1, 2, 2]
frequency={}

for number in arr:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
length=len(arr)//2

for key , value in frequency.items():
    if value > length:
        print(key)
        break
        




    
