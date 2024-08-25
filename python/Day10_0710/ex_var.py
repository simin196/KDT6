'''
함수와 변수

함수명 ==> 코드주소를 저장


지역 변수 (local variable)

전역 변수 (Global Variable)


'''
#----------------------------------
## 전역변수(Global Variable)
# - 파일(py) 내에 존재하며 모든 곳에서 사용 가능 
# - 프로그램 실행 시 메모리에 존재
# - 프로그램 종료 시 메모리에서 삭제
#----------------------------------
total = 100


#----------------------------------
## 지역 변수 (Local Variable)
# - 함수 내에 존재하며 함수에서만 사용 가능
# - 함수 실행 시 메모리에 존재
# - 함수 종료 시 메모리에서 삭제
#  History : 프로젝트를 할때 만드는 사람과 관리하는 사람이 다르거나 회사끼리 하기에 기능을 쪼개 합쳐야하기에
#----------------------------------

#--------------------------------------------------------------------------
# 함수 기능 : 정수를 덧셈한 후 결과를 변환하는 함수
# 함수 이름 : addInt
# 매개 변수 : 0개 ~ n개 즉, 가변인자   *nums
# 함수 결과 : 정수 result

def addInt (*nums):
    total=0
    for n in nums:
        total += n
    return total


def multiInt (*nums):
    total1=1
    for n in nums:
        total1 *= n
    return total1 + total


def multiInt2 (*nums):
    # 전역변수의 값을 변경할 경우 그냥 사용X
    global total # 글로벌 >> 이 경우 바깥 변수 변경 할 수 있다.
    for n in nums:
        total *= n
    return total


## 함수 호출------------------
result1= addInt(1)
print(f' result1 : {result1}') #내부에 total이라는 함수가 있다.

result2= multiInt(5)
print(f' result2 : {result2}') # 내부에 total이라는 함수가 없다. 함수 안에 변수가 없으면 밖에서 찾는다. 밖에도 없으면 죽는다. >>ERROR

result2= multiInt2(5)
print(f' result2 : {result2}') 

#------------------------------------------------

print(f'전 : total => {total}') 


