arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum=0
maximum_sum=float("-inf")

for number in arr:
    current_sum=max(current_sum + number , number)
    if current_sum > maximum_sum:
        maximum_sum=current_sum

print(maximum_sum)



