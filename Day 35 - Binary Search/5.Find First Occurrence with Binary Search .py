def binary_search(arr,target):
    left=0
    right=len(arr)-1
    first_occurence=-1

    while left <= right :
        mid = (left + right) // 2

        if arr[mid] == target :
            first_occurence=mid
            right=mid-1      
        else:
            left=mid+1
            
    return first_occurence

       
arr = [2, 4, 4, 4, 7, 9, 12]
target = 4
result=binary_search(arr,target)
print(f"{target} Found on index : {result}")
