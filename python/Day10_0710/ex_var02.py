#--------------------------------------------------------------------------
# 함수와 변수 - 지역/전역 변수
#--------------------------------------------------------------------------
## 전역변수
persons=['Hong']
year=2024
gender={'H':'남자'}
## 사용자 정의 함수 
def add_person(name):
    global year  # global이 없으니 오류
    year += 1
    persons.append(name) # list는 그냥 크다란 장바구니 생각 >>> 오류 없음 >> 장바구니가 바뀌는게 아니니깐
    gender[name]={'여'} # 딕셔너리도 마찬가지 >>> 컬랙션 타입과 프리미트 타입의 차이

def remove_person(name):
    persons.remove(name)
    gender.pop(name) # 딕셔너리에서 지우는 메서드


## 함수 호출
print(f'persons=> {persons}')
print(f'persons=> {gender}')

add_person("Park")
print(f'persons=> {persons}')
print(f'persons=> {gender}')

remove_person("Park")
print(f'persons=> {persons}')
print(f'persons=> {gender}')