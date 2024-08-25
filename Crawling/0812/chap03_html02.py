from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup= BeautifulSoup(html, 'html.parser')

name_list = soup.find_all('span', {'class': 'green'})
for name in name_list:
    print(name.string)

