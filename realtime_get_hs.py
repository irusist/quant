import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': 'a8d434ddd975f5752965fa782596bd0b5b008376',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}

#
# proxys = {
#     "http": "socks5://127.0.0.1:1080",
#     "https": "socks5://127.0.0.1:1080",
# }


today = date.today().strftime('%Y%m%d')
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "xueqiu", "hs", today)
if not os.path.exists(base_path):
    os.mkdir(base_path)

mysql_cn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
sql = "select id, biz_date, code, name from stock_hs where biz_date = '2017-09-29' order by code "
df = pd.read_sql(sql, mysql_cn, index_col="id")
# df = pd.read_csv("d:\\all_stock.csv")
code_list = list(df['code'])
# 2017-10-10
code_list += ['300705.SZ', '300707.SZ']
# 2017-10-12
code_list += ['603103.SH']
# 2017-10-13
code_list += ['002903.SZ', '603110.SH', '002906.SZ']
# 2017-10-16
code_list += ['603499.SH', '002905.SZ', '300708.SZ']
# 2017-10-17
code_list += ['603829.SH']
# 2017-10-18
code_list += ['603396.SH']
# 2017-10-19
code_list += ['300710.SZ', '300709.SZ']
# 2017-10-20
code_list += ['603683.SH', '002908.SZ', '603466.SH', '002907.SZ']
# 2017-10-23
code_list += ['603922.SH']
# 2017-10-24
code_list += ['601108.SH']
# 2017-10-25
code_list += ['603607.SH', '603722.SH']
# 2017-10-26
code_list += ['300715.SZ', '002909.SZ']
# 2017-10-30
code_list += ['603260.SH']
# 2017-10-31
code_list += ['002910.SZ', '300712.SZ', '603289.SH']
# 2017-11-01
code_list += ['300713.SZ', '603912.SH', '300711.SZ']
# 2017-11-02
code_list += ['603937.SH']
# 2017-11-03
code_list += ['603659.SH']
# 2017-11-06
code_list += ['300718.SZ', '603507.SH', '603856.SH', '300717.SZ', '300720.SZ']
# 2017-11-07
code_list += ['600903.SH']
# 2017-11-09
code_list += ['300719.SZ', '300716.SZ']
# 2017-11-10
code_list += ['603083.SH', '300722.SZ', '603916.SH', '300725.SZ']
# 2017-11-13
code_list += ['603076.SH', '603278.SH']
# 2017-11-15
code_list += ['300721.SZ', '603605.SH']
# 2017-11-16
code_list += ['002864.SZ', '300723.SZ', '603970.SH']
# 2017-11-17
code_list += ['600933.SH', '603619.SH']
# 2017-11-20
code_list += ['603365.SH']
# 2017-11-21
code_list += ['603661.SH', '002912.SZ', '300726.SZ']
# 2017-11-22
code_list += ['601019.SH', '002911.SZ']
# 2017-11-27
code_list += ['300727.SZ', '603685.SH']
# 2017-11-28
code_list += ['603809.SH']
# 2017-11-30
code_list += ['603711.SH']
# 2017-12-01
code_list += ['603848.SH', '002913.SZ', '300729.SZ']
# 2017-12-04
code_list += ['603917.SH']
# 2017-12-05
code_list += ['002915.SZ', '300730.SZ']


# code_list.sort()
print(code_list)


def get_data(param_str, index):
    result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
    # result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, proxies=proxys, cookies=cookies, headers=headers)
    content = result.content.decode(encoding="UTF-8")
    with open(os.path.join(base_path, index + '.json'), 'wb') as f:
        f.write(content.encode('utf-8'))
    print(content)


print(len(code_list))

count = 0
j = 0
param = []
for code in code_list:
    count += 1
    if code.endswith('SH'):
        param.append('SH' + code[:-3])
    else:
        param.append('SZ' + code[:-3])

    if count == 50:
        j += 1
        get_data(','.join(param), str(j))
        param = []
        count = 0

j += 1
get_data(','.join(param), str(j))

import import_xueqiu_hs
import_xueqiu_hs.import_db()

