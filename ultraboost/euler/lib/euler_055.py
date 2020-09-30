def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

print(is_palindrome(1))
print(is_palindrome(12))
print(is_palindrome(123321))

