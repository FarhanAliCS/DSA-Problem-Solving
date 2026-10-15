def find_anagrams(s1,s2):
    if len(s1) != len(s2):
        return "Not Anagrams"

    frequency_s1={}
    frequency_s2={}
    for char in s1:
        if char in frequency_s1:
            frequency_s1[char]+=1
        else:
            frequency_s1[char]=1
            
    for char in s2:
        if char in frequency_s2:
            frequency_s2[char]+=1
        else:
            frequency_s2[char]=1

    if frequency_s1 == frequency_s2:
        return "Anagrams"
    else:
        return "Not Anagram"


s1= input("Enter string s1 :")
s2= input("Enter string s2 :")
print(find_anagrams(s1,s2))