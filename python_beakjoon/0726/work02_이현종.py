import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import random

'''
구현 내용
ü 윷가락은 4개의 값을 저장할 수 있도록 sticks=	[0,	0,	0,	0] 형태로 구현
ü 윷을 던질 때 마다 랜덤하게 0,	1	사이의 값을 생성해서 sticks[]에 저장하고 점수를 계산
함(예:	sticks[i]	=	random.randint(0,	1))
ü 한 명의 점수가 먼저 20점 이상이면 게임은 바로 종료
ü ‘모’나 ‘윷’이 나온 경우, 이미 총 점수가 20점 이상이면 한 번 더 던지지 않음
ü 경기 시작은 어느 누구나 상관없음 >>> 그래서 일단 흥부 시작으로 시작
ü 게임이 종료되면 승패 결과를 화면에 출력하고 프로그램 종료
'''
# 흥부 = j[0], 놀부 = j[1]
j=[0,0]

sticks=[0,0,0,0]

a1= '흥부 {sticks}: 도 (1점)/(총 {j[0]})--->'
b1= '흥부 {sticks}: 도 (1점)/(총 {j[0]})--->'

# 흥부
def roll_a():
    while True:
        for i in range(4):
            sticks[i]=random.randint(0,	1)
        if sum(sticks)==3: # 도
            j[0] = j[0] + 1
            print(f"{'흥부 {sticks}: 도 (1점)/(총 {j[0]})--->':*<30}")
            print()
            break              
        
        elif sum(sticks)==2: # 개
            j[0] = j[0] + 2
            print('흥부 개!!')
            print()
            break

        elif sum(sticks)==1: # 걸
            j[0] = j[0] + 3
            print('흥부 걸!!!')
            print()
            break
            
        elif sum(sticks)==0: # 윷
            j[0] = j[0] + 4
            print('흥부 윳!!!!')
            print('한번 더!!!!')
            print()
            if j[0] >=20:
                break
            else :
                continue
            
        else:               # 모
            j[0] = j[0] + 5
            print('흥부 모!!!!!')
            print('한번 더!!!!!')
            print()
            if j[0] >=20:
                break
            else :
                continue
    print(j)


# 흥부 혼자 신나는 판
def roll_agg():
    while True:
        sum(sticks)==4
        print('흥부 모!!!!!')
        print('한번 더!!!!!')
        print()
        j[0] = j[0] + 5

        if j[0] >=20:
            break
        else :
            continue



# 놀부
def roll_b():
    while True:
        for i in range(4):
            sticks[i]=random.randint(0,	1)
        if sum(sticks)==3: # 도
            print('놀부 도!')
            print()
            j[1] = j[1] + 1
            break              
        
        elif sum(sticks)==2: # 개
            print('놀부 개!!')
            print()
            j[1] = j[1] + 2
            break

        elif sum(sticks)==1: # 걸
            print('놀부 걸!!!')
            print()
            j[1] = j[1] + 3
            break
            
        elif sum(sticks)==0: # 윷
            print('놀부 윳!!!!')
            print('한번 더!!!!')
            print()
            j[1] = j[1] + 4
            if j[1] >=20:
                break
            else :
                continue
        else:               # 모
            print('놀부 모!!!!!')
            print('한번 더!!!!!')
            print()
            j[1] = j[1] + 5
            if j[1] >=20:
                break
            else :
                continue
    print(j)
    
# '게임 시작'
while True:
    roll_a()
    if j[0] >=20:
        print('흥부 승!!!')
        break
    else:
        pass
    roll_b()
    if j[1] >=20:
        print('놀부 승!!!')
        break
    else:
        pass

