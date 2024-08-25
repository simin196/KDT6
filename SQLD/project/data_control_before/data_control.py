import pymysql
import pandas as pd
import csv
import numpy as np
conn = pymysql.connect(host='localhost', user='root', password='4665', db='product', charset='utf8')
cur = conn.cursor()

def isert_p_name(type,d):
    sql = 'insert into product_name_tb(type_id,product_name) values(%s, %s)'
    cur.execute(sql,(type,d))

def isert_p_price(d,val,year):
    idx = 1
    for v in val:
        sql = 'insert into product_price_tb(product_id,city_id,product_price,year) values(%s, %s, %s, %s)'
        cur.execute(sql,(d,idx,v,year))
        idx +=1
    conn.commit()

def product_name_insert_list(type, data):
    for d in data:
        sql = 'select product_id from product_name_tb where product_name = %s'
        cur.execute(sql, d)
        cd = cur.fetchone()
        if cd == None :
            isert_p_name(type,d)
    conn.commit()
    print('입력완료')

def data_isert(link):
    data = pd.read_excel(link)
    data = data.fillna(0)
    product_name_list = data[data.columns[4]].to_list()
    product_price_city_dict = {}
    for idx, val in enumerate(product_name_list):
        product_price_city_dict[val] = data.loc[idx][data.columns[9:16]].tolist()
    product_name_insert_list('A',product_name_list)
    for idx,val in product_price_city_dict.items():
        sql = 'select product_id from product_name_tb where product_name = %s'
        cur.execute(sql,idx)
        d = cur.fetchone()
        if d == None :
            isert_p_name('A',idx)
            sql = 'select product_id from product_name_tb where product_name = %s'
            cur.execute(sql,idx)
            d = cur.fetchone()
        isert_p_price(d,val,2023)



data_isert('신선식품2019.xls')


cur.close()
conn.close()
