'''
대구광역시 전체 및 9개 구,군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군, 
군위군) 남녀 비율을 각각의 파이 차트로 구현하세요. (hw03.py)
- subplots를 이용하여 5x2 형태의 총 10개의 subplot을 파이 차트로 구현
- gender.csv 파일 사용
'''

''' 출력 
대구광역시 :	(남:1,162,046	여:1,205,137)
대구광역시 중구:	(남:44,349	여:48,310)
대구광역시 동구:	(남:168,160	여:175,088)
대구광역시 서구:	(남:81,083	여:82,276)
대구광역시 남구:	(남:65,312	여:71,581)
대구광역시 북구:	(남:206,403	여:210,039)
대구광역시 수성구:	(남:196,513	여:211,798)
대구광역시 달서구:	(남:256,966	여:267,318)
대구광역시 달성군:	(남:131,520	여:127,760)
대구광역시 군위군:	(남:11,740	여:10,967)

gender 3번이 pie그래프
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

city=['대구광역시','대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
     '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', '대구광역시 달서구',
     '대구광역시 달성군','대구광역시 군위군']

plt.figure(figsize=(5,10))

for i in range(1,11):
    f = open('gender.csv', encoding='euc_kr')
    data= csv.reader(f)
    population=[]
    male_count = 0 
    female_count = 0
    color =	['cornflowerblue','tomato']
    c=city[i-1]

    for row in data:
        if c in row[0]:
            male_count = int(row[104].replace(',',''))
            female_count = int(row[207].replace(',',''))
            print(f'{c} : (남 : {male_count:,}  여 : {female_count:,})')

            plt.subplot(5,2,i)
            population=[male_count, female_count]
            plt.pie(population, labels=['남','여'], autopct='%.1f%%', colors=color, startangle=90)
            plt.title(c)
            break
plt.suptitle('대구광역시 구별 남여 인구 비율')
plt.show()

