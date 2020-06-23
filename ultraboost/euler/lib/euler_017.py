def to_words(n):
    if n == 0:
        return "zero"
    if n == 1:
        return "one"
    if n == 2:
        return "two"
    if n == 3:
        return "three"
    if n == 4:
        return "four"
    if n == 5:
        return "five"
    if n == 6:
        return "six"
    if n == 7:
        return "seven"
    if n == 8:
        return "eight"
    if n == 9:
        return "nine"
    if n == 10:
        return "ten"
    if n == 11:
        return "eleven"
    if n == 12:
        return "twelve"
    if n == 13:
        return "thirteen"
    if n == 14:
        return "fourteen"
    if n == 15:
        return "fifteen"
    if n == 16:
        return "sixteen"
    if n == 17:
        return "seventeen"
    if n == 18:
        return "eighteen"
    if n == 19:
        return "nineteen"
    if n == 20:
        return "twenty"


"""
one two three four five six seven eight nine
ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
twenty thirty forty fifty sixty seventy eighty ninety
onehundred

"""

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

ordinals = []

for o in ones:
    print(o)
    ordinals.append(o)

print('ten')
ordinals.append('ten')

for e in teens:
    print(e)
    ordinals.append(e)

for t in tens:
    print(t)
    ordinals.append(t)
    for o in ones:
        print(f'{t} {o}')
        ordinals.append(f'{t} {o}')

for i in ones:
    print(f"{i} hundred")
    ordinals.append(f"{i} hundred")

    for j in ones:
        print(f"{i} hundred and {j}")
        ordinals.append(f"{i} hundred and {j}")

    print(f"{i} hundred and ten")
    ordinals.append(f"{i} hundred and ten")

    for k in teens:
        print(f"{i} hundred and {k}")
        ordinals.append(f"{i} hundred and {k}")

    for l in tens:
        print(f"{i} hundred and {l}")
        ordinals.append(f"{i} hundred and {l}")

        for o in ones:
            print(f"{i} hundred and {l} {o}")
            ordinals.append(f"{i} hundred and {l} {o}")

print("one thousand")
ordinals.append("one thousand")

print(len(ordinals))
total_words = "".join(ordinals)
no_space = total_words.replace(" ", "")
print(no_space)
print(len(no_space))