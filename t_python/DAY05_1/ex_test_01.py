# ----------------------------------------------
# [실습1] 글자를 입력 받습니다 ==> input()  -> str
#         입력 받은 글자의(a~z, A~Z) 코드값을 출력
#         합니다.
# ----------------------------------------------
# data=input("문자 입력 : ")

# if len(data) and ('a'<=data<='z' or 'A'<=data<='Z') :
#     print(f'{data}의 코드값 : {ord(data)}')
# else : 
#     print("1개의 알파벳 문자만 입력해야 합니다.\n입력된 데이터 확인하세요.")
    
# data="A"
# # ord(data[0])  # ord(data[1])   
# print( list(map(ord, data)) )

# ----------------------------------------------
# [실습1] 점수를 입력 받은 후 학점을 출력합니다. 
# - 학점: A+, A, A-, B+, B, B-, C+, C, C-, 
#         D+, D, D-, F
#  A+ : 96~100
#  A  : 95
#  A- : 90~94
# ----------------------------------------------
jumsu=75
grade=''

if jumsu<0 or jumsu>100:
    print(f'{jumsu}는 잘못 입력된 점수입니다.')
else:
    if jumsu>95: grade='A+'
    elif jumsu==95: grade='A'
    elif jumsu>=90: grade='A-'
    elif jumsu>85:  grade='B+'
    elif jumsu==85: grade='B'
    elif jumsu>=80: grade='B-'
    elif jumsu> 75: grade='C+'
    elif jumsu==75: grade='C'
    elif jumsu>=70: grade='C-'
    elif jumsu> 65: grade='D-'
    elif jumsu==65: grade='D'
    elif jumsu>=60: grade='D-'
    else: grade='F'
    print(f'{jumsu}는 {grade}학점입니다.')