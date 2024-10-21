import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

## 일단 표는 뒤에 생각하고
# 마지막에 했는거랑 다름 ㅋㅅㅋ 앜ㅋㅋㅋㅋㅋㅋㅋ
# 입력순서 1. 시작 연도  2. 마지막 연도  3. 측정할 달
# 출력되어야하는거 >>> 1. 시작 부터 마지막 까지 측정할 달의 최저 기온평균 사이 년도 별로 촤르르
#                     2. 최고 기온 촤르르
# and 마지막으로 표 생성


def draw_two_plots(title, x_data, max_temp_list1, label_y1, max_temp_list2, label_y2):

    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10,4))
    plt.plot(x_data, max_temp_list1, marker='s', markersize=6, color='b', label=label_y1)
    plt.plot(x_data, max_temp_list2, marker='s', markersize=6, color='r', label=label_y2)
    plt.xticks(x_data)

    plt.title(title)
    plt.legend()
    plt.show()

def main():
    start_year= int(input('시작 연도를 입력하세요 : '))
    last_year=int(input('마지막 연도를 입력하세요 : '))
    search_month = int(input(" 비교할 월을 입력하세요 : "))

    weather_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

    first_decade=start_year
    second_decade=last_year

    min_temp_list=[0]*(last_year-start_year+1)
    max_temp_list=[0]*(last_year-start_year+1)

    for year in range(start_year,last_year+1):
        min_temp_df=weather_df[(weather_df['날짜'].dt.year== year )&(weather_df['날짜'].dt.month==search_month)]
        min_temp_list[year - start_year] = round(min_temp_df['최저기온'].mean(),1)

        max_temp_df=weather_df[(weather_df['날짜'].dt.year== year )&(weather_df['날짜'].dt.month==search_month)]
        max_temp_list[year - start_year] = round(max_temp_df['최고기온'].mean(),1)

    print(f'{first_decade}년부터 {second_decade}년까지 {search_month}월의 최저 기온 평균 : {min_temp_list}')
    print(f'{first_decade}년부터 {second_decade}년까지 {search_month}월의 최고 기온 평균 : {max_temp_list}')

    x_data= [i for i in range(start_year,last_year+1)]
    draw_two_plots(f'{second_decade}월 최저 기온 비교', x_data,
                   min_temp_list, '최저기온',
                   max_temp_list, '최고기온')
    
main()