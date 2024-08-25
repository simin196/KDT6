#--------------------------------------------------------------------------
# 모듈 : 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은 것
#          여러개의 모듈 파일들이 존재
# 모듈 사용법 : import 모듈파일명 <--- 확장자 제외
#--------------------------------------------------------------------------

import random as rad #줄이더라도 알아볼수있게 

# 임의의 숫자를 생성해서 추출
# 임의의 숫자 10개 생성
# # -> random() : 0.0 <= ~ <= 1.0
# for cnt in range(10):  
#     print(int(rad.random() *10))

# -> randint(a,b) : a <= ~ <= b
for cnt in range(10):
    print(rad.randint(0,1))

#---------------------------------------------------------------------------
# 로또 프로그램을 만들어주세요
# - 1~45 범위에서 중복되지 안는 6개 추출
# - 반복 횟수 : 알 수 없음 >>> 중복뜨면 중복을 지워야하기 때문
#   >>> 무한 반복문
# - 종료 조건 : 중복 x , 6개 숫자 > list, set(중복제거 가능), dict(키를 주면 출력가능)  *제외 >>> tuple(수정할 수 없기에 좋지않다.)

# list사용 > 중복이있다면 조건문으로 만들어 빼준다
lotto=[0,0,0,0,0,0]
idx=0

while True:
    num = rad.randint(1,45)
    if num not in lotto:
        lotto[idx]= num
        idx=idx+1
    if idx==6: break

print(lotto)


#dict 사용
lotto={}
key=1
while len(lotto)<=6:
    num = rad.randint(1,45)
    if num not in lotto.values():
        lotto[key] = num
        key=key+1

print(lotto)

#set 사용 >>> 중복체크안해도됨
lotto=set()
key=1
while len(lotto)<6:
    num = rad.randint(1,45)
    num_set=set([num])
    lotto = lotto.union(num_set)
    
print(lotto)

#------------------------------------------------------------------------------
# set 타입에 add()메서드
lotto=set()
while len(lotto)<6 :
    num= rad.randint(1,45)
    lotto.add(num)
print(lotto)
     