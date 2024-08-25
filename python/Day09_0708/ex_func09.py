#--------------------------------------------------------------------------
# 함수 (function)이해 및 활용 >>>>>>??? return
#--------------------------------------------------------------------------
# 형식:
    # 함수명(매개변수)
    # 실행문
    # 실행문
    # retuen 변환값, 결과값 
#--------------------------------------------------------------------------
# 함수 기능 : 2개의 정수를 사칙연산 후 결과를 반환하는 함수
# 함수 이름 : cl
# 매개 변수 : num1,num2
# 함수 결과 : 실수 result
#--------------------------------------------------------------------------
# 함수기반 계산기 프로그램
# - 4칙연산 기능별 함수 생성=> 덧셈, 뺄셈, 곱셈, 나눗셈
# - 2개 정수만 계산
# num1, num2, n = input().split()
# num1=int(num1)
# print(num1)
# num2=int(num2)
# print(num2)
# print(n)

# def cal(num1,num2,n):
#     if n=='+' or n=='-' or n=='*' or n=='/':
#         if num1>0 and num2>0:
#             if n=='+':
#                 result=num1+num2
#                 return result
#             elif n=='-':
#                 result=num1-num2
#                 return result
#             elif n=='*':
#                 result=num1*num2
#                 return result
#             else:
#                 result=num1/num2
#                 return result
#         else:
#             return '정수를 입력해주세요.'   
#     else:
#         return '잘못된 입력입니다.'

# print(cal(num1,num2,n))

#--------------------------------------------------------------------------
# - 사용자가 종료를 원할때 종료=> 'x', 'X' 입력시
# - 연산방식과 숫자 데이터 입력 받기
# - 반복 >>> 반복 횟수를 아는경우 > for 추천
#            반복 횟수를 모르는 경우 > while 추천

def add(num1,num2):
    result=num1+num2
    return result

def sub(num1,num2):
    result=num1-num2
    return result

def mul(num1,num2):
    result=num1*num2
    return result

def div(num1,num2):
    if not num2==0: 
        result=num1/num2
    else:
        result='0으로 나눌수 없음'

while True:
    # (1) 입력받기
    req=input('연산(+,-,*,/)방식과 정수 2개 입력(예:+ 10 2) : ')
    # (2) 종룍 조건 검사
    if req=='x' or req=='X':
        print('계산기를 종료합니다.')
        break

    # (3) 입력에 연산방식과 데이터 추출 '+ 10 2'
    op, num1, num2 = req.split() #['+' '10' '2']
    # (4) str 정수 --> int 변환
    num1=int(num1)
    num2=int(num2)
    # 연산방식에 따라서 계산 진행
    if op=='+':
        print(f'{num1}+{num2} = {add(num1,num2)}')
    elif op=='-':
        print(f'{num1}-{num2} = {sub(num1,num2)}')
    elif op=='*':
        print(f'{num1}*{num2} = {mul(num1,num2)}')
    else:
        print(f'{num1}/{num2} = {div(num1,num2)}')