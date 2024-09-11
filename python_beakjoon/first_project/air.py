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


print('4월')
air4=pd.read_excel('air_4.xls')
renew(air4)


print('5월')
air5=pd.read_excel('air_5.xls')
renew(air5)


print('6월')
air6=pd.read_excel('air_6.xls')
renew(air6)


print('7월')
air7=pd.read_excel('air_7.xls')
renew(air7)


print('8월')
air8=pd.read_excel('air_8.xls')
renew(air8)


print('9월')
air9=pd.read_excel('air_9.xls')
renew(air9)


#===========================================================================

