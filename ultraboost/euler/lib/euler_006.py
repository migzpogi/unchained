"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum
is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

25164150
"""

natural_number = 100
sum_of_the_squares = sum(list(map(lambda x: x**2, range(1, natural_number+1))))
print(sum_of_the_squares)
square_of_the_sum = sum(range(1, natural_number+1))**2
print(square_of_the_sum)
print(square_of_the_sum - sum_of_the_squares)