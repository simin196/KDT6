#--------------------------------------------------------------------------
# 사용자 정의 함수
#--------------------------------------------------------------------------
# 함수 기능 : 원하는 단의 구구단을 출력해주는 기능 함수
# 함수 이름 : gugudan 
# 매개 변수 : num
# 함수 결과 : None

def gugudan(num):
    for n in range(1,10):
        print(f'{num} * {n} = {num * n}')

#---------------------------------------------------
# 함수 기능 : 파일의 확장자를 반환해주는 기능 함수
# 함수 이름 : extract
# 매개 변수 : file_name
# 함수 결과 : 확장자 str

def extract(file_name):
    # result = file_name[file_name.rfind('.')+1 :]
    # return result
    return file_name[file_name.rfind('.')+1 :]

##---------------------
print(extract("abc.jpeg"))
gugudan(6)

# 목적 : 매개 변수의 개수를 유동적으로
#       0개~ n개 까지 가능하도록
# 형태 : def 함수명( *변수명 ) <= 0개 ~ n개 데이터

#---------------------------------------------------
# 함수 기능 : 정수를 덧셈 한 후 결과를 반환/리턴하는 함수
# 함수 이름 : add
# 매개 변수 : 0개 ~ N개 (가변인자 함수 > 변수가 n개 있다. > 몇개냐가 변한다. )
# 함수 결과 : 덧셈 계산 값 result

def add(*nums):
    total=0
    for n in nums:
        total += n
    return total

# 함수 호출
print(add())
print(add(1,1,1))
print(add(5,6))
print(add(8,9,11,22,55,11,6,7))