# -*- coding: utf-8 -*-
import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': 'b34e26c2718bfc47d479de7c2cd9777a57aecb4c',
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
# today = '20190212'
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
# 2018-12-05
code_list += ['002942.SZ']
# 2018-12-13
code_list += ['300753.SZ']
# 2018-12-24
code_list += ['603629.SH']
# 2018-12-28
code_list += ['300756.SZ', '603185.SH']
# 2019-01-03
code_list += ['601860.SH']
# 2019-01-08
code_list += ['300757.SZ']
# 2019-01-11
code_list += ['603121.SH']
# 2019-01-16
code_list += ['603739.SH', '002948.SZ']
# 2019-01-17
code_list += ['603332.SH', '002945.SZ']
# 2019-01-21
code_list += ['601298.SH']
# 2019-01-22
code_list += ['603700.SH']
# 2019-01-23
code_list += ['601615.SH']
# 2019-01-25
code_list += ['002946.SZ']
# 2019-01-28
code_list += ['300759.SZ']
# 2019-01-29
code_list += ['300755.SZ']
# 2019-01-30
code_list += ['603351.SH']
# 2019-02-01
code_list += ['002947.SZ']
# 2019-02-15
code_list += ['601865.SH']
# 2019-02-18
code_list += ['300761.SZ']
# 2019-02-22
code_list += ['603956.SH', '300758.SZ']
# 2019-02-26
code_list += ['002949.SZ']
# 2019-03-01
code_list += ['600928.SH']
# 2019-03-11
code_list += ['002950.SZ']
# 2019-03-14
code_list += ['300762.SZ']
# 2019-03-15
code_list += ['002951.SZ']
# 2019-03-19
code_list += ['300763.SZ']
# 2019-03-22
code_list += ['300765.SZ']
# 2019-03-25
code_list += ['300766.SZ']
# 2019-03-26
code_list += ['002958.SZ', '603681.SH']
# 2019-03-28
code_list += ['002952.SZ']
# 2019-03-29
code_list += ['300767.SZ']
# 2019-04-02
code_list += ['603379.SH']
# 2019-04-12
code_list += ['300768.SZ']
# 2019-04-15
code_list += ['603068.SH', '300769.SZ']
# 2019-04-16
code_list += ['603317.SH']
# 2019-04-19
code_list += ['300770.SZ']
# 2019-04-22
code_list += ['300771.SZ']
# 2019-04-25
code_list += ['300773.SZ']
# 2019-04-26
code_list += ['300772.SZ']
# 2019-04-29
code_list += ['603967.SH']
# 2019-05-08
code_list += ['603697.SH']
# 2019-05-09
code_list += ['002953.SZ']
# 2019-05-10
code_list += ['300778.SZ']
# 2019-05-15
code_list += ['603267.SH']
# 2019-05-16
code_list += ['600989.SH', '300777.SZ']
# 2019-05-17
code_list += ['300776.SZ']
# 2019-05-21
code_list += ['300775.SZ']
# 2019-05-22
code_list += ['603982.SH', '300779.SZ']
# 2019-05-23
code_list += ['002955.SZ', '603327.SH']
# 2019-05-31
code_list += ['300780.SZ']
# 2019-06-06
code_list += ['300781.SZ']
# 2019-06-14
code_list += ['603915.SH']
# 2019-06-18
code_list += ['300782.SZ']
# 2019-06-19
code_list += ['002956.SZ']
# 2019-06-20
code_list += ['603217.SH']
# 2019-06-21
code_list += ['603863.SH', '300594.SZ']
# 2019-06-26
code_list += ['600968.SH']
# 2019-06-27
code_list += ['603867.SH']
# 2019-06-28
code_list += ['601698.SH']
# 2019-07-05
code_list += ['601236.SH', '300788.SZ']
# 2019-07-12
code_list += ['300783.SZ']
# 2019-07-15
code_list += ['300785.SZ']
# 2019-07-16
code_list += ['603236.SH']
# 2019-07-19
code_list += ['603256.SH']

# 2019-07-22  科创板开始， joinquant有pe数据， uqer没有pe数据
code_list += ['688001.SH', '688002.SH', '688003.SH', '688006.SH', '688008.SH', '688012.SH',
              '688010.SH', '688333.SH', '688018.SH', '688019.SH', '688005.SH', '688007.SH',
              '688009.SH', '688011.SH', '688029.SH', '688088.SH', '688122.SH', '688016.SH',
              '688388.SH', '688066.SH', '688028.SH', '688033.SH', '688022.SH', '688020.SH',
              '688015.SH']
