#--------------------------------------------------------------------------
# 제어문 - while문
#--------------------------------------------------------------------------
num=10

while num>0:
    print(num) # 무한 반복  터미널에서 ctrl c누르면 강제 종료
    num=num-1 # 제한문을 만듬

# 리스트에 원소/요소 읽기
## while 반복문 : 개수
nums=[11,22,33]
cnt=0
while cnt<len(nums):
    print(cnt, nums[cnt])
    cnt=cnt+1

# 'Hello'문자열의 원소를 하나씩 출력하기
msg='Hello'
idx=0

while idx<len(msg):
    print(idx, msg[idx])
    idx=idx+1