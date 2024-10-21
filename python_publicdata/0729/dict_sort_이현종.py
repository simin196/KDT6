data={'Seoul':['South	Korea','Asia',9655000],
      'Tokyo':['Japan','Asia',14110000],
      'Beijing':['China','Asia',21540000],  
      'London':['United Kingdom','Europe',14800000],    
      'Berlin':['Germany','Europe',3426000],  
      'Mexico City':['Mexico','America',21200000]}   

key = list(data.keys())

# ## 1 번
# print(list(data.keys())[1])
# print(list(data.values())[1])

# for i in range(6):
#     print(f'[{i+1}] {list(data.keys())[i]}: [{list(data.values())[i]}]')
# #------------------------------------------------------------------------------

## 2번
key.sort()
print(key)
print(data[key[1]])


for i in range(6):
    print(f'[{i+1}] {key[i]}: [{list(data.values())[i]}]')

# while True:
#     print('''
#     -----------------------------------------
#     1.	전체 데이터 출력		
#     2.	수도 이름 오름차순 출력											
#     3.	모든 도시의 인구수 내림차순 출력		
#     4.	특정 도시의 정보 출력		
#     5.	대륙별 인구수 계산 및 출력		
#     6.	프로그램 종료
#     -----------------------------------------
#     ''')
#     a=int(input('메뉴를 입력하세요:	'))


#     if a==1:
#         for i in range(5):
#             print(data)
#         print(data.keys[0])
#         continue
#     elif a==2:
#         print(data.sorted())
#     elif a==3:
#     elif a==4:
#     elif a==5:
#     elif a==6:
#     else:
#         print('잘못된 입력입니다.')
        

