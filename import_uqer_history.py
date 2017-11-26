# -*- coding: utf-8 -*-

import os
import pandas as pd

data_path = "/Users/zhulx/workspace/python/tmp_data"
print(data_path)

command_pre = '''mysql -uquant -p123456 -h127.0.0.1 quant --local-infile=1 -e 'load data local infile "'''
command_suffix = '''" into table uqer_stock_hs(
    `code`,
    `biz_date`,
    `pe`,
    `pb`,
    `ps`,
    `pcf`)' '''

for file_name in os.listdir(data_path):
    file = os.path.join(data_path, file_name)
    data_all = pd.read_csv(file, index_col=0, converters={1:str})
    data_all.to_csv('n_history_1.csv', sep='\t', header=False, index=False, encoding='utf-8')
    command = command_pre + 'n_history_1.csv' + command_suffix
    print(command)
    os.system(command)

