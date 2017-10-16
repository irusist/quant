import pandas as pd
from datetime import date, datetime, timedelta

today = datetime.strftime(date.today(), '%Y%m%d')

# A股所有代码
code_df = DataAPI.MktEqudGet(tradeDate=today,isOpen="",field=u"ticker",pandas="1")
code_list = list(code_df['ticker'])

# df = pd.read_csv("all_stock.csv", encoding="utf-8")
# code_list = list(df['code'])
# 20171010
# code_list += ['300705.SZ', '300707.SZ']
# 2017-10-12
# code_list += ['603103.SH']
# 2017-10-13
# code_list += ['002903.SZ', '603110.SH', '002906.SZ']

# print len(code_list)
# code_list = filter(lambda x  : not x.startswith('90') and not  x.startswith('20'), code_list)
# code_list = map(lambda  x : x[:-3], code_list)

data_all = pd.DataFrame()
for code in code_list:
    #    print("preparing executing %s" % code)
    data = DataAPI.MktStockFactorsDateRangeGet(secID=u"",ticker=code, beginDate=today,endDate=today,field=u"ticker,tradeDate,PE,PB,PS,PCF", pandas="1")
    data_all = data_all.append(data)

print(data_all)
print(len(data_all))
data_all.to_csv('current_pe_' + today + '.csv', sep='\t', header=False, index=False, encoding='utf-8')
print("===== finished =====")
