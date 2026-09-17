arr=[100, 4, 200, 1, 3, 2]
numbers=set(arr)
print(numbers)
longest=0
for number in numbers:
    if number-1 not in numbers:
        current=number
        count=1
        while current+1 in numbers:
            current+=1
            count+=1

        if count > longest:
           longest=count

print(longest)