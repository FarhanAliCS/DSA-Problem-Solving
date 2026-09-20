arr = [3, 7, 11, 15, 20, 25, 31, 40]
target = 43

left=0
right=len(arr)-1
found=False
while left <= right:
    mid=(left+right)//2
    if arr[mid] == target:
        found=True
        left=right+1
    elif target > arr[mid]:
        left=mid+1
    else:
        right=mid-1

if not found:
    print("Target not found .")
else:
    print("Target found on index :",mid)