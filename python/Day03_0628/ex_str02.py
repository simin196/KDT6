#--------------------------------------------------------------------------
# 문자열 str 데이터 다루기 
# - 문자 요소 연산 : 산술, 비교, 멤버 연산
#--------------------------------------------------------------------------

##[1] 산술 연산

data1 = 'Happy'
data2 = 'Year'

# 덧셈(+) 연산 :  str+str => str연결 (str끼리만 연결, 그 이외의것은 str로 형변환 후 이용)
print(f'{data1}+{data2} => {data1+data2}')
print(f'{data1}+ {10} => {data1+str(10)}')

# print(f'{data1}-{data2} => {data1-data2}') > unsupported 미지원

# 곱셈(*) 연산 str * int => 숫자만큼 반복 str연결  
# print(f'{data1}*{data2} => {data1*data2}') => str*str XXXX
print(f'{data1}*{10} => {data1*10}')



## [2] 멤버 연산
# 요소/원소 (not)in 문자열 ==> 존재하면 True(False), 없으면 False(True) (not은 반대)

print(f'h in {data1} : {"h" in data1}')
print(f'h not in {data1} : {"h" not in data1}')

# print(3 in 123) # ERROR
# print(len(123)) # ERROR
# > in연산자와 len내장함수는 원소/요소를 가지는 데이터 타입에서 사용