def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    sort=[]
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sort.append(left[i])
            i+=1
        else:
            sort.append(right[j])
            j+=1

    while i < len(left):
        sort.append(left[i])
        i+=1

    while j< len(right):
        sort.append(right[j])
        j+=1

    return sort

arr=[8,3,5,1,9,2]
print(merge_sort(arr))

