arr=[12,43,32,12,12,45,43,32]
new_arr=[]
catch=arr[0]
for i in arr:
    if i not in new_arr:
        new_arr.append(i)


print(new_arr)    
    