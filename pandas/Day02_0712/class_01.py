#--------------------------------------------------------------------------
# 클래스 (Class)
# - 객체지향언어(OOP)에서 데이터를 정의하는 자료형
# - 데이터를 정의할 수 있는 데이터가 가진 속성과 기능 명시
# - 구성요소 : 속성/attribute/field + 기능/method
#--------------------------------------------------------------------------

# 클래스 정의 >> 햄버거를 나타내는 클래스
# 클래스 이름 >> 버거
# 클래스 속성 >> 번, 패티, 야채 @경우에 따라 추가 가능 치즈
# 클래스 기능 >> - (없으면 안 넣어도 됨), 햄버거 설명 기능
class Bugger:

    # 힙 영역에 객체 생성 시 속성값 저장 기능 >>>>>>>>>>>?????????? self 뒤에 순서 지켜야 하는지
    # init > 초기화 준말
    def __init__(self, bread, patty, veg, kind) :
        self.bread=bread
        self.patty=patty 
        self.veg=veg
        self.kind=kind

    # 클래스의 기능, 즉 메서드 (함수를 만드는 것처럼) # self에는 객체의 메모리 주소가 저장된다.
    def printInfo(self):
        print(f'브랜드 종류 : {self.kind}')
        print(f'빵 종류 : {self.bread}')
        print(f'패티 종류 : {self.patty}')
        print(f'야채 종류 : {self.veg}')

    
    # 속셩을 변경하거나 읽어오는 메서드 ==>  getter/setter 메서드
    def get_bread(self):
        return self.bread
    
    def set_bread(self, bread):
        self.bread=bread


## 객체 생성
# 불고기 버거 객체생성
bugger1=Bugger('브리오슈','불고기','양상추 양파 토마토','롯데리아')
bugger2=Bugger('참깨빵','쇠고기 패티','치즈 양상추 양파 토마토','맥도날드')

# 버거 정보확인
bugger1.printInfo()

# 속성 읽는 방법 : (1) 직접 접근 읽기 (2)간접 접근 읽기 - getter 메서드 사용
print(bugger1.bread, bugger1.get_bread)

# 속성 변경 방법 : (1) 직접 접근 읽기 (2)간접 접근 읽기 - setter 메서드 사용
bugger1.bread='들깨빵'
bugger1.set_bread('올리브빵')
bugger2.printInfo()

##---------------------------------------------------------------------------------
# if 공통으로 쓰는 속성이 있는경우
# 맥도날드에서 메뉴를 주문하다면??
class Bugger:
    
    kind = '맥도날드'

    
    def __init__(self,bread,patty,veg) : #(인스턴스 속성)
        self.bread=bread
        self.patty=patty
        self.veg=veg
        
        # self.kind=kind 밖으로 뺐다

    def printInfo(self):
        print(f'브랜드 종류 : {self.kind}')
        print(f'빵 종류 : {self.bread}')
        print(f'패티 종류 : {self.patty}')
        print(f'야채 종류 : {self.veg}')

## 객체 생성
# 불고기 버거 객체생성
bugger1=Bugger('브리오슈','불고기','양상추 양파 토마토')
bugger2=Bugger('참깨빵','쇠고기 패티','치즈 양상추 양파 토마토')

# 버거 정보확인
bugger1.printInfo()
bugger2.printInfo()