#tag 없이 바로 텍스크 검색, 간단한거는 가능 복잡한건 좀 힘듬
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup= BeautifulSoup(html, 'html.parser')

prince_list= soup.find_all(string='the prince')
print(prince_list)
print('the prince count: ', len(prince_list))