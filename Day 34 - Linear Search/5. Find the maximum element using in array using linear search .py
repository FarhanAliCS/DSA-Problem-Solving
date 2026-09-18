arr = [12, 45, 7, 89, 23, 56]
largest=float("-inf")
for i in range(len(arr)):
    if arr[i]  > largest:
        largest=arr[i]

print(largest)
    
