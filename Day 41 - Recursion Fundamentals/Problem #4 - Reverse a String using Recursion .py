def reverse(string):
    if len(string) <= 1 :
        return string

    return string[-1] + reverse(string[:-1])


string=input("Enter a string :")
result=reverse(string)
print(result)