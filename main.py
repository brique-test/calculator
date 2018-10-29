import time
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


def make_deque(equation):
    _, expression = equation.split('=')
    strip_ex = expression.replace(' ', '')
    return deque(chain(strip_ex))


def select_notations(collection):
    brackets = ('(', ')')
    operators = ('+', '-', '*', '/')
    operator_count = 0
    num_count = 0

    while True:
        token = collection.popleft()
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


def evaluate_infix(equation, x_value):
    _, expression = equation.split('=')
    replaced_ex = expression.replace('x', x_value)
    return eval(replaced_ex)


def main():
    while True:
        equation = input('Please input equation(quit: q): ')
        if equation == 'q':
            print('Bye')
            break

        x_value = input('Please input x: ')

        is_validated = validate(equation, x_value)
        if is_validated is False:
            continue

        deque_eq = make_deque(equation)

        notation = select_notations(deque_eq)

        if notation is 'prefix':
            pass
        elif notation is 'infix':
            pass
        elif notation is 'postfix':
            pass

        answer = evaluate_infix(equation, x_value)
        print(f'y: {answer}')
        time.sleep(1)


if __name__ == '__main__':
    main()
