#--------------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 연산자의 내장함수
#--------------------------------------------------------------------------
person={'name':'홍길동', 'age': 20 , 'job' : '학생'}
dog={'type':'golden', 'weight':10, 'color':'gold' , 'gender':'men' , 'age' : 30}
jumsu= { '국어': 90, '영어':80 , '수학' : 100}

## 연산자
# 산술 연산 x
# person+dog

# 멤버 연산자 가능
# 1.key로
print('name' in dog)
print('name' in person)

# # 2.value로 > dict 타입에서는 불가 >>> key만 멤버 연산자로 확인
print('golden' in dog)
print('홍길동' in person)

# 그래도 value를 확인해보고싶다. > value추출
print('golden' in dog.values())
print('홍길동' in person.values())

## 내장함수
# 원소 요소 갯수 확인  > len()
print(f' dog의 요소 개수 : {len(dog)}개')
print(f' person의 요소 개수 : {len(person)}개')

# 원소 요소 정렬 > sorted()
# -키만 정렬
print(f' dog 오름차순정렬 : {sorted(dog)}') 
print(f' dog 내림차순정렬 : {sorted(dog, reverse=True)}') 

print(f' jumsu 값 오름차순 정렬 : {sorted(jumsu.values())}') # >>> jumsu 값 오름차순 정렬 : [80, 90, 100]
print(f' jumsu key 오름차순 정렬 : {sorted(jumsu)}') # >>> jumsu key 오름차순 정렬 : ['국어', '수학', '영어']

# 같이 이동 안함 자리 않맞음
print(f' jumsu 값 오름차순 정렬 : {sorted(jumsu.items())}') # >>> jumsu 값 오름차순 정렬 : [('국어', 90), ('수학', 100), ('영어', 80)]

# 이래되면 키가 기본값이기에 정렬할 때 키로 정렬한다. So>   ---------------------------------------------------??????????????????
print(f' jumsu 값 오름차순 정렬 : {sorted(jumsu.items(), key=lambda x:x[1])}')
                                                    #    > 정렬 기준이 인덱스 0번에서 1번으로 변경된다.

# value를 정렬할려고 하지만 서로 타입이 달라 정렬할 수 없다.
# print(f' dog 오름차순정렬 : {sorted(dog.values())}') 

#ex-정렬
n1=[1,4,5,9,2,6] # 가능
n2=['a','z','f'] # 가능
n3=[1,'a',4,'f'] # 불가 > 다른 타입들이 섞여있기때문
print(f'{sorted(n1)}')
print(f'{sorted(n2)}')
# print(f'{sorted(n3)}')
