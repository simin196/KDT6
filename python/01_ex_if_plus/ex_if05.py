#------------------------------------------------------------------------------------------------------------------------
# 숫자를 입력 받아서 0이상 큰 숫자라면 해당 숫자가 홀수인지 짝수인지 검사를 하고, 0미만이면 '잘못된 숫자'라고 출력해주세요
#------------------------------------------------------------------------------------------------------------------------

data=input('숫자 하나 입력하세요 : ')


if len(data)==1:
    if '0'<=data<='9':
        n1=int(data)
        if n1>=0:
            print('짝수') if n1%2==0 else print('홀수')
        else:
            print('잘못된 숫자')
    else:
        print('숫자만 입력 가능합니다.')
else: 
    print('입력된 것이 없거나 2개 이상을 입력했습니다.')