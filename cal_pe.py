# -*- coding: utf-8 -*-


import pandas as pd
import pymysql

mysql_cn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')

# 000015 上证红利
# 950090 50AH优选
# sql = '''  select id, biz_date, code, pe_ttm, pb, trade_status from stock_hs where code in
#   (select stock_code from index_constituent_history where index_code = '000300' and biz_date = '2005-04-08') and biz_date = '2005-04-08';
#  '''
#
# sql = ''' SELECT id, biz_date, code, pe_ttm, pb from xueqiu_hs WHERE biz_date = '2017-11-24' and code in
#     (select SUBSTRING(stock_code,1,6) from index_constituent_current where index_code = '000016') order by code
# '''
# #


# sql = ''' SELECT id, biz_date, code, pe, pb from uqer_stock_hs WHERE biz_date = '2017-11-24' and code in
#     (select SUBSTRING(stock_code,1,6) from index_constituent_current where index_code = '000016') order by code
# '''


# sql = ''' SELECT id, biz_date, code, pe, pb from uqer_stock_hs WHERE biz_date = '2017-11-24' and code in
#     (select SUBSTRING(stock_code,1,6) from index_constituent_history a where index_code = '000016' and status = 1 and a.biz_date <= '2017-11-24' and (select count(*) from index_constituent_history where index_code = a.index_code and stock_code = a.stock_code and biz_date <= '2017-11-24' and biz_date > a.biz_date and status = 0) = 0
# ) order by code
# '''

#
# sql = ''' SELECT id, biz_date, code, pe, pb from joinquant_stock_hs WHERE biz_date = '2017-11-24' and substring(code,1,6) in
#     (select SUBSTRING(stock_code,1,6) from index_constituent_current where index_code = '000016') order by code
# '''

sql = ''' SELECT biz_date from stock_hs   GROUP by biz_date order by biz_date '''

date_list = pd.read_sql(sql, mysql_cn, index_col="biz_date").index.tolist()

print(date_list)


pe_list = []
for d in date_list:
    print(d)
    sql = ''' SELECT id, biz_date, code, pe, pb from stock_hs WHERE biz_date = '%s' order by code ''' % d
    pe_list_pd = pd.read_sql(sql, mysql_cn, index_col="id")
    pe = len(pe_list_pd)/sum([1/p if p > 0 else 0 for p in pe_list_pd.pe])
    pe_list.append(pe)

print(pe_list)

df = pd.DataFrame({'PE': pd.Series(pe_list, index=date_list)})
df.to_csv("/Users/zhulx/pe2.csv")





#
#
# sql = '''select id, biz_date, code, pe_ttm , trade_status from stock_hs
# where biz_date = '2007-09-24' and trade_status in ('正常交易')'''
#

#  and hs.trade_status in ('正常交易')

# print(pe_list)

# pb = len(pe_list)/sum([1/p if p > 0 else 0 for p in pe_list.pb])
#

# print(pe)
# print(pb)



#pd.io.sql.to_sql(df,'test',db,flavor='mysql',if_exists='replace',index=False,chunksize=10000)


