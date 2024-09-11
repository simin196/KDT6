import pandas as pd 
from tabulate import tabulate
import seaborn as sns
import koreanize_matplotlib
import matplotlib.pyplot as plt

file_path = 'new_rain_from3to9.xlsx'
data = pd.read_excel(file_path)


# 컬럼 이름을 영어로 변경
data.columns = ['DateTime', 'Temperature', 'Rainfall', 'WindSpeed', 'Humidity', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM2.5']

# 데이터 구조를 이해하기 위해 처음 몇 행을 출력
data.head()

# 결측치를 앞의 값으로 채우기 (ffill) 및 강수량 결측치는 0.01로 채우기
data.fillna(method='ffill', inplace=True)
data['Rainfall'].fillna(0.01, inplace=True)

# 'DateTime' 컬럼을 datetime 형식으로 변환
data['DateTime'] = pd.to_datetime(data['DateTime'])

# 일별로 그룹화하여 각 컬럼의 평균값 계산
daily_data = data.resample('D', on='DateTime').mean().reset_index()

# 소수점 둘째 자리로 반올림
daily_data = daily_data.round(2)

# 월별로 그룹화하여 각 컬럼의 평균값 계산
monthly_data = daily_data.resample('M', on='DateTime').mean().reset_index()

# 필터링하여 4월부터 9월까지의 데이터만 포함
filtered_data = daily_data[daily_data['DateTime'].dt.month.isin([4, 5, 6, 7, 8, 9])]

# 필터링된 데이터를 월별로 그룹화하여 평균값 계산
monthly_data_filtered = filtered_data.resample('M', on='DateTime').mean().reset_index()

# 월 이름을 추출하여 레이블로 사용
monthly_data_filtered['Month'] = monthly_data_filtered['DateTime'].dt.strftime('%B')


# 서브플롯 생성 (2행 3열)
fig, axs = plt.subplots(2, 3, figsize=(18, 10), sharey=True)
fig.suptitle('4월부터 9월까지의 미세먼지 상황', fontsize=16)

# 각 월별로 서브플롯에 데이터 시각화
for i, month in enumerate(monthly_data_filtered['Month'].unique()):
    ax = axs[i // 3, i % 3]
    month_data = filtered_data[filtered_data['DateTime'].dt.strftime('%B') == month]
    ax.plot(month_data['DateTime'].dt.day, month_data['PM10'], label='PM10', marker='o')
    ax.plot(month_data['DateTime'].dt.day, month_data['PM2.5'], label='PM2.5', marker='o')
    
    # 강수량이 0.5를 초과하는 경우 해당 날짜에 점선 표시
    for j, row in month_data.iterrows():
        if row['Rainfall'] > 0.5:
            ax.axvline(x=row['DateTime'].day, color='blue', linestyle='-', linewidth=1)
    
    ax.set_title(month)
    ax.set_xlabel('Day')
    ax.grid(True)

# 첫 번째 서브플롯에만 범례 추가
axs[0, 0].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

july_13_data = data[(data['DateTime'].dt.month == 7) & (data['DateTime'].dt.day == 13)]
plt.figure(figsize=(10, 5))
plt.plot(july_13_data['DateTime'], july_13_data['PM10'], label='PM10', marker='o')
plt.plot(july_13_data['DateTime'], july_13_data['PM2.5'], label='PM2.5', marker='o')

# 강수량이 0.5를 초과하는 경우 해당 시간에 점선 표시
for j, row in july_13_data.iterrows():
    if row['Rainfall'] > 0.5:
        plt.axvline(x=row['DateTime'], color='blue', linestyle='-', linewidth=1)

# 제목과 라벨 추가
plt.title('July 13th')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
