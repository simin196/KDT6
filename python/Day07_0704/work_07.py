#[22.9]
# a=['alpha','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India']
# b=[]
# b=[i for i in a if len(i)==5]
# print (b)

# #[22.10] ????????????????????????????
# # 2**ㅁ 이고 인덱스 1자리 와 (끝자리수-2)= 인덱스 자리숫자 는 지워야한다.
# a=input('점수를 입력하세요').split(' ')
# n1=list(map(int, a)) # [a a]
# print(n1)
# a1=n1[0]
# a2=n1[1]
# for b in range(a1, a2+1): # range (1, 10)
#     if n1.index(a1+1)==1 or n1.index(a2-1)==len(n1)-2 : 
#         continue
#     else:
#         print(2**b)

