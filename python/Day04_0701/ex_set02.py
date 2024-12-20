#--------------------------------------------------------------------------
# set 자료형 살펴보기
# - 연산자  집합 개념으로 가져가야한다. 
#--------------------------------------------------------------------------
d1= {1,3,5,7}
d2={1,2,3,4,6,8}

# set은 메서드 or 다른 연산자 (| & -) 사용
# 덧셈 연산 ==> 합집합
# print(d1+d2) > 지원하지 않음 
print(d1.union(d2), d1 | d2) # 중복은 제거한다.

# 공통 원소 --> 교집합
print(d1.intersection(d2), d1 & d2)

# 집합에서 공통 원소 제외한 나머지 ==> 차집합
print(d2.difference(d1), d2-d1)