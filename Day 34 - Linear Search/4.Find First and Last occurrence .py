arr = [5, 3, 7, 3, 9, 3, 2]
target = 3
first_occurrence=-1
last_occurrence=-1

for i in range(len(arr)):
     if arr[i] == target:
          if first_occurrence==-1:
               first_occurrence=i
          last_occurrence=i

print(first_occurrence)
print(last_occurrence)