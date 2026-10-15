def count_vowel_and_consonant(s):
    if not s:
        return 0

    count_vowels=0
    count_consonants=0

    for char in s :
        if char.isalpha():
            if char.lower() in "aeiou":
                count_vowels+=1
            else:
                count_consonants+=1

    print("Count of vowels:", count_vowels)
    print("Count of consonants:", count_consonants)

s=input("Enter a string :")
count_vowel_and_consonant(s)

    