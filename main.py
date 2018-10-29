if __name__ == '__main__':
    equation = input('please input equation: ')
    x = input('please input X: ')
    y, expression = equation.split('=')
    replaced_eq = expression.replace('x', x)
    answer = eval(replaced_eq)
    print(f'Y: {answer}')
