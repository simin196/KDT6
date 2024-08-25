#--------------------------------------------------------------------------
# 사용자 정의 함수
#--------------------------------------------------------------------------
# 함수 기능 : 원하는 단의 구구단을 출력해주는 기능 함수
# 함수 이름 : gugudan 
# 매개 변수 : num
# 함수 결과 : None

def gugudan(num):
    for n in range(1,10):
        print(f'{num} * {n} = {num * n}')

#---------------------------------------------------
# 함수 기능 : 파일의 확장자를 반환해주는 기능 함수
# 함수 이름 : extract
# 매개 변수 : file_name
# 함수 결과 : 확장자 str

def extract(file_name):
    # result = file_name[file_name.rfind('.')+1 :]
    # return result
    return file_name[file_name.rfind('.')+1 :]

##---------------------
print(extract("abc.jpeg"))
gugudan(6)

