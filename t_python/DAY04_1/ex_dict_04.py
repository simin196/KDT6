# ----------------------------------------------
# Dict 자료형 살펴보기
# - 연산자와 내장함수
# -----------------------------------------------
person={'name':'홍길동', 'age':20,  'job':'학생'}
dog={'age':5, 'kind':'허스키', 'weight':'3kg', 'color':'검정', 'gender':'남'}
jumsu={'국어':90, '수학':178, '체육':100}

## [연산자] --------------------------------------
# 산술 연산 X 
# person+dog 

# 멤버 연산자 : in, not in
#      key
print('name' in dog )
print('name' in person )

#      value  : dict 타입에서는 key만 멤버 연산자로 확인
# print('허스키' in dog )
# print(20 in person )

# value추출 
print('허스키' in dog.values() )
print(20 in person.values() )

## [내장함수] --------------------------------------
## - 원소/요소 개수 확인 : len()
print(f' dog의 요소 개수 : {len(dog)}개')
print(f' person의 요소 개수 : {len(person)}개')

## - 원소/요소 정렬 : sorted() 
#  - 키만 정렬
print(f' dog 오름차순정렬: {sorted(dog)}')
print(f' dog 내림차순정렬: {sorted(dog, reverse=True)}')

print(f' jumsu 값 오름차순정렬: {sorted(jumsu.values())}')
print(f' jumsu 키 오름차순정렬: {sorted(jumsu)}')
#  jumsu 값 오름차순정렬: [90, 100, 178]
#  jumsu 키 오름차순정렬: ['국어', '수학', '체육']

print(f' jumsu 값 오름차순정렬: {sorted(jumsu.items())}')
#  jumsu 값 오름차순정렬: [('국어', 90), ('수학', 178),  ('체육', 100)]
#                                                      ('국어', 90):
print(f'jumsu 값 오름차순정렬: {sorted(jumsu.items(), key=lambda x:x[1])}')



## - 동일한 타입에서 정렬 가능함 -------------------------
n1=[1,4,9,-2]
n2=['a', 'Z','f']
n3=[1, 'A', -4, 9, 'F']
#print(sorted(n3))