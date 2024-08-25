# -------------------------------------------------------
#  입력 & 출력 실습
# -------------------------------------------------------
# [실습1] 데이터 저장 및 변수 생성 그리고 출력
# - 생년월일
# - 띠 (용,범...) : chinese_zodiac
# - 혈액형
# - 출력형태
#   나는 0000년 00월 00일 000띠입니다
#   혈액형은 ____ 0형입니다
# ------------------------------------------------------- 
# 데이터 저장 
b_year='2024'
b_month='01'
b_day='01'
blood='A'
c_zodiac='용띠'

# 출력
print('나는', b_year,'년', b_month,'월', b_day, '일', c_zodiac,'띠 입니다.')

print(f'나는 {b_year}년 {b_month}월 {b_day}일 {c_zodiac}띠 입니다.')
print(f'혈액형은 소심한 {blood}형 입니다.')
print('혈액형은 소심한 %s형 입니다.' %blood)


# [실습2] 입력 받은 데이터 저장 단, 파일로 저장 ------------
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고 싶은 나라
# ------------------------------------------------------- 
season=input("좋아하는 계절 : ")
nara=input("좋아하는 나라 : ")
nara2=input("여행가고 싶은 나라: ")

FILENAME='info.txt'
f=open(FILENAME, mode='w', encoding='utf-8')

# f.write(season)
# f.write('\n')   # 줄바꿈 문자 
# f.write(nara)
# f.write('\n')   # 줄바꿈 문자
# f.write(nara2)
print(f'좋아하는 계절       : {season}', file=f)
print(f'좋아하는 나라       : {nara}',   file=f)
print(f'여행가고 싶은 나라  : {nara2}',  file=f, end='')

f.close()

