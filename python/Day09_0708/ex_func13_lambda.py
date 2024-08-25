#--------------------------------------------------------------------------
# 람다표현식 또는 람다함수
# - 1줄 함수, 익명 함수
# - 형식 : lambda 매개 변수 : 실행코드
# - 그럼 왜 쓰느냐? >>> 그거외에 쓸곳이 없다 쓰고 버릴거다.
# 함수는 많이 쓰기 때문에 정해서 사용하는데
# 람다는 이때만 쓰고 버리겠다.  
#--------------------------------------------------------------------------
names={1:'Kim', 2:'Adam', 3:'Zoo'}

# 정렬하기 => 내장함수 sorted() >> 결과를 list 반환
# 정렬 기본이 키로 정렬
result = sorted(names)
print('오름차순 정렬[key기준]', result) #>>>key로 정렬

# value로 정렬 => names.items() --> (1:'Kim'), (2:'Adam'), (3:'Zoo')
result = sorted(names.items(), key=lambda items:items[1]) # 여기 파란색 items는 변수 이기에 아무 변수 가져와도 된다.
print('오름차순 정렬[value기준]', result)

result = sorted('This is a test string form Andrew'.split())
print(result)

result = sorted('This is a test string form Andrew'.split(), key=str.lower)
print(result)

#map()와 lambda-----------------------------
data=[11,22,33,44]

# - 각 원소의 값에 곱하기 2해서 다시 리스트로 저장

# 1. 함수로 만들어 map에 적용 >>> 함수는 저장되어 다음에도 불러와 쓸 수 있다.
def multi2(value): return value*2

data2=list(map(multi2,data))
print(data2)

# 2. lambda로 하여 map에 적용 >> lambda는 이번에 한번만 쓰고 버림
data2=list(map(lambda a:a*2, data))
print(data2)