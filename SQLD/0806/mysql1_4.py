import pymysql
import pandas as pd
import csv

conn = pymysql.connect(host='localhost', user='root', password='12325246',
                       db='sakila', charset='utf8')

cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from language')
rows = cur.fetchall()

language_df= pd.DataFrame(rows)
print(language_df)
print()
print(language_df['name'])

cur.close()
conn.close()
