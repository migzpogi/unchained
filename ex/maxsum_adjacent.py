"""
Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the
sequence should be adjacent in the array.

3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7)
"""


def solution(n):
    x = 0
    y = 0

    for i in n:
        if y > x:
            z = y
        else:
            z = x

        x = y + i
        y = z

    return max(x, y)


n = [3, 2, 7, 10]
print(solution(n))

n = [3, 2, 5, 10, 7]
print(solution(n))