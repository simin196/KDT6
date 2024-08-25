#--------------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# - 형태 : { 키1: 값, 키2:값,..., 키n: 값}
# - 키는 중복x 값음 중복o
# - 데이터 분석 시 파일 데이터 가져 올 때 많이 사용
#--------------------------------------------------------------------------
## [Dict 생성]

data={}

print(f'data => {len(data)}개, {type(data)}, {data}')

# 사람에 대한 정보 : 이름, 나이, 성별

data={'name': '마징가', 'age' : 10, 'gender': '남'} # >> key:value을 한 요소로 본다.
print(f'data => {len(data)}개, {type(data)}, {data}')

# 강아지에 대한 정보 : 품종, 무게, 색상, 성별, 나이

dag={'type':'golden', 'weight':10, 'color':'gold' , 'gender':'men' , 'age' : 30}
print(f'data => {len(dag)}개, {type(dag)}, {dag}')

# Dict의 원소/요소 읽기
# - 키를 가지고 값/데이터 읽기
# - 형식 : 변수명 [key]

dag={'type':'golden', 'weight':10, 'color':'gold' , 'gender':'men' , 'age' : 5}

# 색상 출력
print(f'색상 : {dag["color"]}')

# 성별 , 품종
print(f'성별 : {dag["gender"]}, 품종 : {dag["type"]}') 

##원소/요소 변경

#강쥐 5 > 6 살로 나이먹음

dag["age"] =6
print(dag)

# 몸무게 10 > 8줄어듬
dag['weight'] = 8
print(dag)

## - del 변수명 [키] 또는 del(변수명[키])
# 성별 데이터 삭제
del dag['gender']
print(dag)

## - 추가 : 변수명 [새로운 키] = 값
# 이름 추가
dag['name']='뽀삐'
print(dag) # >>끝에 추가

# 이름 수정
dag['name']='마징가'
print(dag) #>>> key가 없으면 추가, key가 있으면 업데이트(변경)



