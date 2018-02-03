# -*- coding: utf-8 -*-


import pandas as pd
import pymysql
import urllib2


conn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')


# 深圳指数，国证指数
# 去掉债券， 多资产， 基金
# TODO 央视系列的没有跟踪标的， 暂时不做处理
# sql = "select id, index_code from index_basic_info where index_series in (8) order by index_code "
sql = "select id, index_code from index_basic_info where index_series in (3, 4) and (assert_type not in (2, 3, 5) or assert_type is null) order by index_code "
df = pd.read_sql(sql, conn, index_col="id")
index_code_list = list(df['index_code'])
print(len(index_code_list))
# TODO 去掉不一致的，暂时不能获取最新的成分股进出记录，先去掉
# 399103   深证乐富基金指数
# 399231   农林牧渔指数
# 399232   采矿业指数
# 399235   建筑业指数
# 399236   批发零售指数
# 399237   运输仓储指数
# 399238   餐饮指数
# 399239   IT指数
# 399240   金融指数
# 399241   房地产业指数
# 399242   商务服务指数
# 399243   科研服务指数
# 399244   公共环保指数
# 399248   文化传播指数
code_not_equals_wind_csindex = ['399103', '399231', '399232', '399235', '399236', '399237', '399238', '399239',
                                '399240', '399241', '399242', '399243', '399244', '399248', '399303', '399311',
                                '399316', '399317', '399318', '399352', '399354', '399370', '399376', '399378',
                                '399383', '399385', '399401', '399418', '399427', '399428', '399635', '399678',
                                '399690', '399692', '399694', '399699', 'CN5073', 'CN5074', 'CN5075', 'CN5076',
                                'CN5077', 'CN5078', 'CN5079', 'CN5080', 'CN5081', 'CN5082', 'CN5083', 'CN5084',
                                'CN5085', 'CN5086', 'CN5087', 'CN5088', 'CN5089', 'CN5090', 'CN5091', 'CN5092',
                                'CN5093', 'CN5094', 'CN5095', 'CN5096', 'CN5097', 'CN5098', 'CN5099', 'CN5100',
                                'CN5101', 'CN5102', 'CN5103', 'CN5104', 'CN5105', 'CN5106', 'CN5107', 'CN5108',
                                'CN5110', 'CN5122', 'CN5123', 'CN5124', 'CN5125', 'CN5126', 'CN5127', 'CN5128',
                                'CN5129', 'CN5130', 'CN5131', 'CN6001', 'CN6002', 'CN6003', 'CN6004', 'CN6005',
                                'CN6006', 'CN6007', 'CN6008', 'CN6009', 'CN6010', 'CN6011', 'CN6012', 'CN6013',
                                'CN6014', 'CN6015', 'CN6016', 'CN6017', 'CN6018', 'CN6019', 'CN6020', 'CN6021',
                                'CN6022', 'CN6023', 'CN6024', 'CN6025', 'CN6026', 'CN6027', 'CN6028', 'CN6029',
                                'CN6030', 'CN6031', 'CN6032', 'CN6033', 'CN6034', 'CN6036', 'CN6037', 'CN6039',
                                'CN6041', 'CN6042', 'CN6043', 'CN6044', 'CN6045', 'CN6046', 'CN6047', 'CN6048',
                                'CN6049', 'CN6050', 'CN6051', 'CN6052', 'CN6053', 'CN6054', 'CN6055', 'CN6056',
                                'CN6057', 'CN6058', 'CN6059', 'CN6060', 'CNG10001', 'CNG10005']


# TODO 399415 I100 有标的， wind无变化， 官网有变化！！！
# TODO 399416 I300 有标的， wind无变化， 官网有变化！！！
# TODO 399422 中关村A指  有标的， wind无变化， 官网有变化
# TODO 399632 深100EW  有标的， wind没历史数据， 官网有变化
# TODO 399633 深证300等权重指数  有标的， wind没历史数据， 官网有变化
# TODO 399634 中小板等权重指数  有标的， wind没历史数据， 官网有变化
# TODO 399656 深证100绩效加权指数  无标的， wind没有历史数据， 官网有变化
# TODO 399657 深证300绩效加权指数  无标的， wind没有历史数据， 官网有变化
# TODO 399658 中小板绩效加权指数  无标的， wind没有历史数据， 官网有变化
# TODO 399659 深证成份等权  无标的， wind没有历史数据， 官网有变化
# TODO 399660 中创100等权  无标的， wind没有历史数据， 官网有变化
# TODO 399691 深证创业板专利领先指数  无标的， wind没有变化， 官网有变化

