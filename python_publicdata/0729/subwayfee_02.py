# 전체 탑승 인원 대비 유임 승차 비율이 가장 높은 역은?

import csv

f= open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
print(header)

max_rate = 0
rate=0

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i]) # 4,5,6,7 컬럼 값을 정수로 변환, 계산을 위해서
    rate = row[4] / row[6] # [6]컬럼의 값이 0인 행 확인 용도 
                           # >> ZeroDivisionError: division by zero 
                           # >> [6]컬럼(무임승차)가 0인 역 존재
    if rate> max_rate:
        max_rate =rate
print(max_rate)
f.close()