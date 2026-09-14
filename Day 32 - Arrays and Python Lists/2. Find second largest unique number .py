arr=[12,32,12,34,45,12,45,12]
largest=float("-inf")
second_largest=float("-inf")
for i in arr:
    if i > largest:
        second_largest=largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest=i

print(second_largest)

