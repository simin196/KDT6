import csv
import pandas

f= open('age.csv', encoding='euc_kr')
data= csv.reader(f)
    
header = next(data)

# row[0]: 행정구역
for row in data:
    if '산격3동' in row[0]: # '산격 3동'이 포함된 행의 row[0](행정구역)만 추출
        print(row)
f.close()


