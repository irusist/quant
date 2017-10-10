# -*- coding: utf-8 -*-


import pandas as pd
import pymysql

index_code = 'H50023'
df = pd.read_excel('http://www.csindex.com.cn/uploads/file/autofile/cons/' + index_code + 'cons.xls', converters={4: str})
code_list = set(df.iloc[:, 4])

mysql_cn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
# sql = "select id, code from stock_hs where biz_date='2017-09-29' and trade_status not in ('终止上市', '暂停上市') and code not like '90%' and code not like '20%' order by code"
sql = "select id, stock_code from index_constituent_current where index_code = '" + index_code + "' order by stock_code"
df = pd.read_sql(sql, mysql_cn, index_col="id")
# db_code_list = list(df['code'])
db_code_list = list(df['stock_code'])

db_code_list = map(lambda x: x[:-3], db_code_list)
db_code_list = set(db_code_list)

print(len(code_list))
print(len(db_code_list))

# realtime add
add_code = code_list.difference(db_code_list)
# realtime del
del_code = db_code_list.difference(code_list)
print(add_code)
print(len(del_code))
print(del_code)
