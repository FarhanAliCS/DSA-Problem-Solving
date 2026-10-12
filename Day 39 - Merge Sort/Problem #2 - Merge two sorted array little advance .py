left=[1,4,7,9]
right=[2,3,8,10,12]

i=0
j=0
sort=[]

while i < len(left) and j < len(right):
    if left[i] < right[j]:
        sort.append(left[i])
        i+=1

    else:
        sort.append(right[j])
        j+=1

while i < len(left):
    sort.append(left[i])
    i+=1

while j < len(right):
    sort.append(right[j])
    j+=1

print(sort)