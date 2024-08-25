'''
for 반복문 : 셀렉트 파일 


for [변수명] in [시퀀스 데이터(여러개를 담고있는 변수들)]:
    변수명을 사용한 실행코드 
     => 

주소참조?ㅇㅅㅇ???? 흠..........
프리미티 데이터 타입 
시퀀스 데이터는 뭐있는지 쭉 정리해보기
레인지? range

'''

nums=[11,22,33]
# for n in nums:
#     n=n * 100
    
#range : nums의 인덱스를 찾아야함
# for idx in range(len (nums)):
#     print(idx,nums[idx])
#     nums[idx]=nums[idx]*10
#     print(nums)

# result=enumerate(nums)
# print(f'result -> {result}, {type(result)}')
# print(list(result))

# for e in enumerate(nums):
#     nums[e[0]]=e[1]*100

# for idx, data in enumerate(nums): #패킹 packing으로 묶음
#     nums[idx]=data*100
#     print


# ----------------------------------------------

# 문자열 출력 형태 정렬
num = 1
print(f'{num:0>3}입니다.')
print(f'{num:<5}입니다.')
print(f'{num:*^10}입니다.')

num=f'{81}입니다'
print(f'123{num:^20}123')