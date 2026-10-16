def duplicate(numbers):
    frequency={}
    duplicates=[]

    for num in numbers:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1

    for key , value in frequency.items():
        if value > 1 :
               duplicates.append(key)

    return duplicates

numbers=[2,3,4,5,2,3,1]
print(duplicate(numbers))

    