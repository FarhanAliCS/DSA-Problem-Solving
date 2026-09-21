arr=[5,3,8,1,2]

smallest=0

for i in range(len(arr)-1):
    smallest=i

    for j in range(i+1,len(arr)):
        if arr[j] < arr[smallest] :
            smallest=j

    arr[i] , arr[smallest] = arr[smallest] , arr[i]

print(arr)