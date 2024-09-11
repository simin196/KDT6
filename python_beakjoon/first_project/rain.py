import pandas as pd 
from tabulate import tabulate
import seaborn as sns
import koreanize_matplotlib
import matplotlib.pyplot as plt

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