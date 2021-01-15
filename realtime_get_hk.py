import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': 'ad26f3f7a7733dcd164fe15801383e62b6033003',
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
# 2018-06-07
code_list += ['01757.HK']
# 2018-06-12
code_list += ['08403.HK']
# 2018-06-15
code_list += ['01806.HK', '08357.HK']
# 2018-06-19
code_list += ['06098.HK']
# 2018-06-21
code_list += ['02003.HK']
# 2018-06-26
code_list += ['01916.Hk']
# 2018-06-27
code_list += ['01587.HK', '08146.HK', '01749.HK']
# 2018-06-28
code_list += ['01620.HK']
# 2018-06-29
code_list += ['06100.HK']
# 2018-07-04
code_list += ['01592.HK', '08305.HK']
# 2018-07-05
code_list += ['02262.HK']
# 2018-07-06
code_list += ['01763.HK']
# 2018-07-09
code_list += ['01810.HK', '08223.HK']
# 2018-07-10
code_list += ['08502.HK', '06190.HK']
# 2018-07-11
code_list += ['01746.HK', '01652.HK']
# 2018-07-12
code_list += ['01739.HK', '01996.HK', '06860.HK', '03700.HK', '01760.HK', '01773.HK', '08219.HK', '08140.HK']
# 2018-07-13
code_list += ['01731.HK', '02051.HK', '01775.HK']
# 2018-07-16
code_list += ['01721.HK', '01715.HK', '08540.HK', '08606.HK', '01968.HK']
# 2018-07-18
code_list += ['03302.HK', '08547.HK', '08525.HK', '00797.HK']
# 2018-07-19
code_list += ['08512.HK', '01576.HK']
# 2018-07-20
code_list += ['02048.HK']
# 2018-07-31
code_list += ['01758.HK']
# 2018-08-01
code_list += ['01672.HK']
# 2018-08-03
code_list += ['01765.HK']
# 2018-08-08
code_list += ['06160.HK', '00788.HK']
# 2018-08-13
code_list += ['08475.HK']
# 2018-08-16
code_list += ['01725.HK']
# 2018-08-22
code_list += ['01783.HK']
# 2018-08-27
code_list += ['08210.HK']
# 2018-09-05
code_list += ['08482.HK']
# 2018-09-07
code_list += ['08609.HK']
# 2018-09-10
code_list += ['01615.HK']
# 2018-09-13
code_list += ['08601.HK', '01969.HK']
# 2018-09-14
code_list += ['02552.HK', '02680.HK']
# 2018-09-17
code_list += ['08619.HK']
# 2018-09-20
code_list += ['03690.HK']
# 2018-09-26
code_list += ['06862.HK', '01748.HK']
# 2018-09-27
code_list += ['01911.HK', '01723.HK']
# 2018-09-28
code_list += ['08017.HK', '01787.HK']
# 2018-10-04
code_list += ['01781.HK']
# 2018-10-08
code_list += ['01540.HK']
# 2018-10-09
code_list += ['01809.HK']
# 2018-10-11
code_list += ['01939.HK', '03990.HK', '06111.HK', '01772.HK']
# 2018-10-12
code_list += ['01894.HK', '08042.HK']
# 2018-10-15
code_list += ['08603.HK', '08516.HK']
# 2018-10-16
code_list += ['01741.HK', '08613.HK']
# 2018-10-19
code_list += ['01653.HK', '01825.HK']
# 2018-10-22
code_list += ['08611.HK']
# 2018-10-30
code_list += ['01034.HK']
# 2018-10-31
code_list += ['01801.HK']
# 2018-11-05
code_list += ['01712.HK']
# 2018-11-06
code_list += ['01755.HK']
# 2018-11-07
code_list += ['08259.HK']
# 2018-11-12
code_list += ['03616.HK']
# 2018-11-13
code_list += ['01835.HK']
# 2018-11-19
code_list += ['06890.HK', '02258.HK']
# 2018-11-26
code_list += ['00780.HK']
# 2018-11-27
code_list += ['01761.HK']
# 2018-11-29
code_list += ['01790.HK']
# 2018-12-06
code_list += ['03668.HK', '01119.HK', '02168.HK']
# 2018-12-11
code_list += ['03992.HK']
# 2018-12-12
code_list += ['08621.HK', '01860.HK', '01837.HK', '02798.HK']
# 2018-12-13
code_list += ['08622.HK', '02359.HK']
# 2018-12-14
code_list += ['01992.HK']
# 2018-12-17
code_list += ['01995.HK', '01983.HK']
# 2018-12-19
code_list += ['01675.HK']
# 2018-12-20
code_list += ['02892.HK']
# 2018-12-21
code_list += ['01762.HK', '01820.HK']
# 2018-12-24
code_list += ['01877.HK']
# 2018-12-27
code_list += ['03978.HK']
# 2018-12-28
code_list += ['01759.HK', '01713.HK']
# 2018-12-31
code_list += ['01796.HK']
# 2019-01-03
code_list += ['01845.HK']
# 2019-01-04
code_list += ['01743.HK']
# 2019-01-08
code_list += ['08631.HK']
# 2019-01-11
code_list += ['02885.HK', '02360.HK']
# 2019-01-14
code_list += ['01767.HK']
# 2019-01-15
code_list += ['02013.HK', '06162.HK', '01785.HK']
# 2019-01-18
code_list += ['01851.HK']
# 2019-01-25
code_list += ['01890.HK']
# 2019-02-04
code_list += ['01896.HK']
# 2019-02-15
code_list += ['01703.HK']
# 2019-02-19
code_list += ['08036.HK']
# 2019-02-26
code_list += ['02616.HK', '02019.HK', '08607.HK']
# 2019-02-27
code_list += ['01793.HK']
# 2019-02-28
code_list += ['01025.HK', '01872.HK']
# 2019-03-06
code_list += ['02108.HK', '01902.HK']
# 2019-03-11
code_list += ['01158.HK']
# 2019-03-14
code_list += ['01917.HK']
# 2019-03-15
code_list += ['01907.HK', '01891.HK', '01563.HK', '03316.HK', '08096.HK']
# 2019-03-18
code_list += ['02682.HK', '03662.HK']
# 2019-03-27
code_list += ['08537.HK', '06819.HK', '01865.HK']
# 2019-03-28
code_list += ['01797.HK', '06185.HK']
# 2019-04-03
code_list += ['02718.HK']
# 2019-04-16
code_list += ['02660.HK']
# 2019-04-23
code_list += ['03321.HK']
# 2019-04-25
code_list += ['01545.HK']
# 2019-04-26
code_list += ['01906.HK', '06806.HK']
# 2019-04-30
code_list += ['01780.HK']
# 2019-05-02
code_list += ['08635.HK']
# 2019-05-07
code_list += ['01753.HK']
# 2019-05-08
code_list += ['01857.HK']
# 2019-05-09
code_list += ['01873.HK']
# 2019-05-10
code_list += ['01903.HK']
# 2019-05-16
code_list += ['02346.HK', '01832.HK']
# 2019-05-21
code_list += ['02230.HK']
# 2019-05-27
code_list += ['01817.HK']
# 2019-05-28
code_list += ['02060.HK', '03868.HK']
# 2019-05-30
code_list += ['01521.HK']
# 2019-06-03
code_list += ['01905.HK']
# 2019-06-12
code_list += ['06055.HK', '00667.HK']
# 2019-06-13
code_list += ['06811.HK', '02189.HK']
# 2019-06-14
code_list += ['03692.HK']
# 2019-06-17
code_list += ['03877.HK']
# 2019-06-18
code_list += ['01935.HK']
# 2019-06-19
code_list += ['06117.HK']
# 2019-06-21
code_list += ['01769.HK']
# 2019-06-25
code_list += ['01951.HK']
# 2019-06-26
code_list += ['01849.HK']
# 2019-06-28
code_list += ['01930.HK', '01901.HK', '01943.HK', '01701.HK', '01842.HK', '01286.HK']
# 2019-07-04
code_list += ['03798.HK']
# 2019-07-05
code_list += ['00924.HK']
# 2019-07-10
code_list += ['02180.HK']
# 2019-07-11
code_list += ['01839.HK']
# 2019-07-12
code_list += ['01931.HK', '06093.HK', '01977.HK', '08612.HK']
# 2019-07-16
code_list += ['06805.HK', '01949.HK', '01134.HK', '02772.HK', '01912.HK', '00382.HK']
# 2019-07-18
code_list += ['02558.HK']
# 2019-08-16
code_list += ['01920.HK']
# 2019-08-27
code_list += ['00647.HK']
# 2019-09-19
code_list += ['03928.HK']
# 2019-09-25
code_list += ['02696.HK']
# 2019-09-26
code_list += ['08668.HK']
# 2019-09-30
code_list += ['01876.HK', '01960.HK', '03938.HK']
# 2019-10-08
code_list += ['06820.HK']
# 2019-10-10
code_list += ['06110.HK', '03601.HK']
# 2019-10-11
code_list += ['01895.HK', '08418.HK']
# 2019-10-15
code_list += ['01846.HK']
# 2019-10-16
code_list += ['01955.HK', '01582.HK']
# 2019-10-17
code_list += ['01084.HK']
# 2019-10-18
code_list += ['01967.HK', '01959.HK', '01283.HK', '02606.HK']
# 2019-10-22
code_list += ['08441.HK']
# 2019-10-23
code_list += ['01843.HK']
# 2019-10-24
code_list += ['01871.HK', '01853.HK']
# 2019-10-25
code_list += ['01692.HK']
# 2019-10-28
code_list += ['06855.HK']
# 2019-10-31
code_list += ['00302.HK', '01847.HK']
# 2019-11-01
code_list += ['01821.HK']
# 2019-11-06
code_list += ['01922.HK', '02163.HK']
# 2019-11-08
code_list += ['01875.HK', '03603.HK', '01870.HK', '01921.HK', '01987.HK', '01501.HK']
# 2019-11-11
code_list += ['01427.HK']
# 2019-11-12
code_list += ['03681.HK', '01640.HK']
# 2019-11-13
code_list += ['01401.HK', '01346.HK', '06186.HK']
# 2019-11-14
code_list += ['01747.HK', '08627.HK']
# 2019-11-15
code_list += ['02103.HK', '08617.HK', '03348.HK']
# 2019-11-21
code_list += ['02296.HK']
# 2019-11-25
code_list += ['01756.HK']
# 2019-11-26
code_list += ['09988.HK']
# 2019-11-28
code_list += ['01425.HK', '03759.HK']
# 2019-11-29
code_list += ['08208.HK']
# 2019-12-05
code_list += ['02231.HK']
# 2019-12-09
code_list += ['08645.HK']
# 2019-12-10
code_list += ['02500.HK']
# 2019-12-12
code_list += ['09966.HK', '02400.HK']
# 2019-12-13
code_list += ['06919.HK', '03680.HK', '01593.HK', '08216.HK']
# 2019-12-18
code_list += ['01691.HK', '01553.HK', '06193.HK']
# 2019-12-19
code_list += ['09928.HK', '06049.HK']
# 2019-12-30
code_list += ['09909.HK', '06199.HK']
# 2019-12-31
code_list += ['09911.HK', '01542.HK']
# 2020-01-08
code_list += ['09998.HK']
# 2020-01-10
code_list += ['09918.HK']
# 2020-01-13
code_list += ['02528.HK', '08646.HK']
# 2020-01-14
code_list += ['08500.HK', '01802.HK']
# 2020-01-15
code_list += ['09922.HK', '03718.HK', '01416.HK']
# 2020-01-16
code_list += ['09919.HK', '01740.HK', '01925.HK', '09968.HK', '01412.HK', '01525.HK', '00301.HK']
# 2020-01-17
code_list += ['01745.HK', '09938.HK', '01937.HK']
# 2020-01-21
code_list += ['01442.HK', '09933.HK', '01601.HK']
# 2020-02-14
code_list += ['09929.HK']
# 2020-02-19
code_list += ['02263.HK']
# 2020-03-09
code_list += ['09916.HK']
# 2020-03-12
code_list += ['01343.HK', '01950.HK', '01433.HK', '09936.HK']
# 2020-03-13
code_list += ['01859.HK', '01941.HK']
# 2020-03-17
code_list += ['01961.HK', '01472.HK']
# 2020-03-18
code_list += ['06918.HK', '00589.HK']
# 2020-03-23
code_list += ['09969.HK']
# 2020-03-27
code_list += ['01463.HK']
# 2020-04-15
code_list += ['06063.HK', '01942.HK', '03390.HK']
# 2020-04-20
code_list += ['08620.HK']
# 2020-04-23
code_list += ['08616.HK']
# 2020-04-24
code_list += ['09926.HK']
# 2020-04-28
code_list += ['01953.HK']
# 2020-05-07
code_list += ['01376.HK']
# 2020-05-13
code_list += ['01936.HK', '01147.HK']
# 2020-05-15
code_list += ['09983.HK', '09996.HK']
# 2020-05-18
code_list += ['08496.HK']
# 2020-05-22
code_list += ['09939.HK']
# 2020-06-01
code_list += ['09923.HK']
# 2020-06-02
code_list += ['02381.HK']
# 2020-06-03
code_list += ['01645.HK']
# 2020-06-11
code_list += ['09999.HK']
# 2020-06-18
code_list += ['09618.HK']
# 2020-06-22
code_list += ['09958.HK']
# 2020-06-29
code_list += ['09997.HK', '06078.HK']
# 2020-07-03
code_list += ['01650.HK']
# 2020-07-06
code_list += ['01502.HK']
# 2020-07-07
code_list += ['01971.HK']
# 2020-07-08
code_list += ['01957.HK', '09989.HK']
# 2020-07-10
code_list += ['01477.HK', '09979.HK', '06958.HK', '06969.HK', '08623.HK', '06978.HK', '01163.HK']
# 2020-07-13
code_list += ['08659.HK', '09906.HK']
# 2020-07-15
code_list += ['09990.HK', '09986.HK', '06968.HK', '01981.HK', '06933.HK', '01156.HK']
# 2020-07-16
code_list += ['09668.HK', '09908.HK', '09977.HK']
# 2020-07-17
code_list += ['00368.HK']
# 2020-08-06
code_list += ['01449.HK']
# 2020-08-07
code_list += ['03347.HK']
# 2020-08-14
code_list += ['09913.HK']
# 2020-09-08
code_list += ['09633.HK']
# 2020-09-10
code_list += ['09987.HK']
# 2020-09-11
code_list += ['01408.HK']
# 2020-09-15
code_list += ['01455.HK']
# 2020-09-18
code_list += ['02101.HK']
# 2020-09-22
code_list += ['01179.HK']
# 2020-09-23
code_list += ['06988.HK']
# 2020-09-25
code_list += ['00909.HK']
# 2020-09-28
code_list += ['09688.HK']
# 2020-09-29
# code_list += ['09616.HK', '01429.HK', '09991.HK', '02057.HK']
# 2020-10-07
code_list += ['06998.HK']
# 2020-10-09
code_list += ['01952.HK']
# 2020-10-12
# code_list += ['09677.HK']
# 2020-10-15
# code_list += ['02130.HK', '02115.HK']
# 2020-10-16
# code_list += ['08657.HK']
# 2020-10-19
# code_list += ['06989.HK']
# 2020-10-20
# code_list += ['02132.HK', '01597.HK']
# 2020-10-22
# code_list += ['02107.HK']
# 2020-10-23
# code_list += ['02169.HK']
# 2020-10-27
# code_list += ['02096.HK']
# 2020-10-29
# code_list += ['09993.HK']
# 2020-10-30
# code_list += ['00873.HK', '03913.HK']
# 2020-11-02
# code_list += ['09698.HK']
# 2020-11-03
# code_list += ['02126.HK']
# 2020-11-09
# code_list += ['09901.HK', '09995.HK']
# 2020-11-11
# code_list += ['01351.HK']
# 2020-11-17
# code_list += ['06900.HK', '09666.HK']
# 2020-11-18
# code_list += ['01795.HK', '02599.HK']
# 2020-11-19
# code_list += ['01516.HK']
# 2020-11-20
# code_list += ['06996.HK']
# 2020-12-02
# code_list += ['06666.HK']
# 2020-12-07
# code_list += ['02110.HK']
# 2020-12-08
# code_list += ['06618.HK']
# 2020-12-09
code_list += ['01153.HK', '01209.HK']
# 2020-12-10
code_list += ['06999.HK', '02142.HK']
# 2020-12-11
code_list += ['09992.HK', '02117.HK']
# 2020-12-16
code_list += ['06993.HK']
# 2020-12-17
code_list += ['02131.HK', '06677.HK']
# 2020-12-18
code_list += ['02148.HK']
# 2020-12-21
code_list += ['01167.HK']
# 2020-12-28
code_list += ['02135.HK']
# 2020-12-29
code_list += ['02127.HK', '01940.HK']
# 2020-12-30
code_list += ['01379.HK', '01945.HK']
# 2020-12-31
code_list += ['02156.HK']
# 2021-01-06
code_list += ['01855.HK', '09600.HK']
# 2021-01-13
code_list += ['02129.HK', '08489.HK', '02153.HK', '01440.HK']
# 2021-01-15
code_list += ['02146.HK', '01490.HK', '01643.HK', '02125.HK', '02158.HK']


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
