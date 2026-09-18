arr = [2, 5, 2, 8, 2, 9, 5, 2]
target = 2
count=0

for i in arr:
    if i == target:
        count+=1
print(f"Number of occurence of {target}  is : {count}")