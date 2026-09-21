arr=[5,3,8,1,2]

smallest=0

for i in range(len(arr)):
    if arr[i] < arr[smallest]:
        smallest=i

print(smallest)