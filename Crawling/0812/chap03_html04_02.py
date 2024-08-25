#tag 없이 바로 텍스크 검색, 간단한거는 가능 복잡한건 좀 힘듬
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup= BeautifulSoup(html, 'html.parser')

desc = soup.find('table', {'id': 'giftList'})
list_desc = list(desc)
print('children 개수: ', len(list_desc))

index= 0
for tag in list_desc:
    print(tag)