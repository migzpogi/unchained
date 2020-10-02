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
        if count > 50:
            return -1, -1
        if is_palindrome(p):
            return p, count
        n = p
        count += 1


# print(is_palindrome(1))
# print(is_palindrome(12))
# print(is_palindrome(123321))
#
# print(reverse_add(47))
# print(reverse_add(349))
#
# print(get_palindrome(47))
# print(get_palindrome(349))
# print(get_palindrome(196))

lychrel = []
for i in range(1, 10000):
    x = get_palindrome(i)
    if x[0] == -1:
        lychrel.append(i)

print(lychrel)
print(len(lychrel))
