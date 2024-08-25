#-----------------------------------------------------------------------------
# Serise/DataFrame에서 사용되는 사용자 정의 함수들
#-----------------------------------------------------------------------------
# 함수기능 : DataFrame의 기본정보와 속성 확인 기능
# 함수이름 : checkDataFrame
# 매개변수 : DataFrame 인스터스 변수명. DataFrame 인스턴스 이름
# 반환값/리터값 : 없음
# >>> 이런걸 독스트링?? 이라고 한다.
#-----------------------------------------------------------------------------
def checkDataFrame(object, name):
    print(f'\n[{name}]')
    object.info()
    print(f'[Index] : {object.index}')
    print(f'[columns] : {object.columns}')
    print(f'[ndim] : {object.ndim}')
    

