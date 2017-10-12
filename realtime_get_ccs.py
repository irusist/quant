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

import pandas as pd
import pymysql
import os
from datetime import date


today = date.today().strftime('%Y%m%d')
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "xueqiu", "ccs", today)
if not os.path.exists(base_path):
    os.mkdir(base_path)


mysql_cn= pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
sql = "select id, biz_date, code, name from stock_ccs where biz_date = '2017-09-29' order by code"
df = pd.read_sql(sql, mysql_cn, index_col="id")
code_list = list(df['code'])
# code_list = ['ABAC', 'ACH', 'ALN', 'AMCN', 'ATAI', 'ATHM', 'ATV', 'AXN', 'BABA', 'BCACU', 'BEDU', 'BGNE', 'BIDU', 'BITA', 'BORN', 'BRQS', 'BSPM', 'BSTI', 'BYSI', 'BZUN', 'CAAS', 'CADC', 'CALI', 'CBAK', 'CBPO', 'CCCL', 'CCCR', 'CCIH', 'CCM', 'CCRC', 'CEA', 'CEO', 'CGA', 'CHA', 'CHL', 'CHNR', 'CHU', 'CIFS', 'CJJD', 'CLDC', 'CLNT', 'CLWT', 'CMCM', 'CNET', 'CNIT', 'CNTF', 'CO', 'COE', 'CPHI', 'CREG', 'CSIQ', 'CTRP', 'CXDC', 'CYD', 'CYOU', 'DELT', 'DL', 'DQ', 'DSWL', 'EDU', 'EHIC', 'EVK', 'FANH', 'FENG', 'FFHL', 'FORK', 'FTFT', 'GDS', 'GSH', 'GSUM', 'GURE', 'HCM', 'HEBT', 'HGSH', 'HIMX', 'HLG', 'HNP', 'HOLI', 'HPJ', 'HQCL', 'HTHT', 'JASO', 'JD', 'JKS', 'JMEI', 'JMU', 'JOBS', 'JP', 'JRJC', 'KANG', 'KGJI', 'KNDI', 'KONE', 'LEJU', 'LFC', 'LITB', 'LLIT', 'MARK', 'MLCO', 'MOMO', 'MOXC', 'NCTY', 'NEWA', 'NFEC', 'NOAH', 'NQ', 'NTES', 'NTP', 'OIIM', 'ONP', 'OSN', 'PETZ', 'PME', 'PTR', 'RCON', 'RENN', 'RYB', 'SECO', 'SEED', 'SFUN', 'SGOC', 'SHI', 'SIMO', 'SINA', 'SINO', 'SKYS', 'SMI', 'SNP', 'SOHU', 'SOL', 'SORL', 'SPI', 'SSC', 'SSW', 'SVA', 'SVM', 'SYMX', 'TAL', 'TANH', 'TEDU', 'TOUR', 'TYHT', 'UTSI', 'VIPS', 'VNET', 'WB', 'WBAI', 'WINS', 'WUBA', 'XIN', 'XNET', 'XNY', 'XRF', 'YGE', 'YIN', 'YRD', 'YY', 'ZKIN', 'ZLAB', 'ZNH', 'ZPIN', 'ZTO', 'ZX']
print(code_list)
print(len(code_list))




import json


j = 0
count = 0
param = []
for code in code_list:
    count += 1
    param.append(code[:-2])
    # param.append(code)
    if count == 50:
        param_str = ','.join(param)
        param = []
        count = 0
        j += 1
        result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
        # result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers, proxies=proxys)
        # print(result.headers)
        content = result.content.decode(encoding="UTF-8")
        print(content)
        with open(os.path.join(base_path, str(j) + '.json'), 'wb') as f:
            f.write(content.encode('utf-8'))

param_str = ','.join(param)
j += 1
result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
# result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers, proxies=proxys)
# print(result.headers)
content = result.content.decode(encoding="UTF-8")
print(content)
with open(os.path.join(base_path, str(j) + '.json'), 'wb') as f:
    f.write(content.encode('utf-8'))

