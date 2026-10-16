def most_frequent(numbers):
    frequency={}
    largest=-1
    number=0
    for num in numbers:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1

    for key , value in frequency.items():
        if value > largest:
            largest=value
            number=key

    return number

numbers=[2,2,2,3,4,5,6,7,5,5,7,7,3]
print(most_frequent(numbers))

    