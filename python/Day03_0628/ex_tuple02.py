#--------------------------------------------------------------------------
# Tuple 데이터 자료형 살펴보기 
# - 내장함수 : len() max() min() sum()
# - 연산자 : 덧셈, 곱셈, 멤버 연산자
#--------------------------------------------------------------------------
nums= 11,22,33,44,55

## 내장함수
print(f'nums 개수 : {len(nums)}개')
print(f'최대값 : {max(nums)} 최소값 : {min(nums)}')
print(f'합계 : {sum(nums)}') # => 정수만 가능, 정수의 합계를 합산해서 낸다.
print(f'정렬 : {sorted(nums)}, {sorted(nums, reverse=True)}') #==> 기본 오름차순 reverse=True을 입력해서 내림차순도 가능

print(max('abc', 'aBC')) # 아스키코드로는 소문자들이 더 크다
print(sorted(('abc' , 'zoo')))


## 연산자
# 덧셈
data1=11,22
data2='A','B','C'
data3= [1,2]

print(data1+data2) # tuple+tuple
# print(data1+data3) >>> tuple+list X >>> ERROR 
print(data1+tuple(data3)) # >> 형변환 후엔 가능

# 곱셈 : tuple*int
print(data1*3) #>> 정수만큼 반복 및 연결

## 멤버 연산자 > in, not in >> True, False로 결과나옴
print(11 in data1)
print('A' in data1)