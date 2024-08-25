#tag 없이 바로 텍스크 검색, 간단한거는 가능 복잡한건 좀 힘듬
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup= BeautifulSoup(html, 'html.parser')

print('previous_siblings')
for sibling in soup.find('tr', {'id': 'gift2'}):
    print(sibling)

sibling1 = soup.find('tr', {'id' : 'gift3'}).next_sibling
print('sibling1: ', sibling1)
print(ord(sibling1))

sibling2 = soup.find('tr', {'id': 'gift3'}).next_sibling.next_sibling
print(sibling2)

style_tag = soup.style
print(style_tag.parent)

img1= soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)