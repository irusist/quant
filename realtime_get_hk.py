import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': '5c915d14d91dc74b5f2e4c3b4753137ae66c1926',
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
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "xueqiu", "hk", today)
if not os.path.exists(base_path):
    os.mkdir(base_path)

mysql_cn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
sql = "select id, biz_date, code, name from stock_hk where biz_date = '2017-09-29' order by code"
df = pd.read_sql(sql, mysql_cn, index_col="id")
code_list = list(df['code'])

# 2018-01-12
code_list += ['06885.HK', '01707.HK', '08437.HK', '08480.HK', '08275.HK', '02337.HK', '08392.HK', '08065.HK']
code_list += ['02225.HK', '06080.HK', '08470.HK', '08436.HK', '02232.HK', '00772.HK', '01720.HK', '08426.HK', '02122.HK']
code_list += ['01337.HK', '08375.HK', '01706.HK', '08400.HK', '08376.HK', '02858.HK', '03358.HK', '01975.HK']
code_list += ['08118.HK', '08373.HK', '08402.HK', '01710.HK', '01997.HK', '08495.HK', '08406.HK', '08429.HK']
code_list += ['01697.HK', '02227.HK', '01475.HK', '01417.HK', '06090.HK', '08385.HK', '00839.HK', '01722.HK']
code_list += ['02022.HK', '08377.HK', '01727.HK', '01789.HK', '08419.HK', '03878.HK', '02708.HK', '08422.HK']
code_list += ['00784.HK', '08485.HK', '01730.HK', '08506.HK', '08501.HK', '03738.HK', '02025.HK', '08350.HK']
code_list += ['08509.HK']
# 2018-01-15
code_list += ['03309.HK']
# 2018-01-16
code_list += ['06158.HK', '08487.HK', '03699.HK', '08285.HK', '02292.HK', '02448.HK', '08493.HK', '08313.HK']
# 2018-01-17
code_list += ['08479.HK', '06182.HK', '08371.HK']
# 2018-01-18
code_list += ['08287.HK', '02139.HK']
# 2018-01-19
code_list += ['01665.HK', '08513.HK', '08043.HK']
# 2018-01-22
code_list += ['02683.HK']
# 2018-01-25
code_list += ['08136.HK', '08395.HK']
# 2018-01-26
code_list += ['08456.HK']
# 2018-01-29
code_list += ['01711.HK']
# 2018-02-02
code_list += ['08450.HK']
# 2018-02-08
code_list += ['06829.HK', '08519.HK']
# 2018-02-09
code_list += ['03319.HK']
# 2018-02-12
code_list += ['08523.HK', '08535.HK', '08473.HK']


print(code_list)
print(len(code_list))


def get_data(param_str, index):
    result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
    # result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers, proxies=proxys)
    content = result.content.decode(encoding="UTF-8")
    print(content)
    with open(os.path.join(base_path, index + '.json'), 'wb') as f:
        f.write(content.encode('utf-8'))


j = 0
count = 0
param = []
for code in code_list:
    count += 1
    param.append(code[:-3])
    # param.append(code)
    if count == 50:
        j += 1
        get_data(','.join(param), str(j))
        param = []
        count = 0

j += 1
get_data(','.join(param), str(j))

import import_xueqiu_hk
import_xueqiu_hk.import_db()
