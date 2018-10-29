from collections import deque
from itertools import chain


# 입력값 검증 함수
def validate(equation, x_value):
    # 방정식에 x 변수가 없다면 invalid
    if 'x' not in equation:
        print('Please type "x" in equation')
        return False

    # equal 로 표현되지 않았다면 invalid
    if '=' not in equation:
        print('Please type equation, not expression')
        return False

    # x 변수가 숫자로 입력되지 않았다면 invalid
    try:
        int(x_value)
    except ValueError:
        print('x is not a number')
        return False

    return True


# x 변수를 식에 대입하는 함수
def replace_to_x_value(equation, x_value):
    return equation.replace('x', x_value)


# 방정식에서 우변만 쪼개는 함수
def split_expression(equation):
    _, expression = equation.split('=')
    return expression


# 두 가지 헬퍼 함수를 이욯애 최종적으로 가공된 표현식을 만드는 함수
def make_expression(equation, x_value):
    replaced_eq = replace_to_x_value(equation, x_value)
    return split_expression(replaced_eq)


# 표현식의 모든 요소를 원소로 하는 deque 생성 함수
def make_deque(expression):
    strip_ex = expression.replace(' ', '')
    return deque(chain(strip_ex))


# 표기법 판단 함수
def select_notations(expression):
    # 입력받은 표현식으로 deque 생성
    deque_eq = make_deque(expression)
    # 괄호와 연산자
    brackets = ('(', ')')
    operators = ('+', '-', '*', '/')
    # 몇 개의 연산자와 피연산자가 지나갔는지 카운트
    operator_count = 0
    num_count = 0

    # deque 원소가 남아있는 동안 루프 진행
    while len(deque_eq) > 0:
        # 매 순회 사이클마다 deque 의 첫 번째 요소를 꺼낸다
        token = deque_eq.popleft()

        # 토큰이 괄호 요소라면 무시하고 루프 재시작
        if token in brackets:
            continue

        # 토큰이 연산자일 경우
        if token in operators:
            # 피연산자가 한 차례도 지나가지 않았다면
            # 연산자 카운트를 1 추가하고 루프 재시작
            if num_count == 0:
                operator_count += 1
                continue
            # 피연산자가 단 1회 지나갔다면 중위 표기
            elif num_count == 1:
                return 'infix'
            # 피연산자가 2회 이상 지나갔다면 후위 표기
            elif num_count >= 2:
                return 'postfix'

        # 토큰이 피연산자일 경우
        else:
            # 연산자가 한 차례도 지나가지 않았다면 중위 / 후위 표기일 가능성이 있음
            # 피연산자 카운트를 1 추가하고 루프 재시작
            if operator_count == 0:
                num_count += 1
                continue
            # 연산자가 1회 이상 지나갔다면 전위 표기
            elif operator_count >= 1:
                return 'prefix'


# 전위 표기식 계산 함수 (개발 못함)
def evaluate_prefix(expression):
    pass


# 중위 표기식 계산 함수
def evaluate_infix(expression):
    return eval(expression)


# 후위 표기식 계산 함수 (개발 못함)
def evaluate_postfix(expression):
    pass
