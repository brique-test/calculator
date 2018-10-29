from collections import deque
from itertools import chain


def validate(equation, x_value):
    if 'x' not in equation:
        print('Please type "x" in equation')
        return False

    if '=' not in equation:
        print('Please type equation, not expression')
        return False

    try:
        int(x_value)
    except ValueError:
        print('x is not a number')
        return False

    return True


def replace_to_x_value(equation, x_value):
    return equation.replace('x', x_value)


def split_expression(equation):
    _, expression = equation.split('=')
    return expression


def make_expression(equation, x_value):
    replaced_eq = replace_to_x_value(equation, x_value)
    return split_expression(replaced_eq)


def make_deque(expression):
    strip_ex = expression.replace(' ', '')
    return deque(chain(strip_ex))


def select_notations(expression):
    deque_eq = make_deque(expression)
    brackets = ('(', ')')
    operators = ('+', '-', '*', '/')
    operator_count = 0
    num_count = 0

    while True:
        token = deque_eq.popleft()
        if token in brackets:
            continue

        if token in operators:
            if num_count == 0:
                operator_count += 1
                continue
            elif num_count == 1:
                return 'infix'
            elif num_count >= 2:
                return 'postfix'

        else:
            if operator_count == 0:
                num_count += 1
                continue
            elif operator_count >= 1:
                return 'prefix'


def evaluate_prefix(expression):
    pass


def evaluate_infix(expression):
    return eval(expression)


def evaluate_postfix(expression):
    pass
