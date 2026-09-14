numbers=[12,34,56,78,76,33,11,21,51,53]

even_count=0
odd_count=0

for num in numbers:
    if num % 2 ==0 :
        even_count+=1
    else:
       odd_count+=1

print("Total Even Numbers :",even_count)
print("Total Odd numbers :",odd_count) 

# Complexity = O(n)