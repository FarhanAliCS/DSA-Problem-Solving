arr=[10,3,7,15,2,12]
target=8

for i in range(len(arr)-1):
    smallest=i
    for j in range(i+1 , len(arr)):
        if abs(arr[j] - target) < abs(arr[smallest] - target):
            smallest=j

    arr[i] , arr[smallest] = arr[smallest] , arr[i]

print(arr)
    