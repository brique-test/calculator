# Calculator App

## 개요

방정식과 x 변수를 입력받으면 결과를 출력하는 계산기입니다. CLI 환경에서 작동합니다. 전위 / 중위/ 후위 표기법을 모두 아우르는 것이 주요 포인트이지만 식의 표기법을 판단하는 방법을 구상하는 데까지만 성공하고 계산까지 해내진 못했습니다.

파이썬 3.7.0을 사용했고 추가 패키지는 사용하지 않았습니다.

## 파일 구조

```
.
├ main.py // 실행 파일
└ function.py // 함수 모듈 파일
```

## 설치 및 실행

소스코드 디렉터리에 들어가서 `main.py`를 실행하시면 됩니다.

```
$ cd calculator
$ python main.py
```

## 사용법

프로그램이 실행되면 방정식과 x 변수의 값을 차례로 입력하십시오.

```
$ python main.py
>>> Please input equation(quit: q):

$ y = 20 + ((10 + x) / (100 - x))
>>> Please input x:

$ 4
>>> y: 20.145833333333332

```

프로그램을 종료하려면 'q'를 입력하면 됩니다.

```
$ python main.py
>>> Please input equation(quit: q):

$ q
>>> Bye
```

'='이 담긴 부등식이 아니거나, 식에 x 값이 없거나, 혹은 입력받은 x가 숫자가 아니라면 경고를 출력합니다.

```
>>> Please input equation(quit: q):
$ x + 1
>>> Please type equation, not expression
$ y = 1
>>> Please type "x" in equation

>>> Please input x:
$ a
>>> x is not a number

```

표기법을 판단하고 계산하는 과정까지 넣고 싶었지만, 아직까지는 표기법 판단 함수의 컨셉까지만 개발한 상태입니다.
