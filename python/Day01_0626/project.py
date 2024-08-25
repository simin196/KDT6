#--------------------------------------------------------------------------
# 가위 바위 보
#--------------------------------------------------------------------------
'''
1. 일단 사용자가 뭘 낼건지 input

2. 랜덤으로 컴퓨터의 가위, 바위, 보 선정 > 딕셔너리로 바로가야할지 안미 그냥 바로되는지 확인

3. 실행
1 - 사용자가 낸거에 따라 결과를 낼것인가 @
2 - 승리 결과에 따른 조건을 낼것이가

4. 승리했다면 >>> 점수 1점 획득 후 재도전 여부
5. 비겼으면 >>> countine
6. 졋으면 패배. >>> break써서 멈추기

추가 적으로
7. 점수와 별개로 몇번 했는지
8. 이때까지 많이 올라간 사람은 몇번까지 했는지
'''
#------------------------------------------------------------------------------------
# 함수 기능 : 사용자가 맞는 답안을 썼느냐 확인
# 함수 이름 : uesr_check
# 매개 변수 : user
# 함수 결과 : True False
def uesr_check(user):
    if user=='가위' or user=='바위' or user=='보':
        return True
    else:
        return False
#---------------------------------------------------------    
# 함수 기능 : 사용자가 이겼을경우 계속할건지 안할건지 판별
# 함수 이름 : retry
# 매개 변수 : yn
# 함수 결과 : True False
def retry(yn):
    if yn=='yes' or yn=='ㅛ' or yn=='y' :
        return True
    else:
        return False



i=0
j=0
while True:
    user=input('가위, 바위, 보 중 하나를 적어주세요.').strip()
    print(f'유저 : {user}')

    import random
    li=['가위','바위','보']
    com=random.choice(li)
    print(f'컴퓨터 : {com}')
    
    
    if uesr_check(user):
        if user=='가위':
            if com=='가위':
                print('비겼다')
                continue
            elif com=='바위':
                print('졌다. 다음 기회에')
                i=0
                j=j+1
                break
            else:
                print('이겼다.')
                i=i+1
                j=j+1
                yn = input('계속하시겠습니까? yes,y로 입력해주세요')
                if retry(yn):
                    continue
                else:
                    break

        elif user=='바위':
            if com=='가위':
                print('이겼다')
                i=i+1
                j=j+1
                yn = input('계속하시겠습니까? yes,y로 입력해주세요')
                if retry(yn):
                    continue
                else:
                    break
            elif com=='바위':
                print('비겼다')
                continue
            else:
                print('졌다. 다음 기회에')
                i=0
                j=j+1
                break

        else:
            if com=='가위':
                print('졌다. 다음 기회에')
                i=0
                j=j+1
                break
            elif com=='바위':
                print('이겼다')
                i=i+1
                j=j+1
                yn = input('계속하시겠습니까? yes,y로 입력해주세요')
                if retry(yn):
                    continue
                else:
                    break
            else:
                print('비겼다')
                continue
    else:
        print('잘 못 입 력 하 셨 습 니 다.')
        continue
print(f'{i}점 획득하셨습니다. {j}번 하셨습니다.')

name= input('이름을 입력해주세요 : ').strip()
if 0<=len(name)<=6 :
    name = name
else :
    name = name[0]+name[1]+name[2]+name[3]+name[4]+name[5]

print(name)
a= [j,name]
rank_score = [[5,'홍길동'],[4,'이재용'],[3,'홀란드'],[2,'손흥민'],[1,'경대카리나']]
rank_score.append(a)
rank_score.sort(reverse=True)
del rank_score[5]
print(rank_score)
score=[]
name=[]
for rs in rank_score:
    score.append(rs[0])
    name.append(rs[1])
print(score)
print(name) 

name1=name[0]
j1=score[0]
name2=name[1]
j2=score[1]
name3=name[2]
j3=score[2]
name4=name[3]
j4=score[3]
name5=name[4]
j5=score[4]

str1 = f'{name1} {j1}번'
str2 = f'{name2} {j2}번'
str3 = f'{name3} {j3}번'
str4 = f'{name4} {j4}번'
str5 = f'{name5} {j5}번'

print(f'{"*":*^40}')
print(f'{"랭     킹":*^40}')
print(f'{"*":*^40}')
print(f'{str1:*^40}')
print(f'{str2:*^40}')
print(f'{str3:*^40}')
print(f'{str4:*^40}')
print(f'{str5:*^40}')
print(f'{"*":*^40}')
