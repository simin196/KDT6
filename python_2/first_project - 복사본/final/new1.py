import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 이건 최고온도와 최저온도를

file_name = 'temp4.xlsx'
data_new = pd.read_excel(file_name)

data_filtered = data_new[['일시', '지점명', '평균기온(°C)', '최고기온(°C)', '최저기온(°C)']]

cities = ['Seoul', 'Daegu', 'Incheon', 'Busan']
data_cities = data_filtered[data_filtered['지점명'].isin(cities)]

grouped_data = data_cities.groupby(['일시', '지점명']).mean().unstack()

fig, axs = plt.subplots(2, 2, figsize=(14, 9), sharex=True, sharey=True)

for ax, city in zip(axs.flat, cities):
    ax.plot(grouped_data.index, grouped_data['평균기온(°C)', city], label='Average Temperature', marker='o', linewidth=2.5)
    ax.plot(grouped_data.index, grouped_data['최고기온(°C)', city], label='Max Temperature', linestyle='--', marker='x', linewidth=2.5)
    ax.plot(grouped_data.index, grouped_data['최저기온(°C)', city], label='Min Temperature', linestyle='-', marker='v', linewidth=2.5)
    ax.set_title(city)
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')
    ax.grid(True)

lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
fig.legend(lines[:3], labels[:3], loc='lower center', ncol=3, bbox_to_anchor=(0.5, -0.05))

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()