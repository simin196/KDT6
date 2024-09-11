### 미세먼지 데이터 확인
# 모듈 로딩
import pandas as pd 
from tabulate import tabulate

# dust.xlsx 불러오기
dust = pd.read_excel('dust.xlsx')

# 데이터 읽기 및 구조 확인
print(dust.head())
print(tabulate(dust.head(), headers='keys', tablefmt='pretty'))

print(dust.info())
print('------------------------------------------------------------------')

# 데이터 가공: 컬럼 이름 변경
dust.rename(columns={'날짜':'date','아황산가스':'so2','일산화탄소':'co','오존':'o3','이산화질소':'co2'}, inplace=True)
print(tabulate(dust.head(), headers='keys', tablefmt='psql'))

# 데이터 가공: 날짜 변경
dust['date']= dust['date'].str[:10]
print(tabulate(dust.head(), headers='keys', tablefmt='psql'))

#데이터 가공: 날짜(data) 자료형 변경
dust['date']=pd.to_datetime(dust['date'])
print(dust.dtypes)

#[‘date’]컬럼에서 년도, 월, 일을 추출하여 새로운 컬럼 생성
dust['year']=dust['date'].dt.year
dust['month']=dust['date'].dt.month
dust['day']=dust['date'].dt.day
print(dust.columns)

# 컬럼 순서 재정렬
dust=dust[['date','year','month','day', 'so2', 'co', 'o3', 'co2', 'PM10', 'PM2.5']]
print(dust.columns)
print('------------------------------------------------------------------')


### 데이터 전처리: 누락값(결측치)
#  데이터 누락값(결측치) 개수 확인
print(' 결측치 개수 확인하기 ')
print(dust.isna().sum()) # isnull() 동일

# 데이터에서 결측치를 포함하는 행 출력
print('결측치를 포함한 데이터 출력')
print(dust[dust.isna().any(axis=1)])
print('------------------------------------------------------------------')


##결측치 채우기
# 결측치의 이전값으로 결측치로 채움
print('결측치 채우기')
dust.ffill(inplace=True)
print(dust.isna().sum())

# 다시 확인
print(dust.iloc[132:134])

print('=====================================================================')

### 날씨 데이터 읽기 및 확인
#엑셀 파일 읽기
weather=pd.read_excel('weather.xlsx')
print(tabulate(weather.head(),headers='keys',tablefmt='psql'))

# 날씨 데이터 기본 정보 출력
print(weather.info())

#불필요한 컬럼 삭제 및 컬럼 이름을 영문으로 변경
weather.drop(['지점','지점명'], axis=1, inplace=True)
weather.columns=['date','temp','wind','rain','humidity']
print(tabulate(weather.head(),headers='keys',tablefmt='pretty'))

# weather['date']컬럼에서 시간 정보 삭제 후 데이터 타입 확인
weather['date']= pd.to_datetime(weather['date'].dt.date)
print(weather.info())
print(weather.head())
print('------------------------------------------------------------------')

## 전처리 : 결측치
# 결측치 확인
print('날씨 데이터 결측치 개수 확인하기')
print(weather.isna().sum())

print('날씨 데이터에서 결측치를 포함하여 행 출력')
print(weather[weather.isna().any(axis=1)])

# 결측치 채우기
weather.ffill(inplace=True)
print(weather.isna().sum())

# 이전과 값 비교
print(weather.iloc[[369,565,742]])
print('------------------------------------------------------------------')

## 강수량 데이터 변경
# 강수량 측정
print('강수량이 0인 항목을 0.01로 변경')
weather['rain'] = weather['rain'].replace(0,0.01)
print(weather['rain'].value_counts())
print('------------------------------------------------------------------')

# 두 데이터 크기 확인
print('dust, weather의 크기 확인')
print('dust.shape', dust.shape)
print('weather.shape', weather.shape)

# 미세먼지 데이터에서 공통 내용이 아닌 행 삭제
print(dust.iloc[740:])
print(weather.iloc[740:])
dust.drop(index=743, inplace=True)
print(dust.shape)
print('------------------------------------------------------------------')

# 데이터프레임 병합
print('dust, weather 데이터프레임 merge')
merged_df= pd.merge(dust, weather, on='date')
print(merged_df)
print()
print('------------------------------------------------------------------')

### 데이터 분석
# 상관계수 계산
pd.set_option('display.max_columns', None) # 전체 컬럼 출력
pd.set_option('display.max_rows', None) # 전체 행 출력
print(merged_df.corr())
print(merged_df.columns)

print('미세먼지(PM10)과 상관관계 분석')
corr = merged_df.corr()
pd.set_option('display.max_rows', None)
print(corr['PM10'].sort_values(ascending=False)) # 내림차순 정렬

import matplotlib.pyplot as plt

merged_df.hist(column=['so2', 'co', 'o3', 'co2', 'PM10', 'PM2.5', 'temp', 'wind', 'rain', 'humidity'],
               bins=50, figsize=(25,15))
plt.show()

import seaborn as sns
import koreanize_matplotlib

plt.figure(figsize=(15,10))
daygraph = sns.barplot(x='day', y='PM10', data=merged_df)
plt.title('날짜별 PM10 농도')
plt.show()

plt.figure(figsize=(15,10))
sns.heatmap(data=corr, annot=True, fmt='.2f', cmap='hot')
plt.show()


               