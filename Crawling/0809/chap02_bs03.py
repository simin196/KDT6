html_example= '''
<!DOCTYPE html>
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
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_example, 'html.parser')
print(soup.find('div'))

div_text = soup.find('div', {'id': 'text_id2'})
print(div_text.text)
print('-'*50)
print(div_text.string)

href_Link = soup.find('a', {'class': 'internal_link'})
href_Link = soup.find('a', class_= 'internal_link')

print(href_Link)
print(href_Link['href'])
print(href_Link.get['href'])
print(href_Link.text)

print('href_link,attrs: ', href_Link.attrs)
print('class 속성값: ', href_Link['class'])

href_value = soup.find(attrs={'href' : 'www.google.com'})
href_value = soup.find('a', attrs={'href' : 'www.google.com'})

print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)

span_tag=soup.find('span')

print('span tag`:', span_tag)
print('sttrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.text)