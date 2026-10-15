def reverse_str(str):
    if not str:
        return None
    reverse=""
    for char in str:
        reverse=char+reverse

    return reverse

string=input("Enter str :")
print(reverse_str(string))

