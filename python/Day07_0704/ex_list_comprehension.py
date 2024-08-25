#--------------------------------------------------------------------------
# List/Set/Dict 자료형과 반복문, 조건부표현식 결합
# - 메모리 사용량 감소 & 속도 빠름
#--------------------------------------------------------------------------
# [실습1] A리스트의 데이터를 B리스트에 담기 
#      단, A리스트에서 짝수값은 3을 곱하고, 홀수 값은 그대로 B리스트에 담기

a=[1,2,3,4,5,6]
b=[]
for num in a:
    if num%2: # 나머지가 1이기에 참값이다. 0은 거짓값이기 때문
        b.append(num)
    else:
        b.append(num*3)
print(f'a=>{a} \n b=>{b}')

# 1. 모든 원소를 새로운 리스트에 담기

# c=[]
# for num in a:
#     c.append(num)
c= [num for num in a]                            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>????????????
print(f' 1. a=>{a} \n b=>{b}\n c=>{c}')

# 2. 짝수 데이터만 새로운 리스트 c에 담기
# c=[]
# for num in a:
#     if not num%2: c.append(num*3)
c=[num*3  for num in a if not num%2]
print(f' 2. a=>{a} \n b=>{b}\n c=>{c}')

# 3. 짝수 데이터는 3곱하고 홀수 데이터는 그대로 새로운 리스트 c에 담기
# c=[]
# for num in a:
#     if not num%2: c.append(num*3)
#     else : c.append(num)

c=[num*3 if not num%2 else num for num in a ]

print(f' 3. a=>{a} \n b=>{b}\n c=>{c}')