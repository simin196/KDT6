# 승하차 인원이 가장 많은 역은?

import csv

max= [0]*4	# [0]:최대 유임승차, [1]:최대 유임하차, [2]:최대 무임승차, [3]:최대 무임하차
max_station= ['']*4 
label=['유임승차','유임하차','무임승차','무임하차']

# with 구문: 자동으로 파일을 close()시킴
with open('subwayfee.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)
    
    #data 컬럼 인덱스
    # 0 : 사용월    # 1 : 호선명
    # 2 : 역ID      # 3 : 지하철역
    # 4 : 유임승차   # 5 : 유임하차
    # 6 : 무임승차   # 7 : 무임하차

    for row in data:
        for i in range(4,8):
            row[i]= int(row[i])

            	# 원본데이터의 컬럼 (인덱스-4) -> max리스트의 인덱스
            if row[i] > max[i-4]:
                max[i-4] = row[i]

                max_station[i-4] = row[3] + ' ' + row[1]

for i in range(4):
    print(f'{label[i]}: {max_station[i]} {max[i]:,}명')