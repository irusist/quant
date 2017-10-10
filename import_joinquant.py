# -*- coding: utf-8 -*-

import os

import pandas as pd

import pymysql

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, "data", "joinquant")
print(data_path)

for file_name in os.listdir(data_path):
    file = os.path.join(data_path, file_name)
    df = pd.read_csv(file, encoding='utf-8')
    print(df)
    param = []
    if len(df) > 1:
        for i in range(len(df)):
            element = list(df.iloc[i])[1:]
            param.append(element)  # 转成list_tuple格式
    if len(df) == 1:
        element = list(df.iloc[0])
        element = list(df.iloc[i])[1:]
        param = [element]
    print(param)

    conn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
    df.to_sql('joinquant_stock_hs', conn, flavor='mysql', schema='quant', index=False, )
    cursor = conn.cursor()
    sql = "insert into joinquant_stock_hs(code, biz_date, pe, pb, ps, pcf) values (%s, %s, %s, %s, %s, %s) "

    # 入库
    cursor.executemany(sql, param)
    # 提交
    conn.commit()
    cursor.close()
