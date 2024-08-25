# 대구 산격3동 인구현황

import csv
import pandas

f= open('age.csv', encoding='euc_kr')
data= csv.reader(f)
header = next(data)

result = [] # 빈 리스트를 만들어서 하나씩 담을예정
            # 이러면 나중에 그래프만들때 따로 담을 필요없이 담아진다.
for row in data:
    if '산격3동' in row[0]: # '산격3동'이 포함된 자료만 출력
        for data in row[3:]: # 0~100세 이상까지 자료를 리스트에 추가
            result.append(data)
print(result)
f.close()


