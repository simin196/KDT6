#--------------------------------------------------------------------------
# 파일명을 확장자까지 입력 받아서 확인가능한 파일인지 검사
# - 파일 종류 : jpg, png, txt
# - 존재하는 경우 : '확인 가능함!'
# - 존재하지 않는 경우 : '확인 불가능한 파일입니다.'
#--------------------------------------------------------------------------

files=['jpg', 'png', 'txt']
filename=input('파일명을 입력하세요(예:a.txt) : ')

if filename[-3:] in files:
    print('확인 가능함!')
else:
    print('jpg, png, txt 파일만 확인 가능합니다. ')