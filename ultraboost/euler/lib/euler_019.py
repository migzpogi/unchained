import datetime
name = datetime.datetime(1900, 1, 1)
print(name.strftime("%A"))

count = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        for k in range(1, 32):
            try:
                name = datetime.datetime(i, j, k).strftime("%A")
                if name == "Sunday" and k == 1:
                    count += 1
            except:
                pass

print(count)