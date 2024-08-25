#--------------------------------------------------------------------------
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
    num1,num2 = input('정수 2개(예:10 2):').split()
    num1=int(num1)
    num2=int(num2)
    
    print(f'결과: {func(num1,num2)}')

#--------------------------------------------------------------------------
# 함수 기능 : 입력받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수 이름 : check
# 매개 변수 : input 입력값(str), 데이터 갯수
# 함수 결과 : True, Fulse

# 1. 원소가 2개인지
# 2. 임마 둘이 숫자인지

def check(num1, num2):
    data=input('예:10 2').split()
    num1=data[0]
    num2=data[1]
    if len(data)==2:
        if num1.isdecimal() and num2.isdecimal():
            return True
        else:
            return False
    else :
        return False
    
#==========================================================================


def check(data, count):
    # 입력된 str==> list 변환 : split()
    date=data.split()
    # 갯수 체크
    if len(data)==count:
        # 0~9로 구성된 str 체크
        if data[0].isdecimal() and data[1].isdecimal():
            return True
        else:
            return False

 

#--------------------------------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴를 출력
# - 종료 메뉴 선택시 프로그램 종료
# -> 반복 무한반복 : while

# while True:

#     # 메뉴 선택
#     print_menu()

#     # 메뉴 선택 요청
#     #choice= int(input('메뉴 선택:'))
#     choice=input('메뉴 선택:')
#     if choice.isdecimal():
#         choice=int(choice)
#     else:
#         print('1~5사이 숫자만 입력하세요')
#         continue
#     # 종료 조건(5번 메뉴 선택) 처리
#     if choice==5:
#         print('프로그램을 종료합니다.')
#         break
#     elif choice ==1: #뎃셈
#         print('덧셈')
#         calc(add,num1,num2)
#     elif choice ==2: #뺄셈
#         print('뺄셈')
#         calc(sub,num1,num2)
#     elif choice ==3: #곱셈
#         print('곱셈')
#         calc(mul,num1,num2)
#     elif choice ==4: #나눗셈
#         print('나눗셈')
#         calc(div,num1,num2)
#     else:
#         print('선택된 메뉴는 없습니다.')

