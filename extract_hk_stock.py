import os
import json
import pandas as pd

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, "data", "xueqiu", 'ccs', '20171010')
print(data_path)

code_list = []
for file_name in os.listdir(data_path):
    file = os.path.join(data_path, file_name)
    df = pd.read_json(file)
    code_list += list(df.loc['symbol'])
    # print(list(df['symbol']))
    # with open(file, 'r', encoding='utf-8') as f:
    #     json_str = f.read()
    #     json_data = json.loads(json_str, encoding='utf-8')
    #     print(json_data)

print(code_list)
print(len(code_list))

