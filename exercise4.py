def is_palindrome(str1):
    str2 = str1.replace(' ','')
    return str2 == str2[::-1]


print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('han nah')) # True
print(is_palindrome('rob ert')) # False
print(is_palindrome('amanaplanac analpanama'))