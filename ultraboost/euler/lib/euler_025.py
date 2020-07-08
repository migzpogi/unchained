import itertools
from leonhard.leonhard import generate_fibonacci_sequence

for i in itertools.count(2):
    sequence = generate_fibonacci_sequence(i)
    x = max(sequence)
    if len(str(x)) == 1000:
        print(sequence.index(x))
        break