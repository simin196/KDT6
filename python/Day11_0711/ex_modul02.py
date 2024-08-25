#--------------------------------------------------------------------------
## modul 모듈 >> 파이썬 파일(py) 1개
# 구성 - 변수, 함수, 클래스가 존재
#       반드시 모두 다 있지는 않음!
# 종류 - 내장 모듈 / 사용자정의모듈/ 써드파티션모듈(설치필수)
#--------------------------------------------------------------------------
## 사용법 => 현재 파이썬 파일에 포함시켜야 사용 가능함
## 모듈 내에서 일부 변수, 함수, 클래스만 포함하는 경우
# 형식 - form 모듈명 import 변수명/함수명/클래스명
# 주의 - 파일안에 동일한 변수명/함수명/클래스명 존재하면 해당 파일에 변수명/함수명/클래스명 사용됨 ~!
# if ~~ apple밑에 pi를 두면 원주율 pi값이 나온다. >>> 근데 변수가 같으면 헷갈리기에 웬만하면 안겹치게 변수 만들기
from math import pi, factorial, e # 희미하게 있으면 사용하고있지 않다는 표싣

## 모듈안에 있는걸 모든걸 가지고 오고 싶으면
from random import * 

# from ex_func11 import * # >>>>>>>>???

## 전역변수 -----------
pi='apple' #>>>> 변수 이름이 같다면 내꺼를 쓴다 그래서 밑에 pi에 apple출력



# 사용할땐 바로 변수명/함수명/클래스명 사용
print(f'내장모듈 math안에 있는 pi변수 사용 : {pi}') # > 가지고 온것만 사용가능
print(factorial(5))

# print(random(),random(2,5)) #>>>???? 왜 안되 ㅋㅋㅋㅋ