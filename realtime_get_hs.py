import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': 'ed965d6ca0f68aa2f0b4a80a510e86fe5c02784d',
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

# 2017-10-10
param = []
code_list = ['300705.SZ', '300707.SZ']
for code in code_list:
    if code.endswith('SH'):
        param.append('SH' + code[:-3])
    else:
        param.append('SZ' + code[:-3])
j += 1
get_data(','.join(param), str(j))
