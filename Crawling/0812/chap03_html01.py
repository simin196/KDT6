from bs4 import BeautifulSoup

html_text = '<span class="rad">Heavens! what a virul;aent attack!</span>'
soup= BeautifulSoup(html_text, 'html.parser')

object_tag= soup.find('span')
print('object_tag: ', object_tag)
print('attrs: ', object_tag.attrs) #>>> attrs는 딕셔너리로 리턴하는데 값은 리스트로 반환
print('value: ', object_tag.attrs['class'])
print('text: ', object_tag.text)

