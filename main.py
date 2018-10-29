import time


def evaluate(equation, x_value):
    y, expression = equation.split('=')
    replaced_eq = expression.replace('x', x_value)
    return eval(replaced_eq)


def main():
    while True:
        equation = input('please input equation(quit: q): ')

        if equation == 'q':
            print('bye')
            break

        x_value = input('please input X: ')
        answer = evaluate(equation, x_value)
        print(f'Y: {answer}')
        time.sleep(1)


if __name__ == '__main__':
    main()
