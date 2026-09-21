arr=[12,34,32,12,22,11]
count=0
for i in range(len(arr)-1):
    smallest=i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[smallest]:
            smallest=j
    if smallest != i:
       arr[i] , arr[smallest] = arr[smallest] , arr[i]
       count+=1
    
print(count)
print(arr)