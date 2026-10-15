def is_palindrome(s):
    if not s :
        return None
    reverse=""
    for char in s:
        reverse = char +reverse

    if reverse == s:
        return "Palindrome"
    else:
        return "Not Palindrome"


s=input("Enter string :")
print(is_palindrome(s))