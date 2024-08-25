import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

max_stations = []
max_numbers = []

for i in range(1, 8):
    with open('subwaytime.csv', encoding='utf-8-sig') as f:
        data = csv.reader(f)
        next(data)
        next(data)

        data_i = []
        for row in data:
            if f'{i}호선' in row:
                data_i.append(row)

        result_i = []
        max_num_i = -1
        max_station_i = ''

        for row in data_i:
            row[4:] = map(int, row[4:])
            row_sum = sum(row[11:14:2])  # row[11,13] : 오전 7, 8시 하차
            result_i.append(row_sum)

            if row_sum > max_num_i:
                max_num_i = row_sum
                max_station_i = row[3]

        result_i.sort(reverse=True)
        print(f'출근 시간대 {i}호선 최대 하차역: {max_station_i}역, 하차인원: {max_num_i:,}')

        max_stations.append(f'{i}호선 {max_station_i}')
        max_numbers.append(max_num_i)

plt.figure(figsize=(10, 10))
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역', size=12)
plt.bar(max_stations, max_numbers)
plt.xticks(max_stations, rotation=80)
plt.tight_layout()
plt.show()