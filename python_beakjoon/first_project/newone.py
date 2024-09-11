import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# NASA GISTEMP 데이터 URL
url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"

# 데이터 읽기
df = pd.read_csv(url, skiprows=1)

# 필요한 열 선택 및 이름 변경
df = df.rename(columns={'Year': '년도', 'J-D': '연평균기온'})

# 2000년도 이후의 데이터만 선택
df = df[df['년도'] >= 2000]

# 결측값 처리
df = df.dropna()

# 그래프 설정
plt.figure(figsize=(10, 5))
plt.plot(df['년도'], df['연평균기온'], marker='o', linestyle='-', color='b')

# 그래프 제목 및 축 레이블 설정
plt.title('2000년 이후 연도별 평균 지구 기온 변화', fontsize=15)
plt.xlabel('년도', fontsize=12)
plt.ylabel('연평균기온 (°C)', fontsize=12)
plt.grid(True)

# 그래프 보여주기
plt.show()