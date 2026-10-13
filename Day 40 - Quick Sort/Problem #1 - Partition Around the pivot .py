def partition(arr,low,high):
    pivot=4
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

    return smaller,pivote ,greater



arr=[7,2,9,4,3,8,1]
low=0
high=len(arr)-1

print(partition(arr,low,high))