#--------------------------------------------------------------------------
# 제어문 - 반복문 중단 break
# - 중첩 반복문일 경우의 break 가장 가까이 있는 반복문만 종료
#--------------------------------------------------------------------------

## 단의 숫자 만큼만 구구단을 출력하세요
# ex) 2단이면 2*2까지
#     3단이면 3*3까지

dan=int(input('출력을 원하는 단입력 : '))
# isBreak=False

# for d in range(2,10): 
#     print(f'\n[{d}단]', end=' ')
#     for n in range(1,10): 
#         print(f'{d} * {n} = {d*n:2}', end=' ')  #정렬은 기본은 오른쪽이다 , 왼쪽으로 정렬하는것을 원하면 <을 찍어주면된다.
#         if n==d: 
#             isBreak= True #안에 break가 걸렸다고 해도 밖에 걸린건 아니다. 
#             break
#     print('outer for')
#     if isBreak : break


#Break를 안쓰고
# for d in range(2, dan+1):
#     print(f'\n[{d}단]', end=' ')
#     for n in range(1,d+1):
#         print(f'{d} * {n} = {d*n:2}', end=' ')


for d in range(2,10): 
    print(f'\n[{d}단]', end=' ')
    for n in range(1,10): 
        print(f'{d} * {n} = {d*n:>2}', end=' ') 
        if n==d: break
    if d==dan : break

#>>> 이 식의 경우 d와 n과 dan이 동시에 끝나기에 따로 isBreak가 필요없다.