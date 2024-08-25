#--------------------------------------------------------------------------
# 연산자 - 격체비교연산자 
# ** 객체
#    힙 영역에 존재하는 데이터 즉, 저장된 데이터
#    클래스를 기반으로 저장됨
#--------------------------------------------------------------------------

num1=10
num2 = num1

# 두개의 변수가 동일한 객체를 저장하고 있느지 확인
# 그 연산자 => 객체비교연산자
print(f'{num1} is {num2} : {num1 is num2}')
print(f' num1 id : {id(num1)} ')
print(f' num2 id : {id(num2)} ')

num2= 10.0
print(f'{num1} is {num2} : {num1 is num2}') # >> is 연산자는 같은 값(id)인지 확인하는 연산자
print(f' num1 id : {id(num1)} ')
print(f' num2 id : {id(num2)} ') # num1 과 num2는 다른 객체를 저장 중

# 비교연산자 : 크기 비교
print(f'{num1} == {num2} : {num1 == num2}') # 각 객체의 값은 같다
print('--------------------------------------------------')
num3=int(num2)
print(f'{num1} is {num3} : {num1 is num3}')
print(f' num1 id : {id(num1)} ')
print(f' num3 id : {id(num3)} ')

num1='Hello'
num2='hello'
# >>> 대소문자 구분되는지 확인
print(f'{num1} is {num2} : {num1 is num2}')
print(f' num1 id : {id(num1)} ')
print(f' num2 id : {id(num2)} ')
print(f'{num1} == {num2} : {num1 == num2}')
