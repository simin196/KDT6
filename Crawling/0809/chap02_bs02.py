html_example= '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')

# 속성에 접근하는 방법 두가지
# 1 속성이용 2. 함수이용

print(soup.title)
print(soup.title.string)
print(soup.title.get_text())
print(soup.title.parent)

print('----------------------------------------------')

print(soup.h1)
print(soup.h1.string)

print('----------------------------------------------')

print(soup.a)
print(soup.a.string)
print(soup.a['href'])
print(soup.a.get('href'))

print('-'*50)

print()