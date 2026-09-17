arr=[12,32,21,23,56,34,45]

smallest=float("inf")
max_difference=float("-inf")

for i in arr:
    difference=i-smallest
    if difference > max_difference:
        max_difference=difference
    if i < smallest:
        smallest=i

print(max_difference)



    