index_code_list = list(set(index_code_list).difference(set(code_not_equals_wind_csindex)))
index_code_list.sort()

print("found %s index from db" % str(len(index_code_list)))

def convert_code(code):
    code_len = len(str(code))
    if code_len < 4:
        zero_len = 4 - code_len
        return '0' * zero_len + code
    return code


def remove_suffix(code):
    index = code.find('.')
    if index > 0:
        return code[0:index]
    return code


def get_stock_code_from_db(code):
    # sql = "select id, code from stock_hs where biz_date='2017-09-29' and trade_status not in ('终止上市', '暂停上市') and code not like '90%' and code not like '20%' order by code"
    # get index constituent from database
    sql = "select id, stock_code from index_constituent_current where index_code = '" + code + "'"
    df = pd.read_sql(sql, conn, index_col="id")
    stock_code_list_db = list(df['stock_code'])

    stock_code_list_db = map(remove_suffix, stock_code_list_db)
    stock_code_list_db = set(stock_code_list_db)
    return stock_code_list_db


def append_suffix(code):
    if code.startswith('60') or code.startswith('90'):
        return code + '.SH'
    elif code.startswith('00') or code.startswith('20') or code.startswith('30'):
        return code + '.SZ'

def update(index_code):
    # get stock code from db
    stock_code_list_db = get_stock_code_from_db(index_code)

    # get index constituent from csindex website
    try:
        df = pd.read_excel('http://www.cnindex.com.cn/docs/yb_' + index_code + '.xls', converters={2: str})
        df = df.set_index(df.columns[2])
    except urllib2.HTTPError as error:
        db_len = len(stock_code_list_db)
        if db_len == 0:
            # maybe 404 error
            print('index %s occurs exception: %s, db size is 0' % (index_code, str(error)))
        else:
            print('index %s occurs exception: %s, db size is %s' % (index_code, str(error), str(db_len)))
        return
    except StandardError as error:
        print('index %s occurs exception: %s' % (index_code, str(error)))
        return

    stock_name_list = df.iloc[:, 3]
    stock_code_list_new = df.index
    stock_code_list_new = map(convert_code, stock_code_list_new)
    stock_code_list_new = set(stock_code_list_new)

    # to be added
    stock_code_add = stock_code_list_new.difference(stock_code_list_db)
    # to be removed
    stock_code_remove = stock_code_list_db.difference(stock_code_list_new)

    if len(stock_code_remove) > 0:
        print("index %s to be removed %s" % (index_code, stock_code_remove))
    if len(stock_code_add) > 0:
        print("index %s to be added %s" % (index_code, stock_code_add))
        # for code in stock_code_add:
        #     cursor = conn.cursor()
        #     sql = "insert into index_constituent_current (index_code, stock_code, stock_name) values (%s, %s, %s) "
        #     # 入库
        #     cursor.execute(sql, [index_code, append_suffix(code, exchange_list[code]), stock_name_list[code]])
        #     # 提交
        #     conn.commit()
        #     sql = "insert into index_constituent_history (index_code, biz_date, stock_code, stock_name, status) values (%s, %s, %s, %s, %s) "
        #     # 入库
        #     cursor.execute(sql, [index_code, '2017-10-30', append_suffix(code, exchange_list[code]), stock_name_list[code], '1'])
        #     # 提交
        #     conn.commit()
        # cursor.close()


# start = time.time()
# pool = threadpool.ThreadPool(10)
# requests = threadpool.makeRequests(update, index_code_list)
# [pool.putRequest(req) for req in requests]
# pool.wait()
for index_code in index_code_list:
    update(index_code)

