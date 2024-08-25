# #[17.5]
# i=2 ; j=5
# while i<33 or j>0:
#     print(i, j)
#     i=i*2
#     j=j-1


#[17.6]
# money=int(input('돈 : '))
# while money>=1350:
#     money=money-1350
#     print(money)


#[18.5]
i=3
while i<=74 :
    print(i, end=' ')
    i=i+10
print()

# if 사용
i = 0
while True:
    if i % 10 == 3: 
        print(i, end=' ')
    if i>73:
        break
    i=i+1

#------------------------------------
# 0~73 사이의 숫자 중 3으로 끝나는 숫자 출력
# 3 13 23 33 43 53 63 73 => 10으로 나누었을때 나머지가 전부 3
i=0
while True:
    if i%10 != 3: 
        i=i+1 
        continue
    if i>73: break #i==74는 왜안됨?
    print(i, end=' ')
    i=i+1


#[18.6] 정수 두개 입력, 두 정수 사이 3으로 끝나지 않는 숫자 출력

# start, stop = map(int, input('정수 두개를 입력하세요').split())
# i=start 
# e=stop 
# while True:
#     if i%10 ==3:
#         i= i+1
#         continue
    
#     if i>e:
#         break
#     print(i, end=' ')
#     i= i+1

#[19] 넘기고 ㅋㅋㅋㅋ

# #[20.7]
# for i in range(1,101):
#     if i%2==0 and i%11==0:
#         print('FizzBuzz')
#     elif i%2==0:
#         print('Fizz')
#     elif i%11==0:
#         print('Buzz')
#     else:
#         print(i)

#[20.8]
# start, stop = map(int, input('정수 두개를 입력하세요').split())
# i=start 
# e=stop 
# for i in range(i,e+1):
#     if i%5==0 and i%7==0:
#         print('FizzBuzz')
#     elif i%5==0:
#         print('Fizz')
#     elif i%7==0:
#         print('Buzz')
#     else:
#         print(i)



dan=range(2,10)
## 구구단 전체 출력 > for문으로 >  for 한개로  >>> 네 그래서 for 말고 while로 했습니다.
# for d in dan: 
#     print(f'{d}단')
#     i = 1 # > 아 여기서 최솟값 정해졌고 
#     while i <= 9: 
#         print(f"{d} * {i} = {d * i}")
#         i = i + 1 # 여기서 조건식까지 가는 조건을 만들어서 올라가고있네 

# # 노동
# for d in dan:
#     print(f'{d}단')
#     print(f'{d} * 1 = {d*1}')
#     print(f'{d} * 2 = {d*2}')
#     print(f'{d} * 3 = {d*3}')
#     print(f'{d} * 4 = {d*4}')
#     print(f'{d} * 5 = {d*5}')
#     print(f'{d} * 6 = {d*6}')
#     print(f'{d} * 7 = {d*7}')
#     print(f'{d} * 8 = {d*8}')
#     print(f'{d} * 9 = {d*9}')



# ## 구구단을 2~5까지 가로로 쭉 그리고 다음으로 6~9까지 가로로 쭉

# dan=range(2,10)
# nums=range(1,10)
# totla=''
# a=
# for d in dan:
#     if 2<=d<=5:
#         print(f'{d}단')
#     for n in nums :  
#         print(f'{d} * {n} = {d*n:0>2}') 
       
#     print(sep='\n')

#------------------------------------------------

# for i in range(1,10):
#     for j in range(2, 6):
#         print(f'{j} * {i} = {i * j:<2}', end='     ')
#     print()
# print()
# for i in range(1,10):
#     for j in range(6, 10):
#         print(f'{j} * {i} = {i * j:<2}', end='     ')
#     print()

#------------------------------------------------------------------------
#별 찍기
  
