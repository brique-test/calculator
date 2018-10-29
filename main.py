import time

from functions import validate, make_expression, select_notations, evaluate_infix


def main():
    # 사용자가 종료할 때까지 무한 루프
    while True:
        equation = input('Please input equation(quit: q): ')
        if equation == 'q':
            print('Bye')
            break

        x_value = input('Please input x: ')

        # 입력값이 유효한지를 체크
        is_validated = validate(equation, x_value)
        if is_validated is False:
            continue

        # 방정식에 x값을 대입하고 우변만 쪼갠다
        expression = make_expression(equation, x_value)
        # 입력된 계산이 전위/중위/후위 표기인지 판단
        notation = select_notations(expression)

        # 판단된 표기법에 따라 계산 진행
        # (전위, 후위 표기법에 따른 계산은 해결하지 못함)
        if notation is 'prefix':
            answer = 'prefix'
        elif notation is 'infix':
            answer = evaluate_infix(expression)
        elif notation is 'postfix':
            answer = 'postfix'

        # 해답 출력 및 1초간 휴식 후 루프 재개
        print(f'y: {answer}')
        time.sleep(1)


if __name__ == '__main__':
    main()
