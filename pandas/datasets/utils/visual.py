#------------------------
# 시각화 관련함수들 존재하는 모듈
#------------------------
# 함수 기능 :  버전체크 후 출력 기능
# 함수 이름 : check_version
# 매개 변수 : None
# 함수 결과 : None
#----------------------------
def check_version():
    import matplotlib
    print(f'matplotlib : v{matplotlib.__version__}')