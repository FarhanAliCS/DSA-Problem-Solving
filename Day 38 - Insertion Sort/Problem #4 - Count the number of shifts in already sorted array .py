arr = [1, 2, 3, 4, 5]
shifts=0
for i in range(1 , len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        shifts+=1
        j-=1

    arr[j+1]=key

print(*arr)
print("No of shifts :",shifts)