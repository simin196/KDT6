import re

m= re.match('[a-z]+', 'Python')
print(m) # >> 왼쪽에서(처음)부터 검사 >> 처음부터 틀렸기에 none출력
m= re.match('[a-z]+', 'pythoN') 
print(m) # >> 소문자 있는곳 까지만 검사
m= re.match('[a-z]+', 'PYthon')
print(m)

print('-'*30)

print(re.search('apple','I like apple!')) 

print('-'*30)

p = re.compile('[a-z]+') # >> 객체 생성
m = p.match('python')
print(m)
print(p.search('I like apple 123')) # >> 첫번째 소문자 문자만 출력

print('-'*30)
print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython'))

print('-'*30)
print(re.match('[a-z]+', 'regex pythoN'))
print(re.match('[a-z]+$', 'regex pythoN'))

print('-'*30)
print(re.match('[a-z]+', 'regex Python'))
print(re.match('[a-z]+$', 'regex Python'))

print('-'*30)
print(re.match('[a-z]+', 'regexpython'))
print(re.match('[a-z]+$', 'regexpython'))

print('-'*30)
print(re.match('[a-z]+$', 'RegexPython'))

print('-'*30)
p= re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

print('-'*30)
result = p.search('I like apple 123')
print(result)

print('-'*30)
result = p.findall('I like apple 123')
print(result)
