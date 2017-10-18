# -*- coding: utf-8 -*-

import os
import platform
import json
import pandas as pd
from pytz import timezone, utc
from pytz.tzinfo import StaticTzInfo
from datetime import datetime, timedelta


base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, "data", "xueqiu", "hs", "20171018")
print(data_path)

is_windows = platform.system() == 'Windows'

command_pre = '''mysql -uquant -p123456 -h127.0.0.1 quant --local-infile=1 -e "load data local infile \''''

command_suffix = '''\' into table uqer_stock_hs(`code`, `biz_date`, `pe`, `pb`, `ps`, `pcf`)" '''


class OffsetTime(StaticTzInfo):
    def __init__(self, offset):
        """A dumb timezone based on offset such as +0530, -0600, etc.
        """
        hours = int(offset[:3])
        minutes = int(offset[0] + offset[3:])
        self._utcoffset = timedelta(hours=hours, minutes=minutes)

def load_datetime(value):
    format = '%a %b %d %X %Y'
    offset = value[-10:-5:]
    value = value[:-10] + value[-4:]
    return OffsetTime(offset).localize(datetime.strptime(value, format))

def dump_datetime(value, format):
    return value.strftime(format)

for file_name in os.listdir(data_path):
    if not file_name == '1.json':
        continue
    file = os.path.join(data_path, file_name)
    df = pd.read_json(file, encoding='utf-8', orient='index')
    if 'afterHoursTime' in df.columns:
        del df['afterHoursTime']
    print(df.iloc[0].time)

    df['biz_date'] = df['time'].apply(lambda x : dump_datetime(load_datetime(x), '%Y-%m-%d'))
    print(df['biz_date'])

    if is_windows:
        file = file.replace('\\', '\\\\')
    command = command_pre + file + command_suffix
    # os.system(command)


