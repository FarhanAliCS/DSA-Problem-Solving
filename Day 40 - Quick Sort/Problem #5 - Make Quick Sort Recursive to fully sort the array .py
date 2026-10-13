def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    pivot=arr[-1]

    smaller=[]
    greater=[]
    pivote=[]

    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            pivote.append(i)

    return quick_sort(smaller) + quick_sort(pivote) + quick_sort(greater)

arr = [6, 2, 9, 3, 7]

print(quick_sort(arr))