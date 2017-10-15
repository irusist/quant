# -*- coding: utf-8 -*-


import pandas as pd
import pymysql
import urllib2


conn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')


# 中证指数
sql = "select id, index_code from index_basic_info where index_series = 1"
df = pd.read_sql(sql, conn, index_col="id")
index_code_list = list(df['index_code'])
print("found %s index from db" % str(len(index_code_list)))

for index_code in index_code_list:
    # get index constituent from csindex website
    try:
        df = pd.read_excel('http://www.csindex.com.cn/uploads/file/autofile/cons/' + index_code + 'cons.xls', converters={4: str})
    except urllib2.HTTPError as error:
        # maybe 404 error
        print('index %s occurs exception: %s' % (index_code, str(error)))
        continue

    stock_code_list_new = set(df.iloc[:, 4])

    # sql = "select id, code from stock_hs where biz_date='2017-09-29' and trade_status not in ('终止上市', '暂停上市') and code not like '90%' and code not like '20%' order by code"
    # get index constituent from database
    sql = "select id, stock_code from index_constituent_current where index_code = '" + index_code + "'"
    df = pd.read_sql(sql, conn, index_col="id")
    stock_code_list_db = list(df['stock_code'])

    stock_code_list_db = map(lambda x: x[:-3], stock_code_list_db)
    stock_code_list_db = set(stock_code_list_db)

    # to be added
    stock_code_add = stock_code_list_new.difference(stock_code_list_db)
    # to be removed
    stock_code_remove = stock_code_list_db.difference(stock_code_list_new)

    if len(stock_code_remove) > 0:
        print("index %s to be removed %s" % (index_code, stock_code_remove))
    if len(stock_code_add) > 0:
        print("index %s to be added %s" % (index_code, stock_code_add))

