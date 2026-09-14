arr = [2, 7, 11, 15, 3, 6, 2 , 8 , 1]
target = 9
seen={}
pairs=[]
for number in arr:
    needed=target-number
    if needed in seen:
        pairs.append((needed,number))
    seen[number]=True

print(pairs)

