#Palindrome Check

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False
