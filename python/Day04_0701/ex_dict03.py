#--------------------------------------------------------------------------
# Dict 자료형 살펴보기
# - Dict 자료형 전용의 함수 즉, 메서드(Method) 사용
# Method 사용법 : 변수명.메서드명()
#--------------------------------------------------------------------------

p1={'name':'홍길동', 'age': 20 , 'job' : '학생'}

## [Dict에서 키만 추출하는 매서드 keys()]
result = p1.keys() # list로 묶어 추출 >> but type다름 dict 형태
print(f'key 추출 : {result}, {type(result)}')
# ERROR : print(result[0])

# list 형 변환 => list(dict_key타입)
result=list(result) #>>> list로 변환해서 list를 합치던지 빼는 함수를 사용하던지 가능
print(f'키 추출 : {result}, {type(result)}')

# dict에서 값/데이터 만 추출하는 메서드 .values()
result = p1.values()
print(f'값 추출 : {result}, {type(result)}')

# dict에서 키와 값을 묶어 추출하는 메서드 .items()
result = p1.items()
print(f'키와 값 추출 : {result}, {type(result)}')

result=list(result)
print(f'키와 값 추출 : {result[0]}, {type(result[0])}') #>>> list안 딕셔너리는 key와 value값이 tuple로 묶여서 나옴 

