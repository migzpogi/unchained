with open("13.txt", 'r') as f:
    total = 0
    for lines in f.readlines():
        total += int(lines.strip())

print(str(total)[0:10])


