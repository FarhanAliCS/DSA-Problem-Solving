arr=[5,3,8,1,2]

smallest=0
for i in range(len(arr)):
    if arr[i] < arr[smallest]:
        smallest=i
arr[0] , arr[smallest] = arr[smallest] , arr[0]

print(arr)
