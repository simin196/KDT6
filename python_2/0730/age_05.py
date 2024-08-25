# 인구 구조 그래프 함수 구현

import csv
import re
import matplotlib.pyplot as plt
import koreanize_matplotlib

def parse_city_name(city):
    city_name = re.split('[()]', city)
    return city_name[0]


# def print_population(population):
#     for i in range(len(population)):
#         print(f'{i:3d}세: {population[1]:4d}명', end= ' ')
#         if (i + 1) % 10 ==0:
#             print()

def draw_piechart(city_name, city_population, voting_population):
    non_voting_populatino= city_population - voting_population
    population= [non_voting_populatino, voting_population]
    color=['tomato', 'royalblue']
    plt.pie(population, labels=['18세 미만','18세 이상'], autopct='%.1f%%', colors=color, startangle=90)
    plt.legend()
    plt.title(city_name + "투표 가능 인구 비율")
    plt.show()

def get_voting_population(city):
    f=open('age.csv', encoding='euc_kr')
    data = csv.reader(f)
    header = next(data)

    city_name = ''
    city_population = 0
    voting_population =0
    for row in data:
        if city in row[0]:
            city_population =row[1]
            city_population= city_population.replace(',','')
            city_population= int(city_population)
            city_name=parse_city_name(row[0])
            for data in row[21:]:
                data = data.replace(',','')
                voting_num = int(data)
                voting_population += voting_num
            break
    print(f'{city_name}전체 인구수:{city_population:,}명,'
          f'투표 가능 인구수: {voting_population:,}명')            
    
    draw_piechart(city_name,city_population,voting_population)
                                                     
city= input('투표 가능 인구수를 확인할 도시이름을 입력하세요: ')
get_voting_population(city)