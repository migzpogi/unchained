def digits_to_power(number, power):
    total = 0
    for n in str(number):
        total += int(n)**power

    if number == total:
        return number
    else:
        return 0

total = 0
for i in range(2, 295245):  # limit is computed as 5 * 9**5
    total += digits_to_power(i, 5)

print(total)