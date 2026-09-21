arr = [4, 2, 4, 3, 2, 4, 1, 3, 1]
frequency={}

for num in arr:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
print(frequency)

for i in range(len(arr)-1):
    largest=i
    for j in range(i+1, len(arr)):
        if frequency[arr[j]] > frequency[arr[largest]]:
            largest=j
        elif frequency[arr[j]] == frequency[arr[largest]]:
            if arr[j] < arr[largest]:
                largest=j
            
    arr[i], arr[largest] = arr[largest] , arr[i]

print(arr)
        
    