# 2019-07-23
code_list += ['300786.SZ']
# 2019-07-25
code_list += ['603983.SH']
# 2019-07-26
code_list += ['603687.SH', '002957.SZ']
# 2019-07-29
code_list += ['603279.SH']
# 2019-07-30
code_list += ['603613.SH']
# 2019-08-02
code_list += ['002966.SZ']
# 2019-08-05
code_list += ['603530.SH']
# 2019-08-06
code_list += ['603662.SH']
# 2019-08-08  uqer有科创板数据了
code_list += ['688188.SH', '688099.SH']
# 2019-08-09
code_list += ['002960.SZ', '603115.SH']
# 2019-08-12
code_list += ['688321.SH']
# 2019-08-15
code_list += ['300787.SZ']
# 2019-08-23
code_list += ['002959.SZ']
# 2019-08-26
code_list += ['003816.SZ', '603992.SH']
# 2019-08-28
code_list += ['300789.SZ', '603755.SH']
# 2019-08-30
code_list += ['603093.SH']
# 2019-09-05
code_list += ['002961.SZ']
# 2019-09-06
code_list += ['688168.SH']
# 2019-09-09
code_list += ['603927.SH']
# 2019-09-17  9月17日查询数据，股票代码不存在
code_list += ['002962.SZ']
# 2019-09-20
code_list += ['300790.SZ']
# 2019-09-25
code_list += ['300791.SZ', '688116.SH']
# 2019-09-27
code_list += ['300792.SZ']
# 2019-09-30       2019-09-27 到 2019-10-08 数据缺失， 国庆回老家，没带电脑，小宝生病了，9号才回
code_list += ['688030.SH', '688068.SH', '688036.SH']
# 2019-10-14
code_list += ['688368.SH']
# 2019-10-15
code_list += ['603786.SH']
# 2019-10-18
code_list += ['300793.SZ']
# 2019-10-21
code_list += ['603815.SH']
# 2019-10-22
code_list += ['300795.SZ']
# 2019-10-25
code_list += ['688139.SH', '002965.SZ']
# 2019-10-28
code_list += ['002963.SZ', '688098.SH']
# 2019-10-29
code_list += ['603610.SH', '300799.SZ', '601077.SH']
# 2019-10-30
code_list += ['688108.SH', '688366.SH']
# 2019-10-31
code_list += ['688369.SH', '688025.SH']
# 2019-11-01
code_list += ['688058.SH', '300797.SZ']
# 2019-11-05
code_list += ['688199.SH', '688023.SH', '688128.SH', '688202.SH', '688389.SH']
# 2019-11-06
code_list += ['688363.SH', '688299.SH', '300800.SZ', '688288.SH', '688021.SH']
# 2019-11-08
code_list += ['688166.SH', '300564.SZ', '002967.SZ']
# 2019-11-11
code_list += ['603489.SH']
# 2019-11-14
code_list += ['300802.SZ']
# 2019-11-15
code_list += ['300796.SZ', '688101.SH', '688300.SH']
# 2019-11-18
code_list += ['300803.SZ', '688111.SH']
# 2019-11-20
code_list += ['688138.SH']
# 2019-11-21
code_list += ['688196.SH', '300805.SZ']
# 2019-11-22
code_list += ['300798.SZ']
# 2019-11-25
code_list += ['300806.SZ', '603390.SH']
# 2019-11-26
code_list += ['601916.SH']
# 2019-11-28
code_list += ['300801.SZ']
# 2019-11-29
code_list += ['300808.SZ']
# 2019-12-02
code_list += ['002969.SZ']
# 2019-12-03
code_list += ['688310.SH', '002968.SZ', '688358.SH']
# 2019-12-04
code_list += ['300809.SZ', '688357.SH', '688118.SH']
# 2019-12-05
code_list += ['688399.SH']
# 2019-12-06
code_list += ['300810.SZ']
# 2019-12-09
code_list += ['688258.SH', '688198.SH']
# 2019-12-10
code_list += ['601658.SH']
# 2019-12-11
code_list += ['688218.SH', '688039.SH']
# 2019-12-16
code_list += ['688037.SH']
# 2019-12-17
code_list += ['603053.SH', '002970.SZ']
# 2019-12-19
code_list += ['300807.SZ', '688089.SH']
# 2019-12-20
code_list += ['601512.SH']
# 2019-12-23
code_list += ['688123.SH']
# 2019-12-24
code_list += ['603995.SH']
# 2019-12-26
code_list += ['688268.SH']
# 2019-12-27
code_list += ['002972.SZ']
# 2019-12-30
code_list += ['688078.SH', '300811.SZ']
# 2019-12-31
code_list += ['603109.SH']
# 2020-01-06
code_list += ['688081.SH', '688181.SH', '002973.SZ']
# 2020-01-09
code_list += ['300812.SZ']
# 2020-01-13
code_list += ['002971.SZ']
# 2020-01-14
code_list += ['688178.SH', '300813.SZ']
# 2020-01-15
code_list += ['603551.SH']
# 2020-01-16
code_list += ['601816.SH']


# code_list.sort()
print(code_list)
''


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

