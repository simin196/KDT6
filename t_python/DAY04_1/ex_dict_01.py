# ----------------------------------------------
# Dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# - 형태 : { 키1:값, 키2:값,...., 키n:값 }
# - 키는 중복 X, 값은 중복 O
# - 데이터 분석 시 파일 데이터 가져 올 때 많이 사용
# ------------------------------------------------
## [Dict 생성] -----------------------------------
data={}
print(f'data => {len(data)}개, {type(data)}, {data}')

# 사람에 대한 정보 : 이름, 나이, 성별
data={'name':'마징가', 'age':100, 'gender':'남'}
print(f'data => {len(data)}개, {type(data)}, {data}')

# 강아지에 대한 정보 : 품종, 무게, 색상, 성별, 나이
data={'age':5, 'kind':'허스키', 'weight':'3kg', 'color':'검정', 'gender':'남'}
print(f'data => {len(data)}개, {type(data)}, {data}')

## [Dict 원소/요소 읽기] -----------------------------------
## - 키를 가지고 값/데이터 읽기
## - 형식: 변수명[키]
data={'age':5, 'kind':'허스키', 'weight':'3kg', 'color':'검정', 'gender':'남'}

# 색상 출력
print(f'색상 : {data["color"]}')

# 성별, 품종 출력
print(f'강아지 성별 : {data["gender"]}, 품종 : {data["kind"]}')

## [Dict 원소/요소 변경] -----------------------------------
## - 변수명[키] = 새로운 값

# 나이 5살 ==> 6살 
data["age"] = 6
print(data)

# 몸무게 3kg ===> 8kg
data["weight"] = '8kg'
print(data)

## - del 변수명[키]   또는  del(변수명[키])
## 성별 데이터 삭제
del data["gender"]
print(data)

## 추가 : 변수명[새로운 키]=값 -----------------------
## 이름 추가
data["name"]="뽀삐"
print(data)

data["name"]=7
print(data)