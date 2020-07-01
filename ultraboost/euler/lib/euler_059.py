import itertools

def decrypt(text, key):
    """
    Performs XOR on each character of the text to each character of the key (cycled)
        text = [100, 101, 102, 103, 104]
        key = [97, 98, 99]
        100^97, 101^98, 102^99, 103^97, 104^98
    :param [int] text: encrypted text in ascii list
    :param [int] key: three character lower case keys
    :return:
    """
    decrypted_text_in_ascii_list = []

    paired = list(zip(text, itertools.cycle(key)))
    for p in paired:
        if 32 <= p[0]^p[1] <= 122:
            decrypted_text_in_ascii_list.append(p[0]^p[1])
        else:
            return []

    return decrypted_text_in_ascii_list


def pretty_print_ascii_list(ascii_list):
    pretty_string = ""
    for a in ascii_list:
        pretty_string += chr(a)

    return pretty_string


three_char_lower_case_keys = []
for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            three_char_lower_case_keys.append([i, j, k])

with open('p059_cipher.txt', 'r') as f:
    for lines in f.readlines():
        encrypted_text_in_ascii_list = list(map(int, lines.strip().split(',')))

for k in three_char_lower_case_keys:
    decrypted_text_in_ascii_list = decrypt(encrypted_text_in_ascii_list, k)
    if decrypted_text_in_ascii_list:
        print(k, sum(decrypted_text_in_ascii_list), pretty_print_ascii_list(decrypted_text_in_ascii_list))