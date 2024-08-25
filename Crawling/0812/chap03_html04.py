#tag 없이 바로 텍스크 검색, 간단한거는 가능 복잡한건 좀 힘듬
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup= BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))

index= 0
for child in table_tag.children:
    index+=1
    print(f"[{index}]: {child}")
    print('-'*30)