def get_score(s):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')

    score = 0
    for i in s.lower():
        score += alphabet.index(i) + 1

    return score

with open("p022_names.txt", 'r') as f:
    for l in f.readlines():
        names = l.strip()

name_list = names.split(',')
s = sorted(name_list)

total = 0
for idx, i in enumerate(s):
    score = get_score(i.replace('"', '')) * (idx+1)
    total += score

print(total)