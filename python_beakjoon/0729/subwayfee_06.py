# 실습 : 유임 승차 비율이 50% 이하인 역

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f= open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
print(header)

min_rate = 100
min_row=[]
min_total_num=0

for row in data:
    for i in [4,6]:
        row[i] = int(row[i])
    total_count= row[4]+row[6] # 유임승차, 무임승차 데이터만 가져옴
    # 무임승차 인원이 없고, 총 승차인원이 1만명 이상
    if (row[6]!=0) and (total_count >=10000):
        rate = row[4] / total_count
        if rate <= 0.5:
            print(row, round(rate,2)) # 먼저 유임 승차 비율이 50% 이하인 역 출력 
            if rate < min_rate: # 비율이 가장 낮은 역 차출
                min_rate = rate
                min_row= row
                min_total_count= total_count
f.close()

print()
print(f'유임 승차 비율이 가장 적은역 : {min_row[3]}')
print(f"전체 인원 : {min_total_count:,}명,"
      f"유임승차인원 : {min_row[4]:,}명,"
      f"유임승차비율 : {round(min_rate*100,1)}%")

plt.title(min_row[3]+ '역 유,무임 승차 비율')
label=['유임승차','무임승차']
values=[min_row[4], min_row[6]]
plt.pie(values, labels=label, autopct='%.1f%%')
plt.legend(loc=2)
plt.show()