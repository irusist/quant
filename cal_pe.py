# -*- coding: utf-8 -*-


import pandas as pd
import pymysql

mysql_cn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')

# 000015 上证红利
# 950090 50AH优选
sql = '''  select id, biz_date, code, pe_ttm, trade_status from stock_hs where code in
  (select stock_code from index_constituent_current where index_code = '000300') and biz_date = '2017-09-29';
 '''

#
#
# sql = '''select id, biz_date, code, pe_ttm , trade_status from stock_hs
# where biz_date = '2007-09-24' and trade_status in ('正常交易')'''
#

#  and hs.trade_status in ('正常交易')
pe_list = pd.read_sql(sql, mysql_cn, index_col="id")

print pe_list

pe = len(pe_list)/sum([1/p if p > 0 else 0 for p in pe_list.pe_ttm])


print pe


#pd.io.sql.to_sql(df,'test',db,flavor='mysql',if_exists='replace',index=False,chunksize=10000)


