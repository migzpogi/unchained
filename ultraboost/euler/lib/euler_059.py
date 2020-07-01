import itertools

def get_ascii(c):
    return ord(c)


def get_char(n):
    return chr(n)


def convert(x):
    converted = []
    for i in x:
        converted.append(i[0]^i[1])

    return converted

# print(get_ascii('a'))
# print(get_char(97))
# print(65^42)
# print(107^42)
#
# key = [97, 97, 97]
# orig = [36,22,80,0,0,4,23,25,19,17,88,4,4,19,21,11,88,22,23,23,29,69]
# encrypted = [9, 7, 15, 13, 13]
# pairs = list(zip(orig, itertools.cycle(key)))
# print(convert(pairs))
# pairs2 = list(zip(encrypted, itertools.cycle(key)))
# z = convert(pairs2)
#
# for p in z:
#     print(get_char(p), end='')


keys = []
for i in range(97,123):
    for j in range(97, 123):
        for k in range(97, 123):
            keys.append([i, j, k])

with open('p059_cipher.txt', 'r') as f:
    for lines in f.readlines():
        orig = list(map(int, lines.strip().split(',')))

with open("p059_answers.txt", 'w') as r:
    for k in keys:
        key_pair = list(zip(orig, itertools.cycle(k)))
        decrypted = convert(key_pair)
        temp = []
        will_write = True
        for d in decrypted:
            temp.append(get_char(d))


        r.write(f'{k} - {"".join(temp)}' + "\n")




