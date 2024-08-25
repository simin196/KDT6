import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs= BeautifulSoup(html, 'html.parser')

# 두 개의 테이블 중에 첫 번째 테이블 사용
#                              속성     속성값
table = bs.find_all('table', {'class': 'wikitable'})[0] # >> 인덱스로 테이블 첫번째 사용 
rows = table.find_all('tr')
# 행찾기 >>>  테이블에서 . 속성 tr 찾아 담기

# csv파일 만들기
csvFile= open('editors.csv', 'wt', encoding='utf-8') # >> t : text mode
writer= csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['th','td']):
            print(cell.text.strip())
            csvRow.append(cell.text.strip())
        writer.writerow(csvRow)
finally:
    csvFile.close()

