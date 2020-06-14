"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
906609
"""


def is_num_palindrome(n):
    str_n = str(n)
    if str_n == str_n[::-1]:
        return True
    else:
        return False

valid_nums = range(100, 1000)
products = []
for x in reversed(valid_nums):
    for y in reversed(valid_nums):
        z = x*y
        if is_num_palindrome(z):
            products.append(z)

print(max(products))