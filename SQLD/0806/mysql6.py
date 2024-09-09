import pymysql
import pandas as pd
import csv

# 6번 update

conn = pymysql.connect(host='localhost', user='root', password='12325246',
                       db='sqlclass_db', charset='utf8')

curs = conn.cursor()

sql = ''' 
    update customer
    set region = '서울특별시'
    where region = '서울'    
    '''
curs.execute(sql)
print('update 완료')

# delete

sql = 'delete from customer where name=%s'
curs.execute(sql, '홍길동')
print('delete 홍길동')

conn.commit()
conn.close()