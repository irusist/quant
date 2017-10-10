import pandas as pd
from datetime import date, datetime

df = pd.read_csv("all_stock.csv", encoding="utf-8")
code_list = list(df['code'])
# 20171010
code_list += ['300705.SZ', '300707.SZ']
# print len(code_list)
# code_list = filter(lambda x  : not x.startswith('90') and not  x.startswith('20'), code_list)
code_list = map(lambda  x : x[:-3], code_list)

today = datetime.strftime(date.today(), '%Y%m%d')

c = 0
data_all = pd.DataFrame()
for code in code_list:
    #    print("preparing executing %s" % code)
    data = DataAPI.MktStockFactorsDateRangeGet(secID=u"",ticker=code, beginDate=today,endDate=today,field=u"ticker,tradeDate,PE,PB,PS,PCF", pandas="1")
    if len(data) == 0:
        c += 1
    data_all = data_all.append(data)

print("empty: " + str(c))
print(data_all)
print(len(data_all))
data_all.to_csv('current_pe_' + today + '.csv', sep='\t', header=False, index=False, encoding='utf-8')
print("===== finished =====")
