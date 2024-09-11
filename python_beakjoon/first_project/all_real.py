import pandas as pd 
from tabulate import tabulate
import seaborn as sns
import koreanize_matplotlib
import matplotlib.pyplot as plt


def renew(data):
    data.rename(columns={'날짜':'date','아황산가스':'so2','일산화탄소':'co','오존':'o3','이산화질소':'co2'}, inplace=True)
    data['date']=pd.to_datetime(data['date'])
    data=data[['date', 'so2', 'co', 'o3', 'co2', 'PM10', 'PM2.5']]
    data.ffill(inplace=True)
    print(data.isna().sum())
    return data
    # print()
    # print(tabulate(data.head(), headers='keys', tablefmt='pretty'))

air3=pd.read_excel('air_3.xls')
print(air3.isna().sum())
print()
renew(air3)
print()
print(air3.isna().sum())

air4=pd.read_excel('air_4.xls')
renew(air4)
print(air4.isna().sum())

air5=pd.read_excel('air_5.xls')
renew(air5)
print(air5.isna().sum())

air6=pd.read_excel('air_6.xls')
renew(air6)
print(air6.isna().sum())

air7=pd.read_excel('air_7.xls')
renew(air7)
print(air7.isna().sum())

air8=pd.read_excel('air_8.xls')
renew(air8)
print(air8.isna().sum())

air9=pd.read_excel('air_9.xls')
renew(air9)
print(air9.isna().sum())


#===========================================================================


def renew(data):
    data.drop(['지점','지점명'], axis=1, inplace=True)
    data.columns=['date','temp','rain','humidity']
    data.ffill(inplace=True)
    data['rain'] = data['rain'].replace(0,0.01)
    data['rain'] = data['rain'].fillna(0.01)
    # print()
    # print(tabulate(data.head(), headers='keys', tablefmt='pretty'))


rain3=pd.read_excel('new_rain_3.xlsx')
renew(rain3)

rain4=pd.read_excel('new_rain_4.xlsx')
renew(rain4)

rain5=pd.read_excel('new_rain_5.xlsx')
renew(rain5)

rain6=pd.read_excel('new_rain_6.xlsx')
renew(rain6)

rain7=pd.read_excel('new_rain_7.xlsx')
renew(rain7)

rain8=pd.read_excel('new_rain_8.xlsx')
renew(rain8)

rain9=pd.read_excel('new_rain_9.xlsx')
renew(rain9)

#================================================================

print('3월')
all3_df= pd.merge(air3, rain3, on='date')
print(all3_df)

print('4월')
all4_df= pd.merge(air4, rain4, on='date')
print(all4_df)

print('5월')
all5_df= pd.merge(air5, rain5, on='date')
print(all5_df)

print('6월')
all6_df= pd.merge(air6, rain6, on='date')
print(all6_df)

print('7월')
all7_df= pd.merge(air7, rain7, on='date')
print(all7_df)

print('8월')
all8_df= pd.merge(air8, rain8, on='date')
print(all8_df)

print('9월')
all9_df= pd.merge(air9, rain9, on='date')
print(all9_df)
print(all9_df.isna().sum())