arr = [7, 4, 9, 2, 5, 1]
k = 2
kth_elemnt=None

for i in range(len(arr) - 1 ):
    largest=i
    for j in range(i+1 , len(arr)):
        if arr[j] > arr[largest]:
            largest=j

    arr[i] , arr[largest] = arr[largest] , arr[i]

    if i == k-1 :
        kth_elemnt=arr[i]
        break

print(kth_elemnt)