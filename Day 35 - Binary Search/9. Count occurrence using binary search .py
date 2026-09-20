def first_occurrence(arr,target):
    left=0
    right=len(arr)-1
    firstoccurrence=-1
    while left <= right:
        mid=(left + right) // 2
        if arr[mid] == target:
            firstoccurrence=mid
            right=mid-1
        else:
            left=mid+1
    return firstoccurrence

def last_occurrence(arr,target):
    left=0
    right=len(arr)-1
    lastoccurrence=-1
    while left <= right:
        mid=(left + right) // 2
        if arr[mid] == target:
            lastoccurrence=mid
            left=mid+1
        else:
            right=mid-1
    return lastoccurrence

arr = [2, 4, 4, 4, 7, 9, 12]
target = 4

occurrence1=first_occurrence(arr,target)
occurrence2=last_occurrence(arr,target)
result=occurrence2-occurrence1+1
print(result)

