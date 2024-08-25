# [12.5] --------------------------------------------------------------
# 표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다.
# 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤 
# 딕셔너리를 출력하는 프로그램을 만드세요. 
# input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.
# --------------------------------------------------------------
# [입력]
# health health_regen mana mana_regen
# 575.6 1.7 338.8 1.63
# [결과]
# {'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}

# [입력]
# health mana melee attack_speed magic_resistance
# 573.6 308.8 600 0.625 35.7
# [결과]
# {'health': 573.6, 'mana': 308.8, 'melee': 600.0, 'attack_speed': 0.625, 'magic_resistance': 35.7}
# --------------------------------------------------------------
keys=input("게임 능력라벨 입력 (예: health  health_regen ): ").split()
print(f'keys => {keys}')

values=input("게임 능력치 입력 (예: 575.6  1.7 ): ").split()
print(f'values => {values}')

# '능력치' ==> 실수타입 형변환
values=list(map(float, values))
print(f'values => {values}')

result = list(zip(keys, values))
print(f'result => {result}')

