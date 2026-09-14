#List of numbers 
numbers=[12,34,32,12,22,11,19,5,9]

# let smallest  Number = 12
Smallest=numbers[0]

#Tresverse list 

for num in numbers:
    if num < Smallest:
        Smallest = num

print("Largest Number in List :",Smallest)

# Complexity = O(n)