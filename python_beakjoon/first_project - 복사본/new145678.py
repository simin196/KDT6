import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 이건 최고온도와 최저온도를

file_name = 'temp4.xlsx'
data_new = pd.read_excel(file_name)

# 필요한 열만 선택
data_filtered = data_new[['일시', '지점명', '평균기온(°C)', '최고기온(°C)', '최저기온(°C)']]

# 서울, 대구, 인천, 부산의 데이터만 필터링
cities = ['Seoul', 'Daegu', 'Incheon', 'Busan']
data_cities = data_filtered[data_filtered['지점명'].isin(cities)]

# 도시별 데이터 그룹화
grouped_data = data_cities.groupby(['일시', '지점명']).mean().unstack()

# 그래프 그리기
fig, axs = plt.subplots(2, 2, figsize=(14, 9), sharex=True, sharey=True)

for ax, city in zip(axs.flat, cities):
    ax.plot(grouped_data.index, grouped_data['평균기온(°C)', city], label='Average Temperature', marker='o')
    ax.plot(grouped_data.index, grouped_data['최고기온(°C)', city], label='Max Temperature', linestyle='--', marker='x')
    ax.plot(grouped_data.index, grouped_data['최저기온(°C)', city], label='Min Temperature', linestyle=':', marker='v')
    ax.set_title(city)
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()