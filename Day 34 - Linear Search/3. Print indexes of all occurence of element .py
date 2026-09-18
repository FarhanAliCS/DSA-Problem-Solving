arr = [5, 3, 7, 3, 9, 3, 2]
target = 3
occurrence=[]

for i in range(len(arr)):
    if arr[i] == target:
        occurrence.append(i)

print(occurrence)
        

