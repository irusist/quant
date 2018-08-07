# -*- coding: utf-8 -*-


import pandas as pd

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
cursor = conn.cursor()


index_code = '930714'
df = pd.read_csv("~/Downloads/aaaa.csv", encoding='utf-8')
df[u'状态'] = (df[u'状态'] == u'纳入').astype(int)

print df
param = []
if len(df) > 1:
    for i in range(len(df)):
        element = list(df.iloc[i])
        element.insert(0, index_code)
        element[-1] = int(element[-1])
        param.append(element)  # 转成list_tuple格式
if len(df) == 1:
    element = list(df.iloc[0])
    element.insert(0, index_code)
    # element = (index_code, ) + element
    element[-1] = int(element[-1])
    param = [element]
# print param

sql = "insert into index_constituent_history (index_code, biz_date, stock_code, stock_name, status) values (%s, %s, %s, %s, %s) "

# 入库
cursor.executemany(sql, param)
# 提交
conn.commit()


for p in param:
    status = p[-1]
    if status == 0:
        sql = "delete from index_constituent_current where index_code = %s and stock_code = %s"
        cursor.execute(sql, (p[0], p[2]))
    else:
        sql = "insert into index_constituent_current (index_code, stock_code, stock_name) values (%s, %s, %s) "
        cursor.execute(sql, (p[0], p[2], p[3]))
    conn.commit()

cursor.close()
