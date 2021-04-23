"""
Write a function to generate all possible n pairs of balanced parentheses. 
"""

def printParenthesis(str, n):
    if (n > 0):
        _printParenthesis(str, 0,
                          n, 0, 0)
    return


def _printParenthesis(str, pos, n,
                      open, close, y=""):
    if (close == n):
        for i in str:
            y += i
        x.append(y)
        return
    else:
        if (open > close):
            str[pos] = ')'
            _printParenthesis(str, pos + 1, n,
                              open, close + 1)
        if (open < n):
            str[pos] = '('
            _printParenthesis(str, pos + 1, n,
                              open + 1, close)

x = []
n = 3
output = [""] * 2 * n
printParenthesis(output, n)

print(x)