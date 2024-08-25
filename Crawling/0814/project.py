"""

사람인에서 데이터 크롤링
page에 수가 페이지 숫자
검색 키워드를 데이터 및 빅데이터 머신러닝으로 신입 경력2년차로 한정
실제 밑에 있는 키워드 단어들을 모아 wordcloud로 진행
각 사람마다 csv파일 or 데이터 프레임으로 저장


사람인 주소
https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={}&cat_kewd=2248%2C82%2C83%2C109%2C116&exp_cd=1%2C2&exp_min=2&exp_max=2&search_optional_item=y&search_done=y&panel_count=y&preview=y&sort=RD&isAjaxRequest=0&page_count=50&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=4#searchTitle
{}에 들어가는 숫자 따라서 페이지 달라짐

이 조건으로 들어감 
    데이터 사이언스
    데이터 분석가
    데이터 엔지니어
    머신러닝
    빅데이터 
    신입 및 경력2년
    최신순

한페이지 당 50개씩

각 단락에 키워드 단어들을 모아서 모으기

csv는 인덱스 숫자 회사명 제목 키워드

일단 여기까지

"""
from urllib.request import Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections
import platform
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter
from konlpy.tag import Okt


# # for j in range(6,11):
# url=f'https://www.saramin.co.kr/zf_user/jobs/list/job-category?page=7&cat_kewd=2248%2C82%2C83%2C109%2C116%2C107%2C106&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=1&page_count=100&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle'
# html = urlopen(url)
# soup = BeautifulSoup(html, 'html.parser')
# box_item= soup.find('div',{'class':'box_item'})
# company_keyword = box_item.find_all('span',{'class':'job_sector'})
# print(company_keyword)

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

item_list = []
for n in range(6,11):
    url=f'https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={n}&cat_kewd=2248%2C82%2C83%2C109%2C116%2C107%2C106&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=100&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle'
    urlrequests= Request(url,headers={'User-Agent':'Mozilla/5.0'})
    html = urlopen(urlrequests)
    soup = BeautifulSoup(html, 'html.parser')
    list_body=soup.find('div',{'class':'list_body'})
    job_sector= list_body.find_all('span',{'class':'job_sector'})
    for num in range(100):
        span_string = str(job_sector[num])
        remove_span = re.split(r'<span>|</span>', span_string)
        for word in remove_span:
            if word !='':
                item_list.append(word)

while '<span class="job_sector">\n' in item_list:
    item_list.remove('<span class="job_sector">\n')
while ' 외                    ' in item_list:
    item_list.remove(' 외                    ')
# stopwords =	['데이터엔지니어']
while '데이터엔지니어' in item_list:
    item_list.remove('데이터엔지니어')
while '데이터분석가' in item_list:
    item_list.remove('데이터분석가')

okt = Okt()	

word_freq = Counter(item_list)

if platform.system() == 'Windows':
	path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin':
	path = r'/System/Library/Fonts/AppleGothic'
else:
	path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

img_mask = np.array(Image.open('cloud.png'))

# WordCloud 생성
wordcloud = WordCloud(font_path=path ,width=800, height=800,repeat=True, mask= img_mask, background_color='white').generate_from_frequencies(word_freq)


# WordCloud 출력
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()