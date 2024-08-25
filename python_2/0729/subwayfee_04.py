# 최대 무임 승차 비율 확인

import csv

f= open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)

max_rate = 0

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0: 	
        # 무임 승차(%) = (무임 승차 수 *100) / (유임 승차 수 + 무임 승차 수)
        rate = (row[6]*100) / (row[4]+row[6])
        if rate > max_rate: # 최대 무임 승차 비율을 찾아가는 과정
            max_rate = rate
            print(row, round(rate,2), '%') 
f.close()