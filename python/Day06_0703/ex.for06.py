#--------------------------------------------------------------------------
# 제어문 - 반복문과 조건문 혼합
#--------------------------------------------------------------------------
# 메세지를 입력 받습니다.
# 알파벳 대문자인 경우 소문자로, 소문자인 경우 대문자로 
# 나머지는 그대로 되도록 출력하기

msg=input('메세지를 남겨주세요 : ')

# for m in msg:
#     if m.isupper==True :
#         print(m.lower(),end='')
#     elif m.islower==True : 
#         print(m.upper(),end='')
#     else:
#         print(m,end='')

#------------------------------------------------------
# 문자를 코드로 > ord(문자 한개) 
# 코드를 문자로 > chr(정수 코드값)
for m in msg:
    if 65<=ord(m)<97: #'A'<= m <= 'Z'
        print(chr(ord(m)+32), end='')
    elif 97<= ord(m) <=122: #'a'<= m <= 'z'
        print(chr(ord(m)-32), end='')
    else: 
        print(m, end='')

#>>>>>>>>>> 이렇게 바로 print를 넣게 되면 바로바로 나와 출력되고


# # 대문자 ---> 소문자
# print(chr(ord('A')+32))
    
# # 소문자 ----> 대문자
# print(chr(ord('a')-32))
