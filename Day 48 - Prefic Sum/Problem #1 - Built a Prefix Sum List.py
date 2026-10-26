def built_prefix_sum(numbers):
    prefix=[]
    total=0

    for num in numbers:
       total+=num
       prefix.append(total)

    return prefix

numbers=[3,1,4,2]
print(built_prefix_sum(numbers))
