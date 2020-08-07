def is_palindrome(n):
    num_str = str(n)
    reversed_num = num_str[::-1]
    if num_str == reversed_num:
        return True
    else:
        return False


pal_list = []
bin_list = []
for i in range(1, 1000000):
    base_2 = "{0:b}".format(i)
    if is_palindrome(i) and is_palindrome(base_2):
        pal_list.append(i)
        bin_list.append(base_2)

print(sum(pal_list))