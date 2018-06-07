import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': '019174f18bf425d22c8e965e48243d9fcfbd2cc0',
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
# 2018-02-13
code_list += ['08510.HK', '08522.HK', '01729.HK', '01183.HK']
# 2018-02-14
code_list += ['08040.HK', '08379.HK']
# 2018-02-23
code_list += ['08532.HK']
# 2018-02-26
code_list += ['08367.HK']
# 2018-02-27
code_list += ['08526.HK']
# 2018-02-28
code_list += ['08483.HK']
# 2018-03-02
code_list += ['01933.HK']
# 2018-03-05
code_list += ['01621.HK']
# 2018-03-08
code_list += ['02182.HK']
# 2018-03-13
code_list += ['01815.HK']
# 2018-03-14
code_list += ['01737.HK', '01705.HK']
# 2018-03-16
code_list += ['06036.HK', '02377.HK', '02363.HK']
# 2018-03-22
code_list += ['08168.HK']
# 2018-03-23
code_list += ['00807.HK']
# 2018-03-26
code_list += ['02779.HK']
# 2018-03-28
code_list += ['02116.HK', '08401.HK', '01716.HK', '08448.HK']
# 2018-03-29
code_list += ['01735.HK', '08372.HK']
# 2018-04-16
code_list += ['08447.HK', '08451.HK', '08241.HK', '08507.HK']
# 2018-04-18
code_list += ['01726.HK']
# 2018-04-20
code_list += ['08511.HK']
# 2018-04-23
code_list += ['08151.HK']
# 2018-04-27
code_list += ['01671.HK']
# 2018-05-04
code_list += ['08107.HK', '01833.HK']
# 2018-05-09
code_list += ['08527.HK']
# 2018-05-11
code_list += ['01752.HK', '02119.HK', '01750.HK', '01742.HK', '08391.HK']
# 2018-05-16
code_list += ['08521.HK', '08105.HK']
# 2018-05-18
code_list += ['08536.HK']
# 2018-05-29
code_list += ['01598.HK']
# 2018-05-30
code_list += ['08490.HK', '01978.HK']
# 2018-05-31
code_list += ['08545.HK']
# 2018-06-01
code_list += ['01451.HK', '06119.HK']


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
