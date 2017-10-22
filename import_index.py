# -*- coding: utf-8 -*-


import os
import pandas as pd
from xlrd import open_workbook
import pyexcel as p

import pandas as pd
from xml.sax import ContentHandler, parse

import pymysql

# Reference https://goo.gl/KaOBG3
class ExcelHandler(ContentHandler):
    def __init__(self):
        self.chars = [  ]
        self.cells = [  ]
        self.rows = [  ]
        self.tables = [  ]

    def characters(self, content):
        self.chars.append(content)

    def startElement(self, name, atts):
        if name == "Cell":
            self.chars = [  ]
        elif name == "Row":
            self.cells = [  ]
        elif name == "Table":
            self.rows = [  ]

    def endElement(self, name):
        if name == "Cell":
            self.cells.append(''.join(self.chars))
        elif name == "Row":
            self.rows.append(self.cells)
        elif name == "Table":
            self.tables.append(self.rows)



base_path = '/tmp/quant/'

# 指数系列 index_series： 1 : 中证指数, 2 : 上证指数, 3 : 深证指数, 4 : 国证指数, 5 : AMAC系列指数, 6 : 中信标普指数, 7 : 中华交易系列指数, 8 : 央视财经50, 9 : 新三板系列指数
# 资产类别 assert_type:  1： 股票  2： 债券  3： 基金  4： 期货  5： 多资产  6： 区域， 7: 定制， 8： 跨境， 9： 其他
# 指数分类 index_type   1： 综合  2：规模  3：行业  4：风格  5：主题  6：策略  7：综合债  8：信用债  9：利率债  10：可转债  11：其他

i = 0
for file_name in os.listdir(base_path):
    i += 1
    index_series = 1
    assert_type = 1
    index_type = 5
    index_code = file_name
    constituent_file = base_path + index_code + "/" + "成份及权重.xls"
    # csv_file = base_path + index_code + "/aaa.csv"

    # if index_code != '000918':
    #     break

    if index_code == '.DS_Store':
        continue

    print("preparing to execute %s" % index_code)

    conn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
    cursor = conn.cursor()

    sql = "insert into index_basic_info (index_code, index_series, assert_type, index_type) values (%s, %s, %s, %s) "

    # 入库
    cursor.execute(sql, [index_code, index_series, assert_type, index_type])
    # 提交
    conn.commit()


    if os.path.exists(constituent_file):
        excelHandler = ExcelHandler()
        parse(constituent_file, excelHandler)
        df1 = pd.DataFrame(excelHandler.tables[0][1:], columns=excelHandler.tables[0][0])

        # df1.to_csv(csv_file, encoding='utf-8', index=False, header=False)
        print(index_code)
        df = df1[[u'代码', u'简称']]
        # data = pd.read_excel(constituent_file, None,)
        # print(df)


        param = []
        if len(df) > 1:
            for i in range(len(df)):
                element = tuple(df.iloc[i])
                element = (index_code,) + element
                param.append(element)  # 转成list_tuple格式
        if len(df)==1:
            element = tuple(df.iloc[0])
            element = (index_code, ) + element
            param = [element]

        # print(param.encode('utf8'))
        # with open('/Users/zhulx/tmp/a.txt', 'wb') as f:
        #     f.write(str(param))

        sql = "insert into index_constituent_current (index_code, stock_code, stock_name) values (%s, %s, %s) "

        # 入库
        cursor.executemany(sql, param)
        # 提交
        conn.commit()
    else:
        print("not exists file: %s" % constituent_file)

    # sql = "select id, biz_date, code, name from stock_hs where biz_date = '2017-09-29'"
    # df = pd.read_sql(sql, mysql_cn, index_col="id")
    # code_list = list(df['code'])
    # print len(code_list)
    # code_list = filter(lambda x  : not x.startswith('90') and not  x.startswith('20'), code_list)
    # code_list = map(lambda  x : x[:-3], code_list)
    # print len(code_list)

    history_file = base_path + index_code + "/" + "成份进出记录.xls"
    if os.path.exists(history_file):
        excelHandler = ExcelHandler()
        parse(history_file, excelHandler)
        df1 = pd.DataFrame(excelHandler.tables[0][1:], columns=excelHandler.tables[0][0])
        df1[u'状态'] = (df1[u'状态'] == u'纳入').astype(int)
        # df1.to_csv(csv_file, encoding='utf-8', index=False, header=False)
        # print(df1)


        param = []
        if len(df1) > 1:
            for i in range(len(df1)):
                element = list(df1.iloc[i])
                element.insert(0, index_code)
                element[-1] = int(element[-1])
                param.append(element)  # 转成list_tuple格式
        if len(df1)==1:
            element = list(df1.iloc[0])
            element.insert(0, index_code)
            # element = (index_code, ) + element
            element[-1] = int(element[-1])
            param = [element]
        # print param

        sql = "insert into index_constituent_history (index_code, biz_date, stock_code, stock_name, status) values (%s, %s, %s, %s, %s) "

        # 入库
        cursor.executemany(sql, param)
        # 提交
        conn.commit()
    else:
        print "not exists file: %s" % history_file

    cursor.close()
