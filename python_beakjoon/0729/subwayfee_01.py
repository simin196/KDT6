# 대중교통 데이터 읽어오기

import csv
f= open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
print(header)
i =1
for row in data:
    print(row)
    if i > 5:
        break
    i += 1 
f.close()

# >>>> pandas에서 head()대신에 할 수 있는 방법