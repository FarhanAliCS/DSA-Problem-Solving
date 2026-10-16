def two_unique_numbers(numbers):
    frequency={}
    unique=[]
    for num in numbers:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num] = 1

    for key , value in frequency.items():
        if len(unique) == 2 :
            break
        elif value == 1:
            unique.append(key)

    return unique
        

numbers=[1,2,3,4,1,2,3,4,5,6]
print(two_unique_numbers(numbers))