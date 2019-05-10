# -*- coding: utf-8 -*-
import json
from datetime import date

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}

time = date.today().strftime("%s")


def get_data():
    result = requests.post("https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=" + time,
                           "volume=&svolume=&premium_rt=&ytm_rt=&is_search=N&btype=&listed=Y&industry=&rp=50&page=1", headers=headers)
    content = result.content.decode(encoding="UTF-8")
    data = json.loads(content, encoding='utf-8')
    # print(data['rows'])
    sum = 0
    count = 0
    lowerCount = 0
    for a in data['rows']:
        # if (a['cell']['list_dt'] is None) or (a['cell']['last_time'] is None):
        if a['cell']['last_time'] is None:
            continue
        # print(a['cell']['bond_nm'])
        price = float(a['cell']['price'])
        if price < 100:
            lowerCount += 1
        count += 1
        sum += (1.0 / float(a['cell']['price']))
    print("一共" + str(count) + "只可转债, 小于100有" + str(lowerCount) + "只，平均价格为： " + str(count / sum))


get_data()
