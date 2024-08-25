#--------------------------------------------------------------------------
# 연산자 
#--------------------------------------------------------------------------

# [3] 논리 연산자
# 종류 : and or not
# 특징 : 여러개의 경우에 대한 결과를 바탕으로 결론 도출
# 1. and : 결과1 and 결과2 and 결과3
#          결과1,2,3모두 True인 경우 True가 됨

num1=8
num2=3

print(f'{num1}>0 and {num2}>0 : {num1>0 and num2>0}')
print(f'{num1}>0 and {num2}==0 : {num1>0 and num2==0}')

# 2. or : 결과1 or 결과2 or 결과3
#         결과1,2,3중 1개 이상 True인 경우 True가 됨

print(f'{num1}>0 or {num2}>0 : {num1>0 or num2>0}')
print(f'{num1}>0 or {num2}==0 : {num1>0 or num2==0}')
print(f'{num1}==0 or {num2}==0 : {num1==0 or num2==0}')

#
# 3. not : not 결과 
#          결과에 반대로 결론을 도출
#          True > False, False > True

print(f'not{num1}>0 : {not num1>0}')
print(f'not{num1}==0 : {not num1==0}')