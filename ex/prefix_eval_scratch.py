# def validate_expression(expression):
#     """
#     Checks if the given prefix expression is valid or not
#
#     Rules:
#         * Must be positive integers
#
#     Args:
#         expression str: prefix expression
#
#     Returns list: list of operators and operands, None if not valid
#
#     """
#
#     valid_operators = ["+", "-", "*", "/"]
#     valid_expression = []
#
#     for i in expression.split(" "):
#         if i in valid_operators:
#             valid_expression.append(i)
#             continue
#         try:
#             if int(i) > 0:
#                 valid_expression.append(i)
#             else:
#                 return None
#
#     return valid_expression
#
# def split_expression(expression):
#     valid_exp = []
#     for i in expression.split(" "):
#         if i in valid_operators:
#             valid_exp.append(i)
#             continue
#         if i[0] == '0':
#             return None
#         try:
#             if int(i) > 0:
#                 valid_exp.append(i)
#             else:
#                 return None
#         except Exception:
#             valid_exp.append(i)
#
#     return " ".join(valid_exp)
#
#
# x = '+ + 1 * 2 3 4' # 11
# print(split_expression(x))
#
#
# def z(expression):
#     while True:
#         m = re.search(r'([-+\/\*]) ([-]?\d+) ([-]?\d+)', expression)
#         if m:
#             ans = eval('%s %s %s' % (m.group(2), m.group(1), m.group(3)))
#             print(ans)
#             after = re.sub(r'([-+\/\*]) ([-]?\d+) ([-]?\d+)', str(ans), expression)
#             print(after)
#             n = re.search(r'([-+\/\*]) ([-]?\d+) ([-]?\d+)', after)
#             if n is None:
#                 return ans
#             else:
#                 expression = after
#         else:
#             return None
#
# print(z(x))