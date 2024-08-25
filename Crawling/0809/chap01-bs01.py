from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser') # 클래스의 생성자  >> 객체 생성
#^ 생성된 객체         
# print(bs)
# print(bs.h1)
# print(bs.h1.string)
# .text -> .string : 테그 내부의 문자열만 가져옴

print(bs.div) # 
print(bs.div.text) # 