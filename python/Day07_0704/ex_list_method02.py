#--------------------------------------------------------------------------
# 리스트 전용의 함수 즉. 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
#--------------------------------------------------------------------------
# * 3 요소 추가 메서드 append(데이터)
# datas=[1,3,5]

# # 새로운 데이터 100 추가 : 제일 마지막 원소 추가 (-1로도 안되는 맨 끝자리는 append사용하면 좋다)
# datas.append(100)
# print(f'datas 개수 : {len(datas)}, {datas}')

# datas.append(100)
# print(f'datas 개수 : {len(datas)}, {datas}')

# # * 4 요소 추가 메서드 insert(인덱스, 데이터)
# datas.insert(0, 300)
# print(f'datas 개수 : {len(datas)}, {datas}')

# datas.insert(-1, 300)
# print(f'datas 개수 : {len(datas)}, {datas}')

#-----------------------------------------------------

# [실습] 임의의 정수 숫자 10개 저장하는 리스트 생성
## 쌉노가다ㅋ
# data=[]
# data.append(1)
# data.append(12)
# data.append(3)
# data.append(45)
# data.append(16)
# data.insert(0,111)
# data.insert(5,222)
# data.insert(7,333)
# data.insert(1,444)
# data.insert(0,555)
# print(data)

#--------------------
# - random 모듈
# - 빈리스트 생성
# - for 반복문
# import random as rad

# nums=[]
# for cnt in range(10):
#     n=rad.randint(1,50)
#     nums.append(n)
# print(f'nums => {nums}')

# # 변수 n을 바로 ()안에 집넣어도 된다.
# nums=[]
# for cnt in range(10):
#     nums.append(rad.randint(1,50))
# print(f'nums => {nums}')

#---------------------------------------------------------------------------------------

# * 4 요소 삭제 메서드 remove(데이터)
# 존재하지 않는 데이터를 삭제 시 ERROR 발생함! 
datas=[300,1,3,5,100,300,100]
print(f'datas 개수 : {len(datas)}, {datas}')

for cnt in range(datas.count(300)):
    datas.remove(300)
    print(f'datas 개수 : {len(datas)}, {datas}')