from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

cafeDF=pd.read_csv('hollys_branches.csv')
print(cafeDF.head())

# 1. 전체 매장 정보를 csv파일로 저장
for i in range(len(cafeDF)):
    print(f'[{i+1}]: 매장이름: {cafeDF.iloc[i][1]}, 지역: {cafeDF.iloc[i][2]}, 주소: {cafeDF.iloc[i][3]}, 전화번호:{cafeDF.iloc[i][4]}')\

print(f'전체 매장 수: {len(cafeDF)}')
print('hollys_branches.csv 파일 저장 완료')

# 2. 지역 검색
'''
저장된 파일 읽고 
무한 반복문 >> quit입력으로 프로그램 종료 >> if문 break
입력받기 >> 지역 ex 대구 북구 >> .strip().split()로 나누고
나누어진 단어들 비교 >> 해당지역 매장이름, 주소, 전화번호 출력 
추가로 앞에 인덱스 1부터 시작
데이터 프레임 앞에 검색된 매장 수 기입 >> len()으로 사용
만약에 len()이 0이라면 >> 검색된 매장이 없습니다. print
'''
# while True:
place = input('검색할 매장의 지역을 입력하세요: ').strip().split()
# if place == 'quit':
        # break
selectDF = cafeDF[cafeDF['address']].isin(place)
selectDF
