#--------------------------------------------------------------------------
# 입력 & 출력 실습
#--------------------------------------------------------------------------
# [실습1] 데이터 저장 및 변수 생성 그리고 출력
# - 생년월일
# - 띠(용, 범,...)
# - 혈액형
# - 출력형태
#   0000년 00월 00일 000띠입니다.
#   혈액형은 _____형입니다.
#--------------------------------------------------------------------------
brith=input('생년월일ex(0000년 00월 00일) : ')
c_zodiac=input('띠 : ')
B_type=input('혈액형 : ')

print(f'{brith} {c_zodiac}띠입니다. \n 혈액형은 {B_type}형 입니다.', )

#--------------------------------------------------------------------------





# [실습2] 입력 받은 데이터 저장 단, 파일로 저장 ------------------------------
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고 싶은 나라 
#--------------------------------------------------------------------------
season=input('좋아하는 계절을 입력하세요 : ')
country=input('좋아하는 나라를 입력하세요 : ')
trevel=input('여행가고 싶은 나라를 입력하세요 : ')

FILENAME= 'info.txt'

f=open(FILENAME, mode='w', encoding='utf-8')

# f.write(season)
# f.write('\n')
# f.write(country)
# f.write('\n')
# f.write(trevel)
# f.write('\n')

print(f'좋아하는 계절 : {season}', file=f) 
      
print(f'좋아하는 나라 : {country}', file=f)

print(f'여행가고 싶은 나라  : {trevel}', file=f, end='') # end를 써야 밑에 칸으로 안넘어간다.

f.close()