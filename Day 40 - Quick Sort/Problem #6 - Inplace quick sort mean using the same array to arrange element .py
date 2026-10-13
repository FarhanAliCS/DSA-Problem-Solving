def partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low , high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high], arr[i+1]

    return i+1

def quick_sort(arr,low,high):
    if low < high :
        pivote_index=partition(arr,low,high)

        quick_sort(arr,low,pivote_index-1)
        quick_sort(arr,pivote_index+1,high)

    return arr

    
arr=[7,8,5,3,1,4]
low=0
high=len(arr)-1
print(quick_sort(arr,low,high))
