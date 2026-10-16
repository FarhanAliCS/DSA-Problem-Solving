def first_non_repeat_num(num):
    frequency={}

    for i in num:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1

    for i in num:
        if frequency[i] == 1:
            return i

    

num=[4,5,1,2,1,4,5]
print(first_non_repeat_num(num))