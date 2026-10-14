def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])


string=input("Enter a string to find palindrome or not :")
print(is_palindrome(string))