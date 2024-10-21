import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# NOAA 해수면 상승 데이터 URL
url = "https://datahub.io/core/sea-level-rise/r/epa-sea-level_csv.csv"

# 데이터 읽기
df = pd.read_csv(url)

# 필요한 열 선택 및 이름 변경
df = df.rename(columns={'Year': '년도', 'CSIRO Adjusted Sea Level': '해수면_상승_레벨'})

# 2000년도 이후의 데이터만 선택
df = df[df['년도'] >= 2000]

# 결측값 처리
df = df.dropna()

# 그래프 설정
plt.figure(figsize=(10, 5))
plt.plot(df['년도'], df['해수면_상승_레벨'], marker='o', linestyle='-', color='b')

# 그래프 제목 및 축 레이블 설정
plt.title('2000년 이후 연도별 해수면 상승', fontsize=15)
plt.xlabel('년도', fontsize=12)
plt.ylabel('해수면 상승 (인치)', fontsize=12)
plt.grid(True)

# 그래프 보여주기
plt.show()