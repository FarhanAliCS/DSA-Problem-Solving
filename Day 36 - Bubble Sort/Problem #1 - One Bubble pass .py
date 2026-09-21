arr=[5,2,8,1,3]
 
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]

    print(arr)
