import re

lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')

lookahead2 = re.search('.+(?=am)','2023-01-26 am 10:00:01')
print(lookahead2.group())

lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)

lookbehind1 = re.search('.(?<=am)+','2023-01-26 am 11:00:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+', 'USD: $51')
print(lookbehind2)

lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 foor 100 apples.')
print(lookbehind4)