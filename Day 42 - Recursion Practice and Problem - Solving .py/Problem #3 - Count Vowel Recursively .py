def count_vowel(s):
    if len(s) == 0:
        return 0
    if s[0].lower() in "aeiou":
        count=1
    else:
        count=0

    return count + count_vowel(s[1:])

print(count_vowel("Farhan Ali"))