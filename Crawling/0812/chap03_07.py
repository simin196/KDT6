from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote # 검색을 한글로 하고 싶을 때

query= 'ChatGPT'
query1= quote('챗지피티') # 한국어 검색
url = f'https://search.naver.com/search.naver?sm=tab_hty.top&ssc=tab.blog.all&query={query1}'

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
blog_results = soup.select('a.title_link')
print('검색 결과수: ', len(blog_results)) # 검색 블러그의 타이틀

# # 제목 추출
# for blog_title in blog_results:
#     title = blog_title.text
#     link = blog_title['href']
#     print(f'{title}, [{link}]')

# print('-'*50)

# # 이건 검색하면 제목 밑에 있는 본문 앞부분을 스르립트 할 수 있는거
# desc_result = soup.select('a.dsc_link')
# for desc in desc_result:
#     print(desc)

search_count= len(blog_results)
desc_results= soup.select('a.dsc_link') # 검색된 블로그의 간단한 설명
for i in range(search_count):
    title = blog_results[i].text 
    link = blog_results[i]['href']
    print(f'{title}, [{link}]') # 제목
    print(desc_results[i].text) # 내용
    print('-'*80)