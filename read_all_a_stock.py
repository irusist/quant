import pandas as pd
import pymysql

mysql_cn= pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
sql = "select id, biz_date, code, name from stock_hs where biz_date = '2017-09-29'"
df = pd.read_sql(sql, mysql_cn, index_col="id")
code_list = list(df['code'])
# uqer.io
# code_list = map(lambda  x : x[:-3], code_list)
# joinquant
code_list = map(lambda  x : x[:-3] + ('.XSHE' if x.endswith('SZ') else '.XSHG'), code_list)
print code_list
print len(code_list)
# df.to_csv("/Users/zhulx/tmp/all_stock.csv", encoding="utf-8")
# uqer.io
df.to_csv("/Users/zhulx/tmp/all_stock.csv", encoding="utf-8")





#pd.io.sql.to_sql(df,'test',db,flavor='mysql',if_exists='replace',index=False,chunksize=10000)