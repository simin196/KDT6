#--------------------------------------------------------------------------
# 리스트 전용의 함수 즉. 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
#--------------------------------------------------------------------------
# * 5 요소 순서 제어 메서드 reverse()
import random as rad\

rad.seed(3) # 동일한 랜덤 숫자 추출을 위한 기준점
datas=[]
for _ in range(10):
    datas.append(rad.randint(1,30))

print(f'{len(datas)}개, {datas}')

# 0번 ->  -1으로 -1번 -> 0번으로 위치 변경
datas.reverse()
print(f'{len(datas)}개, {datas}')

# * 6 요소의 크기를 비교해서 정렬해주는 메서드 sort()
# - 기본정렬 : 오름차순 즉, 작은 데이터 부터 큰 데이터 순서로
datas.sort()
print(f'{len(datas)}개, {datas}')

# - 내림차순 즉, 작은 데이터 부터 큰 데이터 순서로
datas.sort(reverse=True)
print(f'{len(datas)}개, {datas}')

# * 7 리스트에서 요소를 꺼내는 메서드 pop()
# - 리스트에서 요소가 삭제됨
value= datas.pop() # 제일 마지막 원소/요소
print(f'value: {value} - {len(datas)}개, {datas}')

value= datas.pop(0) # 특정 인덱스의 원소/요소 꺼내기
print(f'value: {value} - {len(datas)}개, {datas}')

# * 8 리스트 확장시켜주는 메서드 extend()
datas.extend([11,22,33])
print(f'{len(datas)}개, {datas}')

datas.extend((555,777)) 
print(f'{len(datas)}개, {datas}')

datas.extend('Good Luck') 
print(f'{len(datas)}개, {datas}')

datas.extend({555,777,555,777}) 
print(f'{len(datas)}개, {datas}') #set안에 중복은 지워주고 들어간다.

datas.extend({'name':'홍길동', 'age':12}) 
print(f'{len(datas)}개, {datas}')

# * 8 도든 원소 삭제 메서드 clear()
datas.clear()
print(f'{len(datas)}개, {datas}')
