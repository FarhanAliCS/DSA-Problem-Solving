arr = [5,2,4,1,3]
comparison=0
for i in range(1 , len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 :
        comparison+=1
        if  arr[j] <= key:
            break
        arr[j+1] = arr[j]
        j-=1

    arr[j+1]=key

print(*arr)
print("No of comparison :",comparison)