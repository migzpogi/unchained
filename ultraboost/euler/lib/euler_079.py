keylogs = []

with open("keylog.txt", "r") as f:
    for lines in f.readlines():
        keylogs.append(lines.strip())

print(len(keylogs))
print(len(list(set(keylogs))))

# 73162890