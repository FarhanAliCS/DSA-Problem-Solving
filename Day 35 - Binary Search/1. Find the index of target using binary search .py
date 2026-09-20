arr = [2, 5, 8, 12, 16, 23, 38]
target = 16

left=0
right=len(arr)-1
for i in range(len(arr)):
    mid=(left+right)//2
    if arr[mid] == target:
        print(mid)
        break
    elif target > arr[mid]:
        left=mid+1
    else:
        right=mid-1    


    





