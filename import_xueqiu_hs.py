# -*- coding: utf-8 -*-

import os
import platform
import json
import pandas as pd

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, "data", "xueqiu", "hs", "20171017")
print(data_path)

is_windows = platform.system() == 'Windows'

command_pre = '''mysql -uquant -p123456 -h127.0.0.1 quant --local-infile=1 -e "load data local infile \''''

command_suffix = '''\' into table uqer_stock_hs(`code`, `biz_date`, `pe`, `pb`, `ps`, `pcf`)" '''


for file_name in os.listdir(data_path):
    if not file_name == '1.json':
        continue
    file = os.path.join(data_path, file_name)
    df = pd.read_json(file, encoding='utf-8', orient='index')
    print(type(df.dtypes))
    for a in df.dtypes:
        print(a)


    if is_windows:
        file = file.replace('\\', '\\\\')
    command = command_pre + file + command_suffix
    # os.system(command)

