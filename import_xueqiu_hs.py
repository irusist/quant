# -*- coding: utf-8 -*-

import os
import platform
import json
import pandas as pd
from pytz import timezone, utc
from pytz.tzinfo import StaticTzInfo
from datetime import datetime, timedelta
import migrate


base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, "data", "xueqiu", "hs")
backup_path = os.path.join(base_path, "backup", "xueqiu", "hs")
print(data_path)

is_windows = platform.system() == 'Windows'

command_pre = '''mysql -uquant -p123456 -h127.0.0.1 quant --local-infile=1 -e 'load data local infile "'''

command_suffix = '''" into table xueqiu_hs(
    `afterHours`,`afterHoursChg`,`afterHoursPct`,`after_hour_vol`,`amount`,`amplitude`,
    `benefit_after_tax`,`benefit_before_tax`,`beta`,`biz_date`,`bond_type`,`change`,`circulation`,`close`,`code`,`convert_bond_ratio`,
    `convert_rate`,`convertrate`,`currency_unit`,`current`,`disnext_pay_date`,`dividend`,`due_date`,`due_time`,`eps`,`exchange`,
    `fall_stop`,`flag`,`float_market_capital`,`float_shares`,`has_warrant`,`hasexist`,`high`,`high52week`,`instOwn`,`interestrtmemo`,
    `issue_type`,`kzz_convert_price`,`kzz_convert_time`,`kzz_covert_value`,`kzz_cpr`,`kzz_putback_price`,`kzz_redempt_price`,
    `kzz_stock_current`,`kzz_stock_name`,`kzz_stock_percent`,`kzz_stock_symbol`,`kzz_straight_price`,`last_close`,`lot_size`,
    `lot_volume`,`low`,`low52week`,`marketCapital`,`market_status`,`maturitydate`,`max_order_quantity`,`min_order_quantity`,
    `name`,`net_assets`,`open`,`outstandingamt`,`pankou_ratio`,`par_value`,`pb`,`pe_lyr`,`pe_ttm`,`percent5m`,`percentage`,
    `psr`,`publisher`,`rate`,`redeem_type`,`release_date`,`remain_year`,`rest_day`,`rise_stop`,`sale_rrg`,`symbol`,`tick_size`,
    `time`,`totalShares`,`totalissuescale`,`turnover_rate`,`type`,`updateAt`,`value_date`,`variable_tick_size`,`volume`,
    `volumeAverage`,`volume_ratio`,`warrant`,`yield`)' '''

if is_windows:
    command_pre = '''mysql -uquant -p123456 -h127.0.0.1 quant --local-infile=1 -e "load data local infile \''''
    command_suffix = '\' into table xueqiu_hs('
    command_suffix += '`afterHours`,`afterHoursChg`,`afterHoursPct`,`after_hour_vol`,`amount`,`amplitude`,'
    command_suffix += '`benefit_after_tax`,`benefit_before_tax`,`beta`,`biz_date`,`bond_type`,`change`,`circulation`,`close`,`code`,`convert_bond_ratio`,'
    command_suffix += '`convert_rate`,`convertrate`,`currency_unit`,`current`,`disnext_pay_date`,`dividend`,`due_date`,`due_time`,`eps`,`exchange`,'
    command_suffix += '`fall_stop`,`flag`,`float_market_capital`,`float_shares`,`has_warrant`,`hasexist`,`high`,`high52week`,`instOwn`,`interestrtmemo`,'
    command_suffix += '`issue_type`,`kzz_convert_price`,`kzz_convert_time`,`kzz_covert_value`,`kzz_cpr`,`kzz_putback_price`,`kzz_redempt_price`,'
    command_suffix += '`kzz_stock_current`,`kzz_stock_name`,`kzz_stock_percent`,`kzz_stock_symbol`,`kzz_straight_price`,`last_close`,`lot_size`,'
    command_suffix += '`lot_volume`,`low`,`low52week`,`marketCapital`,`market_status`,`maturitydate`,`max_order_quantity`,`min_order_quantity`,'
    command_suffix += '`name`,`net_assets`,`open`,`outstandingamt`,`pankou_ratio`,`par_value`,`pb`,`pe_lyr`,`pe_ttm`,`percent5m`,`percentage`,'
    command_suffix += '`psr`,`publisher`,`rate`,`redeem_type`,`release_date`,`remain_year`,`rest_day`,`rise_stop`,`sale_rrg`,`symbol`,`tick_size`,'
    command_suffix += '`time`,`totalShares`,`totalissuescale`,`turnover_rate`,`type`,`updateAt`,`value_date`,`variable_tick_size`,`volume`,'
    command_suffix += '`volumeAverage`,`volume_ratio`,`warrant`,`yield`)" '


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


def get_oneday_data(one_day_path):
    print("preparing to execute: %s" % one_day_path)
    df = pd.DataFrame()
    for file_name in os.listdir(one_day_path):
        # if not file_name == '1.json':
        #     continue
        file = os.path.join(one_day_path, file_name)
        df_tmp = pd.read_json(file, encoding='utf-8', orient='index', dtype={'code':str})
        if 'afterHoursTime' in df_tmp.columns:
            del df_tmp['afterHoursTime']
        # print(df_tmp.iloc[0].time)

        try:
            df_tmp['biz_date'] = df_tmp['time'].apply(lambda x : dump_datetime(load_datetime(x), '%Y-%m-%d'))
        except ValueError as error:
            print("================ error ", file_name, "===================")
        df = df.append(df_tmp)
        # print(df['biz_date'])
        # print(df['code'])
        # print(dump_datetime(load_datetime('Tue Oct 10 10:07:04 -0400 2017'), '%Y-%m-%d'))
        # print(df.columns)
        # print(df)
        # print(datetime.strptime('Tue Oct 10 10:07:04 -0400 2017', '%a %b %d %X %z %Y'))
    return df


def import_db():
    for path in os.listdir(data_path):
        csv_file = os.path.join(base_path, "tmp", "tmp.csv")
        child_path = os.path.join(data_path, path)
        df = get_oneday_data(child_path)
        df.to_csv(csv_file, sep='\t', header=False, index=False, encoding='utf-8')
        if is_windows:
            csv_file = csv_file.replace('\\', '\\\\')
        command = command_pre + csv_file + command_suffix
        os.system(command)
        dest = os.path.join(backup_path, path)
        migrate.move(child_path, dest)

if __name__ == '__main__':
    import_db()



