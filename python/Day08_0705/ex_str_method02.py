#--------------------------------------------------------------------------
# 문자열 전용의 함수 즉. 메서드(Method)
#--------------------------------------------------------------------------

# 문자열에서 좌우 여백 제거 메서드 -> strip(), lstrip(), rstrip() > 문자열 내부에 공백은 XX

# msg='Good Luck'
# data="      Happy New Year 2025!     "

# # 좌우 모든 공백 제거
# m1=msg.strip()
# print(f'원본 msg : {len(msg)}개 ---> 제거 m1 : {len(m1)}개')
# d1=data.strip()
# print(f'원본 msg : {len(data)}개 ---> 제거 m1 : {len(d1)}개')


# ## 이름을 입력받아 저장하세요
# name= input('이름 : ').strip()

# print(f'name : {name}')

# if len(name)>0:
#     name= input('이름 : ')
# else:
#     print('입력하지 않았습니다.')


## 입력받은 데이터에 따라 출력을 다르게 합니다.
# - input()함수 사용
# - [조건] 알파벳이면 ★, 숫자면 ♥, 나머지는 무시 <=== if문 사용
data=input ('알파벳, 숫자 또는 문자 1개 입력 : ').strip()

if 'a'<= data <='z' or 'A'<= data <='Z':
    print('★')
elif '0'<= data <='9':
    print('♥')