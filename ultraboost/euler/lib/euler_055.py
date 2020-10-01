def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def reverse_add(n):
    reversed = int(str(n)[::-1])
    return n + reversed


def get_palindrome(n):
    count = 1
    while True:
        p = reverse_add(n)
        if is_palindrome(p):
            return p, count
        n = p
        count += 1


print(is_palindrome(1))
print(is_palindrome(12))
print(is_palindrome(123321))

print(reverse_add(47))
print(reverse_add(349))

print(get_palindrome(47))
print(get_palindrome(349))
