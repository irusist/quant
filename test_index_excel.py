import pandas as pd

df = pd.read_excel('http://www.csindex.com.cn/uploads/file/autofile/cons/930798cons.xls', converters={4: str}, index_col=4)
exchange_list = df.iloc[:, 6]

def convert_code(dict, code):
    exchange = dict[code]
    code_len = len(code)
    if exchange == 'HKG' and code_len < 4:
        zero_len = 4 - code_len
        return '0' * zero_len + code
    return code


code_list = df.index
stock_code_list_db = map(convert_code, code_list)
print(stock_code_list_db)

