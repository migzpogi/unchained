import re
valid_operators = ["+", "-", "*", "/"]


def evaluate_prefix(expression):
    """
    Evaluates the given prefix expression
    Must be integers
    
    Args:
        expression str: mathematical expression to be evaluated in prefix notation

    Returns:

    """
    while True:
        prefix_match = re.search(r'([-+\/\*]) ([-]?\d+) ([-]?\d+)', expression)  # searches the expression for operator-operand-operand
        if prefix_match:
            ans = eval('%s %s %s' % (prefix_match.group(2), prefix_match.group(1), prefix_match.group(3)))  # evaluate the matched pattern
            substitute_ans = re.sub(r'([-+\/\*]) ([-]?\d+) ([-]?\d+)', str(ans), expression)  # substitute the answer to the expression

            next = re.search(r'([-+\/\*]) ([-]?\d+) ([-]?\d+)', substitute_ans)
            if next is None:
                try:
                    return int(substitute_ans)
                except:
                    return None
            else:
                expression = substitute_ans
        else:
            return None


x = '+ + 1 * 2 3 4' # 11
print(evaluate_prefix(x))

x = '+ + 1 * 2 3 4 +' # None
print(evaluate_prefix(x))

x = '* - + 2 7 5 4' # 16
print(evaluate_prefix(x))

x = '- + 10 * 2 8 3' # 23
print(evaluate_prefix(x))

x = '/ * + 3 14 2 7' # 4
print(evaluate_prefix(x))