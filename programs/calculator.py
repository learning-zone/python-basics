import unittest

# Correct, but uses eval
# def evaluate(expression):
#     return eval(expression)


# Correct, but uses eval
# def evaluate(expression):
#     storage = []
#     parens_indices = []

#     for i in range(len(expression)):
#         char = expression[i]
#         if char == '(':
#             parens_indices.append(i)
#         elif char == ')':
#             start = parens_indices.pop() + 1  # parens + 1 position
#             total = str(eval(expression[start:i]))
#             storage = storage[:start-1]
#             storage.append(total)
#         else:
#             storage.append(char)

#     string_expression = ''.join(storage)
#     return eval(string_expression)


# Without using eval:
def evaluate(expression):
    expression = ''.join(expression.split(' '))
    storage = []
    parens_indices = []
    operators = {'*': [], '/': [], '+': [],'-': []}

    for i in range(len(expression)):
        char = expression[i]
        if char == '(':
            parens_indices.append(i)
        elif char == ')':
            start = parens_indices.pop() + 1
            total = str(calculate(expression[start:i], operators))
            storage = storage[:start-1]
            storage.append(total)
        else:
            storage.append(char)

        if char in operators:
            operators[char].append(i)

    string_expression = ''.join(storage)
    return calculate(string_expression, operators)


def calculate(inner_expression, operators):
    total = 0
    operators = {'*': [], '/': [], '+': [],'-': []}
    new_expr = inner_expression

    for i in range(len(inner_expression)):
        char = inner_expression[i]
        if char in operators:
            operators[char].append(i)

    while operators['*'] != []:
        op_index = operators['*'].pop()
        prev = new_expr[op_index-1]
        nxt = new_expr[op_index+1]
        total = int(prev) * int(nxt)
        new_expr = new_expr[:op_index-1] + str(total) + new_expr[op_index+2:]
        print(new_expr)

    while operators['/'] != []:
        op_index = operators['/'].pop()
        prev = new_expr[op_index-1]
        nxt = new_expr[op_index+1]
        total = int(prev) / int(nxt)
        new_expr = new_expr[:op_index-1] + str(total) + new_expr[op_index+2:]

    while operators['-'] != []:
        op_index = operators['-'].pop()
        prev = new_expr[op_index-1]
        nxt = new_expr[op_index+1]
        total = int(prev) - int(nxt)
        new_expr = new_expr[:op_index-1] + str(total) + new_expr[op_index+2:]

    while operators['+'] != []:
        op_index = operators['+'].pop()
        prev = new_expr[op_index-1]
        nxt = new_expr[op_index+1]
        total = int(prev) + int(nxt)
        new_expr = new_expr[:op_index-1] + str(total) + new_expr[op_index+2:]

    return total



class Testing(unittest.TestCase):

    def test_no_parens(self):
        self.assertEqual(evaluate('1 + 3 * 2'), 7)

    def test_single_parens(self):
        self.assertEqual(evaluate('(1 + 7) * 2'), 16)

    def test_operations_order(self):
        self.assertEqual(evaluate('4 * (1 + 7) - 3'), 29)

    def test_long_parens(self):
        self.assertEqual(evaluate('(4 - 7 - 1) * 3'), -6)

    def test_decimals(self):
        self.assertEqual(evaluate('(1.2 + 1.3) * 2.5'), 6.25)


if __name__ == '__main__':
    unittest.main()

