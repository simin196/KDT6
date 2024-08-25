#--------------------------------------------------------------------------
# 리스트 전용의 함수 즉. 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
#--------------------------------------------------------------------------

import random as rad

datas=[11,22,33]
nums=datas

print(f'datas => {datas} \n nums => {nums}')

nums[0]='백'
print(f'datas => {datas} \n nums => {nums}')


# * 9 list 복사해주는 메서드 copy()
# 얕은 복사임!! ==>> 깊은 복사는 모듈 추가해줘야함
nums2=datas.copy()
nums2[0]="A"
print(f'datas => {datas} \n nums2 => {nums2}')
