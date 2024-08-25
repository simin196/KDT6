#--------------------------------------------------------------------------
# 내장함수 range()
# - 숫자 범위를 생성하는 내장함수
# - 형식 : range(시작 숫자, 끝 숫자+1, 간격)
#          range(끝 숫자 +1)
#--------------------------------------------------------------------------
# 1~100 숫자를 저장하세요
nums=range(1,101)
print(f'nums 값 : {nums}\n 타입 : {type(nums)}\n 개수 : {len(nums)}')

# 요소/원소 읽기 (인덱싱 이용)
print( nums[0], nums[-1])

# 요소/원소 여러개 읽기 (슬라이싱 이용)
print(nums[0:10], nums[30:41]) # ===> range 형태로 나온다.

# 요소/원소 하나하나 보고싶으면 > list\tuple로 형변환
print(list(nums[0:10]), tuple(nums[30:41]))

#--------------------------------------------------------------------------

# 1~100사이 3의 배수만 저장하세요.
three = range(3,101,3)
print(list(three))

#--------------------------------------------------------------------------

# 1.0 ~ 10.0사이에 숫자 저장
data = list(range(1, 11))
# print(data)
# print(float(data))     # 바로 float으로 가지못함 왜>> list에 값이 많아서 float함수의 경우 한개만 치환 해줄수있는데 list의 경우 많은 값이있어 일일이 다 대입을 해줘야한다

datas = list (map(float, data)) # 각 인덱스에 float을 대입해줘야 하는데 많기도 하고 하기 힘듬 >>> 그래서 map() 함수 사용
print(datas)