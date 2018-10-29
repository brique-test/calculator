import time

from functions import validate, make_expression, select_notations, evaluate_infix


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

        expression = make_expression(equation, x_value)
        notation = select_notations(expression)

        if notation is 'prefix':
            answer = 'prefix'
        elif notation is 'infix':
            answer = evaluate_infix(expression)
        elif notation is 'postfix':
            answer = 'postfix'

        print(f'y: {answer}')
        time.sleep(1)


if __name__ == '__main__':
    main()
