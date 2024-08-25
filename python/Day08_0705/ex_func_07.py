#--------------------------------------------------------------------------
# 사용자 정의 함수
#--------------------------------------------------------------------------
# 덧셈(a), 뺄셈(b), 곱셈(c), 나눗셈(d) 함수를 각각 만들기
# - 매개 변수 : 정수 2개, num1, num2
# - 함수 결과 : 연산 결과 반환

# def data(num1, num2, any):
#     if any == '+':
#         print(f'{num1} + {num2} = {num1+num2}')
#     elif any == '-':
#         print(f'{num1} - {num2} = {num1-num2}')
#     elif any == '*':
#         print(f'{num1} * {num2} = {num1*num2}')
#     else:
#         print(f'{num1} / {num2} = {num1/num2}')

#------------------------------------------------------


def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌 수 없음'

#-----------------------------------------------------------------------------------------------------
# 함수 기능 : 입력 데이터가 유효한 데이터 인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 갯수 , data, count, sep=''e
# 함수 결과 : 유효 여부 True/False

def check_data(data, count, sep=''):
    # 데이터 여부
    if len(data):
        #데이터 분리 후 갯수 체크
        data2=data.split(sep)
        return True if count== len(data2) else False
    else:
        return False

print(check_data('+ 10 2', 3 )) 


# 함수 호출하기
print(div(10,0))

# 사용자로부터 연산자, 숫자1, 숫자2를 입력 받아서 연산결과를 출력해주세요.
# data = input('연산자, 숫자1, 숫자2 : ' ).split(',') # 공백으로 두면 '.'둘 필요없음
# a=int(data[1])
# b=int(data[2])
# if '+' in data:
#     print(plus(a,b))
# elif '-' in data:
#     print(minus(a,b))
# elif '-' in data:
#     print(mult(a,b))
# elif '-' in data:
#     print(div(a,b))
# else:
#     print('잘못된 입력입니다.')

#===========================================================================================
op, num1, num2 = input('연산자 숫자1 숫자2 : ' ).split(' ')
print(op, num1, num2)

if op not in ['*','-','*','/']:
    print("f'{op} 잘못된 연산자입니다.")
elif num1.isdecimal() and num2.isdecimal():
    num1=int(num1)
    num2=int(num2)
    if op == '+' : result=plus(num1,num2)
    if op == '-' : result=minus(num1,num2)
    elif op == '*' : result=mult(num1,num2)
    else: result=div(num1,num2)
    print(f'{num1}{op}{num2}= {result}')
else:
    print('정수만 입력 가능합니다.')