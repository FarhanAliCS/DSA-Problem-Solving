arr=[16,17,4,3,5,2]
leaders=[]
largest=float("-inf")
for i in range(len(arr)-1,-1,-1):
    if arr[i] > largest:
        largest=arr[i]
        leaders.append(largest)

reverse=leaders[-1::-1]
print(reverse)
