arr = [3, 7, 11, 15, 20, 25, 31, 40]
target = 11

left=0
right=len(arr)-1

count=0
while left <= right :
    mid = (left + right) // 2

    if arr[mid] == target :
        left=right+1
    elif target > arr[mid]:
        left=mid+1

    else:
        right=mid-1
    count+=1



print(count)
