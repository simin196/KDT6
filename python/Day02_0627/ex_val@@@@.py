'''
변수와 메모리 관계 
 - 파이썬에서 사용하는 변수 -> 창조성 변수 (레퍼런스 변수)
 - 메모리 힙 영역에 저장된 데이터의 주소 확인
 -> 주소확인 내장함수 : id(key or 변수명 또는 데이터)
'''

age = 27
number = 27

# 데이터가 존재하는 주소 확인
print(id(age))
print(id(27))
print(id(number))


age = 100
print(id(age))
print(id(27))
print(id(100))
print(id(number))
id(100, 300, age) #>>>>???? id 함수는 변수 하나만 되는것인가?
