#List of numbers 
numbers=[12,34,32,12,22,11,19,0,9]

# let  Largest Number = 12
largest=numbers[0]

#Tresverse list 

for num in numbers:
    if num > largest:
        largest = num

print("Largest Number in List :",largest)

# Complexity = O(n)