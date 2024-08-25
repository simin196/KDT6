# 연산자 (4칙연산자 : + - * /)와 숫자 2개 입력받기 
# - 입력된 연사자에 따라 계산 결과 저장
# - 예 입력 : + 10 3 출력 13

num = input('연사자(+,-,*,/)와 숫자 두개를 적으시오 예) + 10 3 : ').split(' ')
if num[0]=='+':
    print(f'{int(num[1])+int(num[2])}')
elif num[0]=='-':
    if int(num[1])>=int(num[2]):
        print(f'{int(num[1])-int(num[2])}')
    else :
        print(f'{int(num[2])-int(num[1])}')
elif num[0]=='*':
    print(f'{int(num[1])*int(num[2])}')
else :
    print(f'{int(num[1])/int(num[2])}')
