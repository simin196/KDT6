import pymysql
import pandas as pd
import csv

# 4번과 다르게 4번은 하나하나씩 추가를 했는데
# 5번에서는 executemany를 사용해서 데이터를 한번에 추가

conn = pymysql.connect(host='localhost', user='root', password='12325246',
                       db='sqlclass_db', charset='utf8')

curs = conn.cursor()
sql = ''' insert into customer(name, category, region)
            values(%s,%s,%s)'''

data = (
    ('홍진우',1,'서울'),
    ('강지수',2,'부산'),
    ('김청진',1,'대구'),
)
curs.executemany(sql, data)
conn.commit()
print('executemany() 완료')
curs.close()
conn.close()


