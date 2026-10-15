def  count_frequency(s):
    frequency={}
    for char in s:
        if char  in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency
string=input("Enter string :")
print(count_frequency(string))

    