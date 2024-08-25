#----------------------------------------------------------------------------------------------------------------------
# if
#----------------------------------------------------------------------------------------------------------------------
'''
형식 
if 조건식(booling 형식으로): (보통은 True가 참이지만, not를 붙혀 False가 참으로 만들 수 있다.)
    [tap으로 드려쓰기(위 조건이 참일 경우 드려쓰기 한 부분의 식을 적용)] 
elif (else if 준말):
    위 조건이 참일 경우 해당식 적용
else (나머지) : 
    해당식 적용

if 조건식: 후
    그냥 아무 식이 없으면 오류발생
그래서 pass를 사용 >>> 지나간다.

continue와 pass차이
continue >> 윗 조건으로 올라가고 if에서는 잘 안쓴다.
pass >> 해당 코드가 없어 지나고 아래 코드로 넘어간다.
'''

# # ex)
# number=int(input())
# if number%2==0:
#     print('짝수입니다')
# else :
#     print('홀수입니다')

# ex) # 스플릿 후 map 사용해서 int로 치환 )완
# time=input('ex.02:00 : ').split(':')
# time=list(map(int,time)) #>>>>map을 하게되면 map type으로 변경되서 다시 list로 묶어줘야한다.
# t=time[1]
# if t == 0:
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.')  

# # 스플릿 사용 )완
# time=input('ex.02:00 : ').split(':')
# t=time[1]
# if t == '00':
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.')

# # 슬라이싱 )완
# time=input('ex.02:00 : ').split(':')
# if time[3:] == '00':
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.')

# # ex) 출력 90점이상은 a 60까지 d 나머지 f
# a=[85,100,67,53,94,73,42]
# for i in a:
#     if i>=90:
#         print(f'{i}점 : A')
#     elif i>=80:
#         print(f'{i}점 : B')
#     elif i>=70:
#         print(f'{i}점 : C')
#     elif i>=60:
#         print(f'{i}점 : D')
#     else:
#         print(f'{i}점 : F')

# ex) 조건1 각 점수들이 0에서 100점인지 판별하기
#     조건2 4과목 평균이 80점 이상이면 합격, 아니면 불합격 출력
a=[80,75,100,95]
b=[105,70,65,80]

# for c in a:
#     if 0<=c<=100: 
#         d=(a[0]+a[1]+a[2]+a[3])/4
#         if d>=80:
#             print('합격입니다.')
#         else:
#             print('불합격입니다.')
#     else:
#         print('잘못된 입력입니다.')

# if 0<=a[0]<=100 and 0<=a[1]<=100 and 0<=a[2]<=100 and 0<=a[3]<=100:
#     d= sum(a)/len(a)
#     if d>=80:
#         print(f'합격')
#     else:
#         print(f'불합격')
# else:
#     print('점수 오류')


#----------------------------------------------------------------------------------------------------------------------
# while
#----------------------------------------------------------------------------------------------------------------------
'''
형식

초기값 >> 있어야지 실행 조건문에 돌릴수있네ㅇㅅㅇ
while 실행 조건문:
    실행문 
    조건의 제어문

ex)
i=0
while i<100:
    실행문
    i = i+1 (=> i+=1)
'''

#ex)
# balance=13500
# while balance>=1350:
#     print(balance-1350)
#     balance=balance-1350

# i=0 
# while i<101:
#     if i%2==1:
#         print(i)
#     i=i+1
