def partition(arr,low,high):
    pivot=arr[high]
    smaller=[]
    greater=[]
    pivote=[]

    for j in range(low,high+1):
        if arr[j] < pivot:
            smaller.append(arr[j])
        elif arr[j] > pivot:
            greater.append(arr[j])
        else:
            pivote.append(arr[j])

    array=smaller+pivote+greater
    return array



arr = [6, 2, 9, 3, 7]
low=0
high=len(arr)-1

print(partition(arr,low,high))