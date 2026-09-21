arr=[1,4,5,3,1,2]

swap=0
for i in range(len(arr)):
    swapped=False
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
            swap+=1
    if not swapped:
        break
print(swap)