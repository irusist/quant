# -*- coding: utf-8 -*-
import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': '385b836a045da45667afda72237fc969313f56f0',
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
# 2020-01-17
code_list += ['688278.SH']
# 2020-01-20
code_list += ['688158.SH']
# 2020-01-21
code_list += ['688100.SH']
# 2020-01-22
code_list += ['688026.SH']
# 2020-01-23
code_list += ['688266.SH', '300815.SZ', '688159.SH']
# 2020-02-04
code_list += ['603290.SH']
# 2020-02-05
code_list += ['002975.SZ', '688298.SH']
# 2020-02-06
code_list += ['603195.SH']
# 2020-02-07
code_list += ['603893.SH']
# 2020-02-10
code_list += ['300816.SZ']
# 2020-02-11
code_list += ['688186.SH', '688398.SH']
# 2020-02-12
code_list += ['688080.SH', '300818.SZ']
# 2020-02-13
code_list += ['688208.SH', '300820.SZ']
# 2020-02-17
code_list += ['688090.SH']
# 2020-02-18
code_list += ['688200.SH', '300817.SZ']
# 2020-02-21
code_list += ['688177.SH', '688169.SH', '688233.SH']
# 2020-02-24
code_list += ['603719.SH']
# 2020-02-26
code_list += ['601696.SH', '688086.SH']
# 2020-02-27
code_list += ['688396.SH']
# 2020-03-02
code_list += ['603948.SH']
# 2020-03-06
code_list += ['002976.SZ']
# 2020-03-10
code_list += ['603949.SH']
# 2020-03-12
code_list += ['300821.SZ', '300819.SZ']
# 2020-03-13
code_list += ['300822.SZ']
# 2020-03-17
code_list += ['002977.SZ']
# 2020-03-19
code_list += ['300823.SZ']
# 2020-03-20
code_list += ['688051.SH']
# 2020-03-23
code_list += ['603221.SH']
# 2020-03-26
code_list += ['688189.SH']
# 2020-03-27
code_list += ['688228.SH', '300825.SZ']
# 2020-04-03
code_list += ['300826.SZ']
# 2020-04-07
code_list += ['603353.SH']
# 2020-04-08
code_list += ['002979.SZ']
# 2020-04-09
code_list += ['688096.SH', '688085.SH']
# 2020-04-10
code_list += ['300827.SZ']
# 2020-04-15
code_list += ['002980.SZ', '603095.SH']
# 2020-04-16
code_list += ['688222.SH']
# 2020-04-17
code_list += ['002981.SZ', '002978.SZ']
# 2020-04-20
code_list += ['688126.SH']
# 2020-04-21
code_list += ['300828.SZ', '603682.SH']
# 2020-04-22
code_list += ['300829.SZ', '601609.SH']
# 2020-04-24
code_list += ['002982.SZ']
# 2020-04-27
code_list += ['688318.SH']
# 2020-04-28
code_list += ['603439.SH', '002983.SZ']
# 2020-04-29
code_list += ['603392.SH', '002985.SZ', '688365.SH']
# 2020-04-30
code_list += ['603212.SH']
# 2020-05-06
code_list += ['300830.SZ']
# 2020-05-07
code_list += ['002987.SZ', '300831.SZ']
# 2020-05-08
code_list += ['688466.SH']
# 2020-05-11
code_list += ['688588.SH']
# 2020-05-12
code_list += ['300832.SZ']
# 2020-05-18
code_list += ['002988.SZ', '688598.SH', '688566.SH']
# 2020-05-19
code_list += ['601778.SH']
# 2020-05-20
code_list += ['300833.SZ']
# 2020-05-21
code_list += ['688516.SH']
# 2020-05-22
code_list += ['605001.SH']
# 2020-05-25
code_list += ['300835.SZ', '002990.SZ']
# 2020-05-26
code_list += ['603950.SH']
# 2020-05-28
code_list += ['605168.SH', '300836.SZ']
# 2020-06-01
code_list += ['605288.SH']
# 2020-06-02
code_list += ['688360.SH', '002986.SZ']
# 2020-06-03
code_list += ['600918.SH']
# 2020-06-05
code_list += ['300837.SZ', '601827.SH']
# 2020-06-08
code_list += ['300838.SZ', '688312.SH']
# 2020-06-09
code_list += ['688157.SH']
# 2020-06-10
code_list += ['002989.SZ', '688599.SH']
# 2020-06-12
code_list += ['688004.SH']
# 2020-06-16
code_list += ['688106.SH', '300841.SZ']
# 2020-06-18
code_list += ['300842.SZ', '605166.SH']
# 2020-06-19
code_list += ['300824.SZ', '688505.SH']
# 2020-06-22
code_list += ['688518.SH', '688520.SH']
# 2020-06-23
code_list += ['688555.SH']
# 2020-06-29
code_list += ['603087.SH', '600956.SH']
# 2020-06-30
code_list += ['300839.SZ', '688558.SH']
# 2020-07-01
code_list += ['300846.SZ', '688528.SH']
# 2020-07-02
code_list += ['300843.SZ']
# 2020-07-03
code_list += ['300845.SZ', '688600.SH']
# 2020-07-07
code_list += ['688277.SH']
# 2020-07-08
code_list += ['688568.SH', '300840.SZ', '688377.SH']
# 2020-07-09
code_list += ['300847.SZ', '688027.SH']
# 2020-07-10
code_list += ['300849.SZ', '605199.SH', '688060.SH']
# 2020-07-13
code_list += ['300850.SZ', '300852.SZ']
# 2020-07-14
code_list += ['688309.SH']
# 2020-07-15
code_list += ['688165.SH', '688180.SH']
# 2020-07-16
code_list += ['688500.SH', '688981.SH', '605108.SH']
# 2020-07-17
code_list += ['300851.SZ', '688567.SH', '688579.SH']
# 2020-07-20
code_list += ['300848.SZ', '688256.SH', '688488.SH']
# 2020-07-21
code_list += ['688580.SH']
# 2020-07-22
code_list += ['688561.SH', '688508.SH', '688336.SH', '688589.SH', '688069.SH', '300856.SH', '688418.SH', '688077.SH']
# 2020-07-23
code_list += ['300855.SZ']
# 2020-07-24
code_list += ['300853.SZ']
# 2020-07-27
code_list += ['300858.SZ', '300857.SZ']
# 2020-07-28
code_list += ['605188.SH']
# 2020-07-29
code_list += ['688050.SH']
# 2020-07-30
code_list += ['603408.SH', '605118.SH']
# 2020-07-31
code_list += ['601456.SH', '605222.SH', '002991.SZ', '688311.SH', '688586.SH']
# 2020-08-03
code_list += ['002992.SZ', '605318.SH']
# 2020-08-04
code_list += ['605399.SH']
# 2020-08-05
code_list += ['605158.SH']
# 2020-08-06
code_list += ['688338.SH', '688338.SH', '300859.SZ']
# 2020-08-07
code_list += ['605066.SH', '688556.SH']
# 2020-08-10
code_list += ['688286.SH', '688339.SH']
# 2020-08-11
code_list += ['605100.SH', '688155.SH']
# 2020-08-12
code_list += ['688313.SH', '605366.SH', '688065.SH']
# 2020-08-13
code_list += ['688185.SH']
# 2020-08-17
code_list += ['002993.SZ', '688335.SH', '688229.SH', '605088.SH', '688055.SH', '688055.SH']
# 2020-08-18
code_list += ['605388.SH', '688519.SH', '605333.SH', '688521.SH']
# 2020-08-19
code_list += ['603931.SH', '688379.SH']
# 2020-08-20
code_list += ['688393.SH', '688596.SH']
# 2020-08-21
code_list += ['605178.SH', '605008.SH']
# 2020-08-24
code_list += ['300861.SZ', '300860.SZ', '300862.SZ', '300875.SZ', '300865.SZ',
              '300866.SZ', '300863.SZ', '300869.SZ', '300867.SZ', '300868.SZ', '300870.SZ', '300864.SZ', '300871.SZ',
              '300872.SZ', '300873.SZ', '300876.SZ', '300877.SZ', '300878.SZ']
