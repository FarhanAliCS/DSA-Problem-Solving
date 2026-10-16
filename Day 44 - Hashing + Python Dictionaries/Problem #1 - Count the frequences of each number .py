def count_frequency(num):
    frequency={}

    for i in num:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1

    return frequency
num=[2,1,4,5,1,1]
print(count_frequency(num))
