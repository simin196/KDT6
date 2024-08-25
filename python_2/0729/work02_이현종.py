'''
n 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
n 출근 시간대: 07:00~08:59
n 사용 파일: subwaytime.csv	또는 subway.xls
- 07:00~07:59 하차: index[11],	08:00~08:59 하차: index	[13]
n 각 지하철 노선별 가장 많이 내리는 지하철 역 분석
Ø 1 호선, 2 호선, 3 호선, 4 호선, 5 호선, 6 호선, 7 호선
n 하차 인원은 1,000 단위로 콤마를 찍어서 구분할 것
n 7 개의 지하철 역을 막대 그래프로 표시
n Bar	chart 의 x 축은 (노선 +	지하철 역 이름)을 표시하고, y 축은 인원수를 표시
'''

'''
* 최대 하차인원
1 2 3 4 5 6 7호선 대상   index 11 13 합을 구해서 각 호선마다 정렬후 나열 
1호선따로 2호선따로 하는게 좋지 않을까?
각 호선마다 최대인원 찾고
'''
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

## 1호차
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    
    data1 = []
    for row in data:
        if '1호선' in row:
            data1.append(row)
    
    result1=[]
    max_num1=-1
    max_station1=''

    for row in data1:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[11:14:2]) # row[11,13] : 오전 7,8시 하차
        result1.append(row_sum)

        if row_sum > max_num1:
            max_num1 = row_sum
            max_station1 = row[3] 
    
    result1.sort(reverse=True)
    print(f'출근 시간대 1호선 최대 하차역: {max_station1}역, 하차인원: {max_num1:,}')
    
## 2호차
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    
    data2 = []
    for row in data:
        if '2호선' in row:
            data2.append(row)
    
    result2=[]
    max_num2=-1
    max_station2=''

    for row in data2:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[11:14:2]) # row[11,13] : 오전 7,8시 하차
        result2.append(row_sum)

        if row_sum > max_num2:
            max_num2 = row_sum
            max_station2 = row[3] 
    
    result2.sort(reverse=True)
    print(f'출근 시간대 2호선 최대 하차역: {max_station2}역, 하차인원: {max_num2:,}')
    
    
## 3호차
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    
    data3 = []
    for row in data:
        if '3호선' in row:
            data3.append(row)
    
    result3=[]
    max_num3=-1
    max_station3=''

    for row in data3:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[11:14:2]) # row[11,13] : 오전 7,8시 하차
        result3.append(row_sum)

        if row_sum > max_num3:
            max_num3 = row_sum
            max_station3 = row[3] 
    
    result3.sort(reverse=True)
    print(f'출근 시간대 3호선 최대 하차역: {max_station3}역, 하차인원: {max_num3:,}')


## 4호차
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    
    data4 = []
    for row in data:
        if '4호선' in row:
            data4.append(row)
    
    result4=[]
    max_num4=-1
    max_station4=''

    for row in data4:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[11:14:2]) # row[11,13] : 오전 7,8시 하차
        result4.append(row_sum)

        if row_sum > max_num4:
            max_num4 = row_sum
            max_station4 = row[3] 
    
    result4.sort(reverse=True)
    print(f'출근 시간대 4호선 최대 하차역: {max_station4}역, 하차인원: {max_num4:,}')
    
    
## 5호차
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    
    data5 = []
    for row in data:
        if '5호선' in row:
            data5.append(row)
    
    result5=[]
    max_num5=-1
    max_station5=''

    for row in data5:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[11:14:2]) # row[11,13] : 오전 7,8시 하차
        result5.append(row_sum)

        if row_sum > max_num5:
            max_num5 = row_sum
            max_station5 = row[3]
    
    result5.sort(reverse=True)
    print(f'출근 시간대 5호선 최대 하차역: {max_station5}역, 하차인원: {max_num5:,}')
    
    
## 6호차
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    
    data6 = []
    for row in data:
        if '6호선' in row:
            data6.append(row)
    
    result6=[]
    max_num6=-1
    max_station6=''

    for row in data6:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[11:14:2]) # row[11,13] : 오전 7,8시 하차
        result6.append(row_sum)

        if row_sum > max_num6:
            max_num6 = row_sum
            max_station6 = row[3] 
    
    result6.sort(reverse=True)
    print(f'출근 시간대 6호선 최대 하차역: {max_station6}역, 하차인원: {max_num6:,}')
    

## 7호차
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    
    data7 = []
    for row in data:
        if '7호선' in row:
            data7.append(row)
    
    result7=[]
    max_num7=-1
    max_station7=''

    for row in data7:
        row[4:]=map(int, row[4:])
        row_sum = sum(row[11:14:2]) # row[11,13] : 오전 7,8시 하차
        result7.append(row_sum)

        if row_sum > max_num7:
            max_num7 = row_sum
            max_station7 = row[3]
    
    result7.sort(reverse=True)
    print(f'출근 시간대 7호선 최대 하차역: {max_station7}역, 하차인원: {max_num7:,}')

a=[f'1호선 {max_station1}',f'2호선 {max_station2}',f'3호선 {max_station3}',f'4호선 {max_station4}',f'5호선 {max_station5}',f'6호선 {max_station6}',f'7호선 {max_station7}']
b=[max_num1,max_num2,max_num3,max_num4,max_num5,max_num6,max_num7]


plt.figure(figsize=(10,10))
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역', size=12)
plt.bar(a, b)
plt.xticks(a, rotation=80)
plt.tight_layout()
plt.show()
