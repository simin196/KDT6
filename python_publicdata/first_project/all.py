import pandas as pd 
from tabulate import tabulate
import seaborn as sns
import koreanize_matplotlib
import matplotlib.pyplot as plt


def renew(data):
    data.rename(columns={'날짜':'date','아황산가스':'so2','일산화탄소':'co','오존':'o3','이산화질소':'co2'}, inplace=True)
    data['date']=data['date'].str[:10]
    data['date']=pd.to_datetime(data['date'])
    data['year']=data['date'].dt.year
    data['month']=data['date'].dt.month
    data['day']=data['date'].dt.day
    data=data[['date','year','month','day', 'so2', 'co', 'o3', 'co2', 'PM10', 'PM2.5']]
    data.ffill(inplace=True)
    print(data.columns)
    print()
    print(data.isna().sum())
    print()
    print(tabulate(data.head(), headers='keys', tablefmt='pretty'))

print('3월')
air3=pd.read_excel('air_3.xls')
renew(air3)


# print('4월')
# air4=pd.read_excel('air_4.xls')
# renew(air4)


# print('5월')
# air5=pd.read_excel('air_5.xls')
# renew(air5)


# print('6월')
# air6=pd.read_excel('air_6.xls')
# renew(air6)


# print('7월')
# air7=pd.read_excel('air_7.xls')
# renew(air7)


# print('8월')
# air8=pd.read_excel('air_8.xls')
# renew(air8)


# print('9월')
# air9=pd.read_excel('air_9.xls')
# renew(air9)


#===========================================================================


def renew(data):
    data.drop(['지점','지점명'], axis=1, inplace=True)
    data.columns=['date','temp','rain','humidity']
    data['date']= pd.to_datetime(data['date'].dt.date)
    data.ffill(inplace=True)
    data['rain'] = data['rain'].replace(0,0.01)
    data['rain'] = data['rain'].fillna(0.01)
    print(data['rain'].value_counts())
    print(data.columns)
    print()
    print(data.isna().sum())
    print()
    print(tabulate(data.head(), headers='keys', tablefmt='pretty'))

print('3월')
rain3=pd.read_excel('new_rain_3.xlsx')
renew(rain3)


# print('4월')
# rain4=pd.read_excel('new_rain_4.xlsx')
# renew(rain4)

# print('5월')
# rain5=pd.read_excel('new_rain_5.xlsx')
# renew(rain5)

# print('6월')
# rain6=pd.read_excel('new_rain_6.xlsx')
# renew(rain6)

# print('7월')
# rain7=pd.read_excel('new_rain_7.xlsx')
# renew(rain7)

# print('8월')
# rain8=pd.read_excel('new_rain_8.xlsx')
# renew(rain8)

# print('9월')
# rain9=pd.read_excel('new_rain_9.xlsx')
# renew(rain9)

#================================================================

print('rain.shape', rain3.shape)
print('air.shape', air3.shape)

all3_df= pd.merge(air3, rain3, on='date')
print(all3_df)