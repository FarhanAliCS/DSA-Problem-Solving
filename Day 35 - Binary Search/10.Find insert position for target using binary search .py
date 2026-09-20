arr = [2, 5, 8, 12, 16, 21]
target = 15

left=0
right=len(arr)-1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] < target:
        left=mid+1
    else:
        right=mid-1

print(left)