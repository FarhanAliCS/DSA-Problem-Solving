def num_frequency(numbers):
    frequency={}

    for num in numbers:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1

    for key , value in frequency.items():
        if value == 1:
            return value

numbers=[2,3,4,2,3,4,5]
print(num_frequency(numbers))