# 2020-08-25
code_list += ['605255.SH', '605123.SH']
# 2020-08-26
code_list += ['688356.SH']
# 2020-08-28
code_list += ['688289.SH', '688408.SH', '688215.SH', '688017.SH', '002996.SZ']
# 2020-08-31
code_list += ['688569.SH']
# 2020-09-01
code_list += ['300881.SZ', '300879.SZ', '300880.SZ', '603155.SH']
# 2020-09-02
code_list += ['688056.SH', '688550.SH', '688513.SH']
# 2020-09-03
code_list += ['002999.SZ', '002997.SZ', '688378.SH', '605006.SH']
# 2020-09-04
code_list += ['688390.SH']
# 2020-09-07
code_list += ['601702.SH']
# 2020-09-08
code_list += ['688095.SH', '605003.SH']
# 2020-09-09
code_list += ['688559.SH']
# 2020-09-10
code_list += ['300882.SZ', '300883.SZ', '688551.SH']
# 2020-09-11
code_list += ['605358.SH', '002984.SZ', '605009.SH']
# 2020-09-14
code_list += ['003000.SZ']
# 2020-09-15
code_list += ['605128.SH']
# 2020-09-16
code_list += ['300887.SZ', '300889.SZ', '605369.SH', '688577.SH', '300886.SZ']
# 2020-09-17
code_list += ['300891.SZ', '300890.SZ', '300888.SZ', '603112.SH']
# 2020-09-18
code_list += ['605198.SH', '688301.SH']
# 2020-09-21
code_list += ['688127.SH', '688536.SH', '003003.SZ', '003006.SZ', '605116.SH']
# 2020-09-22
code_list += ['688526.SH', '688156.SH', '003005.SZ', '003002.SZ']
# 2020-09-23
code_list += ['003008.SZ', '003007.SZ']
# 2020-09-24
code_list += ['300893.SZ', '300895.SZ', '605050.SH', '300892.SZ']
# 2020-09-25
code_list += ['603565.SH', '003010.SZ', '002998.SZ', '003009.SZ']
# 2020-09-28
code_list += ['688595.SH', '605218.SH', '605111.SH', '300897.SZ', '688013.SH', '300896.SZ', '688585.SH']
# 2020-09-29
code_list += ['605136.SH', '605018.SH']
# 2020-09-30
code_list += ['003011.SZ', '688093.SH', '605099.SH']
# 2020-10-12
code_list += ['605338.SH']
# 2020-10-13
code_list += ['003001.SZ']
# 2020-10-15
code_list += ['300999.SZ', '688330.SH']
# 2020-10-16
code_list += ['688386.SH', '300898.SZ', '300899.SZ']
# 2020-10-19
code_list += ['003012.SZ', '605336.SH']
# 2020-10-20
code_list += ['601568.SH']
# 2020-10-21
code_list += ['003015.SZ', '605058.SH']
# 2020-10-22
code_list += ['688788.SH', '003013.SZ']
# 2020-10-23
code_list += ['688129.SH']
# 2020-10-26n
code_list += ['003016.SZ', '688179.SH', '003017.SZ']
# 2020-10-27
code_list += ['601187.SH']
# 2020-10-28
code_list += ['688221.SH']
# 2020-10-29
code_list += ['300902.SZ', '300901.SZ', '300900.SZ']
# 2020-10-30
code_list += ['605169.SH', '688133.SH']
# 2020-11-02
code_list += ['601995.SH']
# 2020-11-05
code_list += ['300906.SZ', '300903.SZ', '300905.SZ']
# 2020-11-06
code_list += ['003018.SZ']
# 2020-11-09
code_list += ['688529.SH']
# 2020-11-10
code_list += ['605007.SH']
# 2020-11-11
code_list += ['688057.SH', '688135.SH']
# 2020-11-12
code_list += ['300884.SZ', '688160.SH']
# 2020-11-17
code_list += ['003019.SZ']
# 2020-11-18
code_list += ['300909.SZ', '300907.SZ', '688219.SH']
# 2020-11-23
code_list += ['300908.SZ', '605068.SH']
# 2020-11-24
code_list += ['688777.SH']
# 2020-11-25
code_list += ['605177.SH']
# 2020-11-26
code_list += ['003004.SZ']
# 2020-11-27
code_list += ['300910.SZ']
# 2020-12-01
code_list += ['605266.SH']
# 2020-12-02
code_list += ['688557.SH', '300916.SZ', '300915.SZ', '688578.SH']
# 2020-12-03
code_list += ['300911.SZ', '605258.SH']
# 2020-12-04
code_list += ['003021.SZ', '601686.SH']
# 2020-12-07
code_list += ['300912.SZ', '300913.SZ', '605183.SH', '688590.SH']
# 2020-12-08
code_list += ['605376.SH', '003022.SZ']
# 2020-12-10
code_list += ['688308.SH']
# 2020-12-11
code_list += ['003023.SZ', '003025.SZ', '688571.SH']
# 2020-12-14
code_list += ['688136.SH']
# 2020-12-15
code_list += ['003020.SZ', '605299.SH', '605151.SH']
# 2020-12-16
code_list += ['688510.SH', '688608.SH']
# 2020-12-18
code_list += ['003026.SZ', '688699.SH', '003027.SZ']
# 2020-12-21
code_list += ['300917.SZ', '688668.SH']
# 2020-12-22
code_list += ['300918.SZ', '605186.SH', '300921.SZ', '605500.SH']
# 2020-12-23
code_list += ['300919.SZ', '688678.SH']
# 2020-12-24
code_list += ['003029.SZ', '688560.SH', '688658.SH', '300923.SZ']
# 2020-12-25
code_list += ['300922.SZ', '300920.SZ', '688679.SH']
# 2020-12-28
code_list += ['605377.SH', '605179.SH', '003028.SZ']
# 2020-12-29
code_list += ['688698.SH']
# 2020-12-30
code_list += ['688618.SH', '688063.SH', '300925.SZ']
# 2020-12-31
code_list += ['605155.SH', '688686.SH', '300894.SZ']
# 2021-01-04
code_list += ['003031.SZ']
# 2021-01-06
code_list += ['300928.SZ', '605277.SH', '003030.SZ']
# 2021-01-07
code_list += ['688617.SH', '300927.SZ', '300926.SZ']
# 2021-01-11
code_list += ['003033.SZ']
# 2021-01-12
code_list += ['003032.SZ']
# 2021-01-13
code_list += ['688656.SH']
# 2021-01-18
code_list += ['688317.SH', '688819.SH']
# 2021-01-19
code_list += ['003035.SZ', '605005.SH']
# 2021-01-20
code_list += ['300929.SZ', '300935.SZ', '605228.SH']
# 2021-01-21
code_list += ['605398.SH', '300931.SZ', '300930.SZ']
# 2021-01-22
code_list += ['300933.SZ', '688680.SH', '300932.SZ']
# 2021-01-25
code_list += ['688669.SH']
# 2021-01-26
code_list += ['300936.SZ']
# 2021-01-27
code_list += ['300937.SZ', '300938.SZ', '688689.SH']
# 2021-01-28
code_list += ['003036.SZ', '688350.SH', '300939.SZ']
# 2021-01-29
code_list += ['605055.SH', '605368.SH']
# 2021-02-01
code_list += ['688607.SH', '688628.SH']
# 2021-02-03
code_list += ['300940.SZ']
# 2021-02-04
code_list += ['003037.SZ']
# 2021-02-05
code_list += ['600916.SH', '601963.SH']
# 2021-02-08
code_list += ['688059.SH', '300946.SZ', '688687.SH', '605337.SH']
# 2021-02-09
code_list += ['300941.SZ', '300942.SZ', '688665.SH', '605081.SH', '605077.SH']
# 2021-02-10
code_list += ['003038.SZ', '300947.SZ', '300945.SZ', '300943.SZ', '688070.SH']
# 2021-02-23
code_list += ['688619.SH']
# 2021-02-24
code_list += ['605268.SH', '605133.SH']
# 2021-02-25
code_list += ['300948.SZ', '688183.SH']
# 2021-02-26
code_list += ['300951.SZ', '688677.SH', '300949.SZ']
# 2021-03-01
code_list += ['605060.SH', '605303.SH', '605298.SH']
# 2021-03-02
code_list += ['688079.SH']
# 2021-03-03
code_list += ['300950.SZ', '688696.SH']
# 2021-03-08
code_list += ['605208.SH', '003039.SZ']
# 2021-03-09
code_list += ['688676.SH', '688328.SH']
# 2021-03-10
code_list += ['605122.SH']
# 2021-03-11
code_list += ['688083.SH', '300952.SZ']
# 2021-03-12
code_list += ['688667.SH']
# 2021-03-16
code_list += ['688316.SH']
# 2021-03-17
code_list += ['688456.SH']
# 2021-03-18
code_list += ['300953.SZ', '688616.SH']
# 2021-03-19
code_list += ['688092.SH']
# 2021-03-22
code_list += ['300959.SZ', '605286.SH', '605389.SH', '003040.SZ']
# 2021-03-23
code_list += ['688609.SH']
# 2021-03-24
code_list += ['688633.SH', '300955.SZ']
# 2021-03-25
code_list += ['300957.SZ', '688606.SH']
# 2021-03-26
code_list += ['603759.SH', '688195.SH', '300956.SZ']
# 2021-03-29
code_list += ['300960.SZ', '688661.SH', '300958.SZ', '688329.SH']
# 2021-03-30
code_list += ['300961.SZ', '688109.SH']
# 2021-03-31
code_list += ['688659.SH', '688626.SH']
# 2021-04-01
code_list += ['688662.SH', '688630.SH']
# 2021-04-02
code_list += ['300965.SZ']
# 2021-04-06
code_list += ['003043.SZ', '003042.SZ', '003041.SZ', '688260.SH']
# 2021-04-07
code_list += ['603324.SH']
# 2021-04-08
code_list += ['688191.SH', '688636.SH']
# 2021-04-09
code_list += ['688468.SH', '300966.SZ', '300963.SZ', '300962.SZ']
# 2021-04-12
code_list += ['688683.SH', '605378.SH', '688611.SH', '300969.SZ', '300970.SZ']
# 2021-04-13
code_list += ['688663.SH', '688315.SH', '300967.SZ']
# 2021-04-15
code_list += ['300973.SZ', '300971.SZ', '601279.SH', '300968.SZ']
# 2021-04-16
code_list += ['605086.SH']
# 2021-04-19
code_list += ['688533.SH', '300976.SZ', '300972.SZ']
# 2021-04-20
code_list += ['688682.SH', '300983.SZ', '605117.SH', '300977.SZ']
# 2021-04-21
code_list += ['300975.SZ', '688201.SH', '605016.SH', '300980.SZ']
# 2021-04-22
code_list += ['688639.SH']
# 2021-04-26
code_list += ['605289.SH', '300979.SZ', '300978.SZ']
# 2021-04-27
code_list += ['300981.SZ', '605089.SH', '300982.SZ']
# 2021-04-28
code_list += ['688323.SH', '688383.SH', '001201.SZ']
# 2021-04-29 晚上加班到12点，没来得及记录
code_list += ['001202.SZ', '688395.SH', '300985.SZ']
# 2021-04-30
code_list += ['605300.SH', '300986.SZ', '605180.SH']
# 2021-05-06
code_list += ['688113.SH', '605305.SH', '605080.SH']
# 2021-05-07
code_list += ['300989.SZ', '600906.SH']
# 2021-05-10
code_list += ['001203.SZ']
# 2021-05-11
code_list += ['688655.SH', '605196.SH', '300987.SZ']
# 2021-05-12
code_list += ['688355.SH', '688097.SH', '300990.SZ', '300988.SZ']
# 2021-05-13
code_list += ['688565.SH', '605488.SH', '001205.SZ', '688685.SH']
# 2021-05-17
code_list += ['688575.SH', '688217.SH']



# code_list.sort()
print(code_list)


def get_data(param_str, index):
    # if (int(index) < 40):
    #     return
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

