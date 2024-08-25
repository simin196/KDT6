#--------------------------------------------------------------------------
# - 사용자가 종료를 원할때 종료=> 'x', 'X' 입력시
# - 연산방식과 숫자 데이터 입력 받기
# - 반복 >>> 반복 횟수를 아는경우 > for 추천
#            반복 횟수를 모르는 경우 > while 추천

# def add(num1,num2):
#     result=num1+num2
#     return result

# def sub(num1,num2):
#     result=num1-num2
#     return result

# def mul(num1,num2):
#     result=num1*num2
#     return result

# def div(num1,num2):
#     if not num2==0: 
#         result=num1/num2
#     else:
#         result='0으로 나눌수 없음'

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
    if num2!=0: 
        result=num1/num2
        return result
    else:
        return '0으로 나눌수 없음'

#--------------------------------------------------------------------------
# 함수 기능 : 계산기 메뉴를 출력하는 함수
# 함수 이름 : print_menu
# 매개 변수 : 없음
# 함수 결과 : 없음
def print_menu(): # 매개 변수가 없어도 ()해야 함수인것을 인식
    print(f'{"*":*^16}')
    print(f'{"계 산 기":^16}')
    print(f'{"*":*^16}')
    print(f'{"* 1. 덧    셈  *":16}')
    print(f'{"* 2. 뺄    셈  *":16}')
    print(f'{"* 3. 곱    셈  *":16}')
    print(f'{"* 4. 나 눗 셈  *":16}')
    print(f'{"* 5. 종    료  *":16}')
    print(f'{"*":*^16}')

# print(f'{"*":*^16}')    # 가운데 정렬
# print(f'{"*":<16}')    # 왼쪽 정렬
# print(f'{"*":>16}')    # 오른쪽 정렬

#--------------------------------------------------------------------------
# 함수 기능 : 연산수행 후 결과를 변환하는 함수
# 함수 이름 : calc
# 매개 변수 : 함수명, str 숫자 2개
# 함수 결과 : 없음

def calc(func, num1, num2):
    num1=int(num1)
    num2=int(num2)
    print(f'결과: {func(num1,num2)}')

#--------------------------------------------------------------------------
# while True:
#     # (1) 입력받기
#     req=input('연산(+,-,*,/)방식과 정수 2개 입력(예:+ 10 2) : ')
#     # (2) 종룍 조건 검사
#     if req=='x' or req=='X':
#         print('계산기를 종료합니다.')
#         break

#     # (3) 입력에 연산방식과 데이터 추출 '+ 10 2'
#     op, num1, num2 = req.split() #['+' '10' '2']
#     # (4) str 정수 --> int 변환
#     num1=int(num1)
#     num2=int(num2)
#     # 연산방식에 따라서 계산 진행
#     if op=='+':
#         print(f'{num1}+{num2} = {add(num1,num2)}')
#     elif op=='-':
#         print(f'{num1}-{num2} = {sub(num1,num2)}')
#     elif op=='*':
#         print(f'{num1}*{num2} = {mul(num1,num2)}')
#     else:
#         print(f'{num1}/{num2} = {div(num1,num2)}')




#--------------------------------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴를 출력
# - 종료 메뉴 선택시 프로그램 종료
# -> 반복 무한반복 : while

while True:

    # 메뉴 선택
    print_menu()

    # 메뉴 선택 요청
    #choice= int(input('메뉴 선택:'))
    choice=input('메뉴 선택:')
    if choice.isdecimal():
        choice=int(choice)
    else:
        print('1~5사이 숫자만 입력하세요')
        continue
    # 종료 조건(5번 메뉴 선택) 처리
    if choice==5:
        print('프로그램을 종료합니다.')
        break
    elif choice ==1: #뎃셈
        print('덧셈')
        num1,num2 = input('정수 2개(예:10 2):').split()
        calc(add,num1,num2)
    elif choice ==2: #뺄셈
        print('뺄셈')
        num1,num2 = input('정수 2개(예:10 2):').split()
        calc(sub,num1,num2)
    elif choice ==3: #곱셈
        print('곱셈')
        num1,num2 = input('정수 2개(예:10 2):').split()
        calc(mul,num1,num2)
    elif choice ==4: #나눗셈
        print('뺄샘')
        num1,num2 = input('정수 2개(예:10 2):').split()
        calc(div,num1,num2)
    else:
        print('선택된 메뉴는 없습니다.')

# # div(10,2)