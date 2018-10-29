import time


def validate(equation, x_value):
    if 'x' not in equation:
        print('Please type "x" in equation')
        return False

    try:
        int(x_value)
    except ValueError:
        print('x is not a number')
        return False

    return True


def evaluate(equation, x_value):
    if '=' not in equation:
        replaced_eq = equation.replace('x', x_value)
        return eval(replaced_eq)

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

        answer = evaluate(equation, x_value)
        print(f'y: {answer}')
        time.sleep(1)


if __name__ == '__main__':
    main()
