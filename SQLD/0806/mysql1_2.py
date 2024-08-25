import pymysql
import pandas as pd
import csv

conn = pymysql.connect(host='localhost', user='root', password='12325246',
                       db='sakila', charset='utf8')

cur = conn.cursor()
cur.execute('select * from language')

rows=cur.fetchall()
print(rows)

language_df= pd.DataFrame(rows)
print(language_df)

cur.close()
conn.close()
