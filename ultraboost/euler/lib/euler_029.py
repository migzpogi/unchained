a = range(2, 101)
b = range(2, 101)

distinct_terms = []
for i in a:
    for j in b:
        product = i**j
        if product not in distinct_terms:
            distinct_terms.append(i**j)

print(len(distinct_terms))