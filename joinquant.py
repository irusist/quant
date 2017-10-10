import pandas as pd
from datetime import date, datetime, timedelta



df = pd.read_csv("all_stock.csv", encoding="utf-8")
code_list = list(df['code'])
# 20171010
code_list += ['300705.SZ', '300707.SZ']

code_list = map(lambda  x : x[:-3] + ('.XSHE' if x.endswith('SZ') else '.XSHG'), code_list)
print (code_list)

today = datetime.strftime(date.today() - timedelta(1), '%Y%m%d')

q = query(
    valuation.code, valuation.day, valuation.pe_ratio, valuation.pb_ratio, valuation.ps_ratio, valuation.pcf_ratio
).filter(valuation.code.in_(code_list)
         ).order_by(valuation.code)
df = get_fundamentals(q, today)
print(df)
print(len(df))
df.to_csv('current_pe_' + today + '.csv', sep='\t', header=False, index=False, encoding='utf-8')