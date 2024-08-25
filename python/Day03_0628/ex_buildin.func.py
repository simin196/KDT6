#--------------------------------------------------------------------------
# 내장함수
#--------------------------------------------------------------------------

# 숫자 데이터 절대값 계산해주는 내장함수 abs(n)
print(abs(-9))

# 최대값, 최소값 찾아주는 내장함수 max(), min()
print(max(10,3), min(10,3))
print(max(10,3,91), min(10,3,-2))
a=[111,222,333]
print(max(a), min(a))
# 제곱근 계산 내장함수 pow()
print('연산자 ** : ', 2**4)
print('내장함수 pow() : ', pow(2,4))

# 파일관련 내장함수 open(파일명, 동작모드, 인코딩)
# - 기본값 : 동작모드 - 읽기 read 'r'
#           인코딩 - 시스템 따라서

FILE_PATH= '0628.txt'
#프로그램에는 변경이 가능한 변수가있고 변경되면 안되는 데이터를 상수라고 부름, BUT 파이썬은 변수만있다. 상수없음 그래서 만들어진것 대문자 명으로 바꾸면 안된다는것을 표시

# [1] 파일열기 - 쓰기 모드로
file=open(FILE_PATH, mode='w', encoding='utf-8')
# [2] 데이터 쓰기
file.write('Hello\n') #\n 줄바꾸기 문자
file.write('안녕~ 좋은 아침이야')
# [3] 파일 닫기
file.close