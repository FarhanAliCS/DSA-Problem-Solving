def remove_duplicate(s):
    new_str=""
    for char in s:
        if char not in new_str:
            new_str+=char

    return new_str


string=input("Enter string :")
print(remove_duplicate(string))