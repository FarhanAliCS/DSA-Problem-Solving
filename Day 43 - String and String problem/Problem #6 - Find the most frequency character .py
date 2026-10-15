def most_frequency_char(s):
    if not s:
        return 
    frequency={}
    for char in s:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1

    highest_char=""
    highest=-1

    for key,value in frequency.items():
        if value > highest:
            highest=value
            highest_char=key
    
    return highest_char

string=input("Enter string :")
print(most_frequency_char(string))