#--------------------------------------------------------------------------
# 형변환 / tpye casting(타입 캐스팅)
# - 자료형을 다른 종류의 자료형으로 변경
# - 종류 
#   * 자동/ 무식적 형변환 : 컴퓨터가 진행
#   * 수동/ 명시적 형변환 : 개발자가 진행
#--------------------------------------------------------------------------
age=20.7

# float > int 변환 : 다시 저장하지 않으면 형변환 결과 적용 X
print(age, int(age), type(age))

age = int(age) # 저장했기에 다음 age는 int로 변환
print(age, type(age))


# int > float 변환
age=float(age)
print(age, type(age)) # 정수를 실수로 바꾸었기에 'XX.0'으로 표현됨

# float > str 변환
age=str(age)
print(age, type(age))
