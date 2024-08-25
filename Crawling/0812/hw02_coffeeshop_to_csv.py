from urllib.request import urlopen 
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote # 검색을 한글로 하고 싶을 때
import pandas as pd
'''
url 주소를 불러와서 각 페이지 마다 변화되는 부분  >>> No의 번호 1~50
각 매점의 지역, 매장명, 매장 주소, 전화번호를 csv파일로 저장
1. 페이지 불러오고
2. 각표에 tbody을 태그
3. [1]지역 [2]이름 [4]주소 [5]전화번호
4. 1부터 50페이지 까지 전체 진행 
5. 전체 묶어서 csv파일로 저장
'''

cafecafelist=[]
for j in range(1,51):
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={j}&sido=&gugun=&store=')
    soup = BeautifulSoup(html.read(), 'html.parser')
    cafelist =soup.select('table.tb_store > tbody > tr')
    for i in cafelist:
        idx = i.select('td')
        city= idx[0].text
        name= idx[1].text
        address= idx[3].text
        phone= idx[5].text
        cafecafelist.append([city,name,address,phone])

cafeDF=pd.DataFrame(cafecafelist, columns=['city','name','address','phone'])
cafeDF.to_csv('hollys_branches.csv',encoding='utf-8')


