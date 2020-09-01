import string

def word_to_number(word):
    word = word.lower()
    alphabet = list(string.ascii_lowercase)

    sum_of_positions = 0
    for w in word:
        position = alphabet.index(w) + 1
        sum_of_positions += position

    return sum_of_positions

def is_triangular(n):
    if (((8*n) + 1)**0.5) % 1 == 0:
        return True
    else:
        return False


with open("p042_words.txt", 'r') as f:
    for lines in f.readlines():
        words = lines.strip()

triangle_count = 0
for w in words.split(","):
    clean = w.replace('"', '')
    value = word_to_number(clean)
    if is_triangular(value):
        triangle_count += 1

print(triangle_count)


def generate_triange_sequence(n):
    return (n+1) * n * 0.5








# print(generate_triange_sequence(10))
# print(word_to_number("SKY"))
# print(is_triangular(4))