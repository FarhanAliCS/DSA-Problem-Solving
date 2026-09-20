arr = [2, 4, 4, 4, 7, 9, 12]
target = 4

left=0
right=len(arr)-1
answer=-1
while left <= right:
    mid=(left+right)//2
    if arr[mid] == target :
        answer=mid
        left=mid+1

    else:
        
        right=mid-1

print(answer)