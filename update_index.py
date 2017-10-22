# -*- coding: utf-8 -*-


import pandas as pd
import pymysql
import urllib2


conn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')


# 中证指数
sql = "select id, index_code from index_basic_info where index_series = 1 order by index_code"
df = pd.read_sql(sql, conn, index_col="id")
index_code_list = list(df['index_code'])
print("found %s index from db" % str(len(index_code_list)))

def convert_code(code):
    exchange = exchange_list[code]
    code_len = len(str(code))
    if exchange == 'HKG' and code_len < 4:
        zero_len = 4 - code_len
        return '0' * zero_len + code
    return code


def remove_suffix(code):
    index = code.find('.')
    if index > 0:
        return code[0:index]
    return code


def get_stock_code_from_db(code):
    # sql = "select id, code from stock_hs where biz_date='2017-09-29' and trade_status not in ('终止上市', '暂停上市') and code not like '90%' and code not like '20%' order by code"
    # get index constituent from database
    sql = "select id, stock_code from index_constituent_current where index_code = '" + code + "'"
    df = pd.read_sql(sql, conn, index_col="id")
    stock_code_list_db = list(df['stock_code'])

    stock_code_list_db = map(remove_suffix, stock_code_list_db)
    stock_code_list_db = set(stock_code_list_db)
    return stock_code_list_db


for index_code in index_code_list:
    # get stock code from db
    stock_code_list_db = get_stock_code_from_db(index_code)

    # get index constituent from csindex website
    try:
        df = pd.read_excel('http://www.csindex.com.cn/uploads/file/autofile/cons/' + index_code + 'cons.xls', converters={4: str})
        df = df.set_index(df.columns[4])
    except urllib2.HTTPError as error:
        db_len = len(stock_code_list_db)
        if db_len == 0:
            # maybe 404 error
            print('index %s occurs exception: %s, db size is 0' % (index_code, str(error)))
        else:
            print('index %s occurs exception: %s, db size is %s' % (index_code, str(error), str(db_len)))
        continue
    except StandardError as error:
        print('index %s occurs exception: %s' % (index_code, str(error)))
        continue

    exchange_list = df.iloc[:, 6]
    stock_code_list_new = df.index
    stock_code_list_new = map(convert_code, stock_code_list_new)
    stock_code_list_new = set(stock_code_list_new)

    # to be added
    stock_code_add = stock_code_list_new.difference(stock_code_list_db)
    # to be removed
    stock_code_remove = stock_code_list_db.difference(stock_code_list_new)

    if len(stock_code_remove) > 0:
        print("index %s to be removed %s" % (index_code, stock_code_remove))
    if len(stock_code_add) > 0:
        print("index %s to be added %s" % (index_code, stock_code_add))

