# 출근 시간대 지하철 이용 현황 

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)

    result=[]
    max_num=-1
    max_station=''


    for row in data:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[10:15:2]) # row[10,12,14] : 오전 7,8,9시 승차
        result.append(row_sum)

        if row_sum > max_num:
            max_num = row_sum
            max_station= row[3] + '(' + row[1] + ')'
            
print(f'최대 승차 인원역: {max_station} {max_num:,}')
result.sort(reverse=True)

# 1행, 2행 그래프 그리기
# figure 생성
plt.figure(figsize=(10,4))

# 1행 그래프
ax1 = plt.subplot(1,2,1)
plt.title('10개 역의 승차 인원수', size=12)
plt.bar(range(10),result[0:10])
plt.ylabel('승창인원수')

# 2행 그래프
ax2 = plt.subplot(1,2,2, sharey=ax1) # sharey : y축 label 공유
plt.title('전체 역의 승차 인원수', size=12)
plt.bar(range(len(result)), result)

plt.suptitle('출근시간대 승차 인원 현황\n', size=20)
plt.tight_layout()
plt.show()