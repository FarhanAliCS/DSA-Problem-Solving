arr=[0,2,0,3,0,4,5,6]
new_arr=[]
zerocount=0
for i in arr:
    if i != 0:
        new_arr.append(i)
    else:
        zerocount+=1
while zerocount !=0:
    new_arr.append(0)
    zerocount-=1


print(new_arr)