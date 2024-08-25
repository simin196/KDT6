import requests
from bs4 import BeautifulSoup

# top10

url='https://finance.naver.com/sise/sise_market_sum.naver'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser') 

company = soup.find('table',{'class' : 'type_2'}).find_all('a',{'class': 'tltle'},limit=10)
com_link = []
com_name = []
for name in company:
    com_name.append(name.text)
    link = name.attrs['href']
    com_link.append(link)

def money(link):
    url1='https://finance.naver.com' + link
    html1 = requests.get(url1)
    soup1 = BeautifulSoup(html1.text, 'html.parser')
    a1=soup1.find('dl',{'class':'blind'}).find_all('dd')
    idxs = [1,2,3,4,5,6,8]
    print(url1)
    for idx in idxs:
        aa=a1[idx].text.split(' ')
        print(f'{aa[0]} : {aa[1]}')

def top10():
    while True:
        print("-"*40)
        print('[네이버 코스피 상위 10대 기업 목록]')
        print("-"*40)
        i=1
        for name in com_name:
            print(f'[{i}] {name}')
            i += 1
        com_count= int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
        if com_count==-1:
            print('프로그램 종료')
            break
        else:
            money(com_link[com_count-1])
top10()
