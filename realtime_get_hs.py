import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': '6125633fe86dec75d9edcd37ac089d8aed148b9e',
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
# 2017-12-08
code_list += ['002917.SZ', '300731.SZ']
# 2017-12-12
code_list += ['603890.SH', '300732.SZ']
# 2017-12-13
code_list += ['002916.SZ']
# 2017-12-15
code_list += ['600025.SH']
# 2017-12-18
code_list += ['603477.SH', '002919.SZ']
# 2017-12-19
code_list += ['002918.SZ']
# 2017-12-25
code_list += ['603283.SH']
# 2017-12-26
code_list += ['002920.SZ']
# 2017-12-27
code_list += ['300684.SZ', '002921.SZ']
# 2017-12-29
code_list += ['300735.SZ', '603655.SH', '002922.SZ', '603329.SH']
# 2018-01-03
code_list += ['603080.SH']
# 2018-01-05
code_list += ['300664.SZ', '002923.SZ', '603161.SH']
# 2018-01-09
code_list += ['300736.SZ']
# 2018-01-15
code_list += ['002925.SZ']
# 2018-01-16
code_list += ['603056.SH', '300733.SZ']
# 2018-01-17
code_list += ['601828.SH']
# 2018-01-18
code_list += ['300624.SZ']
# 2018-01-19
code_list += ['300738.SZ']
# 2018-01-22
code_list += ['603895.SH']
# 2018-01-24
code_list += ['603356.SH']
# 2018-01-25
code_list += ['300737.SZ']
# 2018-01-31
code_list += ['601838.SH']
# 2018-02-01
code_list += ['300739.SZ', '603506.SH']
# 2018-02-02
code_list += ['603516.SH']
# 2018-02-05
code_list += ['002926.SZ']
# 2018-02-06
code_list += ['603871.SH', '300644.SZ']
# 2018-02-08
code_list += ['603709.SH', '300740.SZ']
# 2018-02-12
code_list += ['603156.SH']
# 2018-02-23
code_list += ['002927.SZ']
# 2018-02-26
code_list += ['603712.SH']
# 2018-02-27
code_list += ['603680.SH']
# 2018-02-28
code_list += ['601360.SH']
# 2018-03-01
code_list += ['600901.SH', '300741.SZ', '002929.SZ']
# 2018-03-02
code_list += ['603059.SH', '002928.SZ']
# 2018-03-23
code_list += ['300634.SZ']
# 2018-03-26
code_list += ['600929.SH']
# 2018-03-28
code_list += ['002930.SZ']
# 2018-03-30
code_list += ['603214.SH', '300504.SZ']
# 2018-04-03
code_list += ['002931.SZ']
# 2018-04-10
code_list += ['603897.SH']
# 2018-04-12
code_list += ['603301.SH']
# 2018-04-17
code_list += ['603773.SH']
# 2018-04-18
code_list += ['603876.SH']
# 2018-04-20
code_list += ['603733.SH']
# 2018-04-26
code_list += ['603348.SH']
# 2018-04-27
code_list += ['300743.SZ', '603596.SH']
# 2018-05-08
code_list += ['603259.SH', '300742.SZ']
# 2018-05-09
code_list += ['603013.SH']
# 2018-05-16
code_list += ['300454.SZ']
# 2018-05-17
code_list += ['603045.SH']
# 2018-05-23
code_list += ['300745.SZ']
# 2018-05-25
code_list += ['300746.SZ']
# 2018-05-28
code_list += ['603486.SH']
# 2018-06-08
code_list += ['601138.SH']
# 2018-06-11
code_list += ['601330.SH', '300750.SZ']
# 2018-06-12
code_list += ['603666.SH']
# 2018-06-13
code_list += ['601990.SH']
# 2018-06-20
code_list += ['601066.SH']
# 2018-06-22
code_list += ['603587.SH']
# 2018-06-25
code_list += ['300747.SZ']
# 2018-06-27
code_list += ['603650.SH']
# 2018-07-03
code_list += ['603693.SH']
# 2018-07-09
code_list += ['603706.SH', '603105.SH']
# 2018-07-10
code_list += ['002932.SZ']
# 2018-07-13
code_list += ['603713.SH']
# 2018-07-20
code_list += ['601869.SH']
# 2018-07-30
code_list += ['603657.SH']
# 2018-08-06
code_list += ['601606.SH']
# 2018-08-10
code_list += ['300724.SZ']
# 2018-08-27
code_list += ['603590.SH']
# 2018-08-28
code_list += ['002933.SZ', '603192.SH']
# 2018-08-31
code_list += ['601068.SH']
# 2018-09-03
code_list += ['002935.SZ']
# 2018-09-10
code_list += ['603297.SH']
# 2018-09-12
code_list += ['603790.SH']
# 2108-09-17
code_list += ['603810.SH']
# 2018-09-18
code_list += ['002938.SZ']
# 2018-09-19
code_list += ['002936.SZ']
# 2018-09-21
code_list += ['300748.SZ', '603583.SH']
# 2018-09-25
code_list += ['300749.SZ']
# 2018-09-26
code_list += ['002937.SZ', '601577.SH']
# 2018-10-15
code_list += ['300694.SZ']
# 2018-10-16
code_list += ['300760.SZ']
# 2018-10-19
code_list += ['601162.SH']
# 2018-10-23
code_list += ['002940.SZ']
# 2018-10-26
code_list += ['002939.SZ']
# 2018-11-07
code_list += ['300674.SZ']
# 2018-11-09
code_list += ['300751.SZ']
# 2018-11-15
code_list += ['603220.SH']
# 2018-11-16
code_list += ['601319.SH']
# 2018-11-28
code_list += ['002941.SZ']
# 2018-11-29
code_list += ['603187.SH', '002943.SZ']
# 2018-11-30
code_list += ['300752.SZ']



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

