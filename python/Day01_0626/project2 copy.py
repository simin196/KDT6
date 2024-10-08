#--------------------------------------------------------------------------
# 포켓몬 상성표
#--------------------------------------------------------------------------
'''

1. 본인이 알고 싶은 타입을 입력

2. 입력된 타입의 상성과 약점을 출력할것이다.
   타입을 하나만 가지는 포켓몬이 많지만 타입 2개 짜리도 있다
    > 2중 약점도 생각할것.
    > 거기에다가 약점 + 강점으로 인해 1배로 약점 상쇄된다.
    > 강점 + 강점은 1/4데미지가 들어간다. 
        > 이 부분은 빼도 좋으듯하다. 약점이 뭔지 강점이 뭔지만 알면 되기때매

●: 효과가 굉장함(2배 대미지를 입힌다)
◇: 한배 - ●△X제외하고 나머지
△: 효과가 별로다(대미지가 절반이 된다)
X: 효과가 없다(대미지가 아예 들어가지 않는다)

3. 기준 잡기
 1) 공격하는 기술에 따라서 할건지
 2) 공격받는 포켓몬의 타입을 할건지 근데 2번이 맞겠다 
   >>>2중 약점도 생각해야해서  

4. 타입은 
노말 불꽃 물 풀 전기 얼음 격투 독 땅 비행 에스퍼
 벌레 바위 고스트 드래곤 악 강철 페어리

tp=['노말', '불꽃' '물' '풀' '전기' '얼음' '격투' '독' '땅' '비행' '에스퍼' '벌레' '바위' '고스트' '드래곤' '악' '강철' '페어리']

1. 노말  
O - 격투 
△
X - 고스트
  
2. 불꽃  
O - 물, 땅, 바위
△ - 불꽃, 풀, 얼음, 벌레, 강철, 페어리 
X 
  
3. 물  
O - 풀, 전기
△ - 불꽃, 물, 얼음, 강철
X  
  
4. 풀  
O - 불꽃, 얼음, 독, 비행, 벌레 
△ - 물 풀 전기 땅 
X 
  
5. 전기  
O - 땅 
△ - 전기 비행 강철
X 
  
6. 얼음  
O - 불꽃 격투 바위 강철 
△ - 얼음
X 
  
7. 격투  
O - 비행 에스퍼 페어리
△ - 벌레 바위 악
X 
  
8. 독  
O - 땅 에스퍼 
△ - 풀 격투 독 벌레 페어리
X  

9. 땅  
O - 물 풀 얼음  
△ - 독 바위 
X - 전기
  
10. 비행  
O - 전기 얼음 바위 
△ - 풀 격투 벌레
X - 땅
  
11. 에스퍼  
O - 벌레 고스트 악
△ - 격투 에스퍼
X - 
  
12. 벌레
O - 불꽃 비행 바위 
△ - 풀 격투 땅
X - 
  
13. 바위  
O - 물 풀 격투 땅 강철 
△ - 노말 불꽃 독 비행
X - 
  
14. 고스트  
O - 고스트 악 
△ - 독 벌레 
X - 노말 격투

15. 드래곤  
O - 얼음 드래곤 페어리 
△ - 불꽃 물 풀 전기 
X - 
  
16. 악  
O - 격투 벌레 페어리 
△ - 고스트 악
X - 에스퍼
  
17. 철  
O - 불꽃 격투 땅  
△ - 노말 풀 얼음 비행 에스퍼 벌레 바위 드래곤 강철 페어리
X - 독
  
18.페어리  
O - 독 강철 
△ - 격투 벌레 악
X - 드래곤
'''
# 각 타입별로 변수로 변환
# 1. W >>> 약점
# 2. S >>> 효과 별고없음(강점)
# 3. N >>> 효과 없음


# 1. 노말  
normal =['노말',['격투'] ]
normal_n =['고스트']


# 2. 불꽃  
fire= ['불꽃',['물', '땅', '바위']]
fire_h= ['불꽃', '풀', '얼음', '벌레', '강철', '페어리']
  
# 3. 물  
water=['물',['풀', '전기']]
water_h=['불꽃', '물', '얼음', '강철']
  
# 4. 풀
grass=['풀',['불꽃', '얼음', '독', '비행', '벌레']]
grass_h= ['물', '풀', '전기', '땅'] 

# 5. 전기 
ele=['전기', ['땅']]
ele_h=['전기', '비행', '강철']
  
# 6. 얼음
ice=['얼음', ['불꽃', '격투', '바위', '강철']]
ice_h=['얼음']
  
# 7. 격투
fight=['격투',['비행', '에스퍼', '페어리']]
fight_h=['벌레', '바위', '악']
  
# 8. 독  
poi=['독',['땅', '에스퍼']]
poi_h=['풀', '격투', '독', '벌레', '페어리']

# 9. 땅 
land=['땅',['물', '풀', '얼음']]
land_h=['독', '바위']
land_n=['전기']
  
# 10. 비행
fly=['비행', ['전기', '얼음', '바위']]
fly_h=['풀', '격투', '벌레']
fly_n=['땅']
  
# 11. 에스퍼  
esper=['에스퍼',['벌레', '고스트', '악']]
esper_h=['격투', '에스퍼']

# 12. 벌레
worn=['벌레',['불꽃', '비행', '바위']]
worn_h=['풀', '격투', '땅']
  
# 13. 바위
rock=['바위',['물', '풀', '격투', '땅', '강철' ]]
rock_h=['노말', '불꽃', '독', '비행']
  
# 14. 고스트  
ghost=['고스트',['고스트', '악']]
ghost_h=['독', '벌레']
ghost_n=['노말', '격투']

# 15. 드래곤 
dragon=['드래곤',['얼음', '드래곤', '페어리']]
dragon_h=['불꽃', '물', '풀', '전기']
  
# 16. 악
bad=['악',['격투', '벌레', '페어리']]
bad_h=['고스트', '악']
bad_n=['에스퍼']
  
# 17. 강철  
iron=['강철',['불꽃', '격투', '땅']]
iron_h=['노말', '풀', '얼음', '비행', '에스퍼', '벌레', '바위', '드래곤', '강철', '페어리']
iron_n=['독']
  
# 18.페어리  
fairy=['페어리',['독', '강철']]
fairy_h=['격투', '벌레', '악']
fairy_n=['드래곤']

data= input('포켓몬의 타입을 적으세요. 2중 타입의 경우 : ').strip().split()

if len(data)>0:
    if '노말' in data:

    if '불꽃' in data:

    if '물' in data:

    if '풀' in data:

    if '전기' in data:

    if '얼음' in data:

    if '격투' in data:

    if '독' in data:

    if '땅' in data:

    if '비행' in data:

    if '에스퍼' in data:

    if '벌레' in data:

    if '바위' in data:

    if '고스트' in data:

    if '드래곤' in data:

    if '악' in data:

    if '강철' in data:

    if '페어리' in data:

else:
    print('잘못입력하였습니다.')



