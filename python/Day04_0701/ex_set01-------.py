#--------------------------------------------------------------------------
# set 자료형 살펴보기
# - 여러 가지 종류의 여러 개 데이터를 저장
# - 단, 중복은 안됨!
# - 컬렉션 타입의 데이터 저장 시 Tuple가능
# - 형태 : {데이터1, 데이터2, ..., 데이터n}
#--------------------------------------------------------------------------
##set 생성

data=[] # list
data=() # tuple
data={} # key:value를 넣으면 dict
data=set()

print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

# 여러개 데이터 저장한 set
data={10, 30, 20, 90, 400, 600, 51, 22}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')


data={9.34, 'Alppe', 10, True, '10'}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

# data={1,2,3,[1,2,3]}
data={1,2,3,(1,2,3)}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

data={1,2,3,(1)} #그냥 (1)은 그냥 1이기에 중복되어 밖에있는 1과 중복
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

data={1,2,3,(1,)[0]} 
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

data={1,2,3,(1,)} 
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

# data={1,2,3, {1:100}} dict는 사용 불가
# print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

#set() 내장함수
data= {1,2,3}  # ===> set([1,2,3])
data= set() #Empty Set #생성자??????????
data= set({1,2})

#다양한 타입 ---> set 변환, 중복 제거
data= set([1,2,1,2,3])
data= set('Good') # 'o'가 중복이라 'o' 중복 지우고 표시
print(data)
data= set({'name' : '홍길동', 'age':12}) #key만 표시
print(data)
print({'name' : '홍길동', 'age':12})
data= list('Good') # 반면 list는 중복이라도 있는 그대로 표시
print(data)
