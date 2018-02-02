# -*- coding: utf-8 -*-


import pandas as pd
import pymysql
import urllib2


conn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')


# 中证指数
# 去掉债券， 多资产， 基金
# sql = "select id, index_code from index_basic_info where index_series = 1 and assert_type not in (2, 3, 5) order by index_code"
# TODO 新三板指数  899001  899002 没有跟踪标的， 暂时不做处理
# TODO 中华交易系列指数， 8个， 没有跟踪标的， 暂不处理
# TODO AMAC系列指数 没有跟踪标的， 暂不处理
# sql = "select id, index_code from index_basic_info where index_series = 5 order by index_code "


# 上证指数
sql = "select id, index_code from index_basic_info where index_series in (1, 2)  and assert_type not in (2, 3, 5) order by index_code "
df = pd.read_sql(sql, conn, index_col="id")
index_code_list = list(df['index_code'])
print(len(index_code_list))
# TODO  固定债券
# index_code_list = ['000832', '000833', '000845','000923','930780','930786','930787','930788','930823',
#     '930824','930825','930826','930827','930828','930829','930830','930831','930832','930833','930834',
#     '930849','930865','930866','930870','930871','930872','930873','930874','930909','930916','930951',
#     '930954','930996','931010','H11001', 'H11002','H11003','H11004','H11005','H11006','H11007','H11008',
#     'H11009','H11010','H11014','H11015','H11016','H11017','H11019','H11070','H11071','H11072','H11073',
#     'H11074','H11075','H11076','H11078','H11079','H11087','H11088','H11089','H11090','H11091','H11092',
#     'H11093','H11094','H11096','H11097','H11099','H11185','H30396', 'H30521']

# TODO 去掉不一致的，暂时不能获取最新的成分股进出记录，先去掉
code_not_equals_wind_csindex = ['000891', '930667', '930764', '930794', '930798', '930802', '930899', '930912', '930914', '930917',
    '930919', '930921',  '930930', '930932', '930945', '930957', '930959', '930960', '930961', '930962', '930963', '930964',
                                '930965', '930966', '930967', '930968', '930969', 'H11100', 'H11102', 'H11104',
                                'H11105', 'H11106', 'H11108', 'H11113', 'H11123', 'H11132', 'H11134', 'H11136',
                                'H11140', 'H11152', 'H11156', 'H11160', 'H11162', 'H11167', 'H11181', 'H11183',
                                'H30103', 'H30107', 'H30131', 'H30133', 'H30135', 'H30232', 'H30233', 'H30236',
                                'H30238', 'H30251', 'H30252', 'H30255', 'H30257', 'H30369', 'H30374', 'H30375',
                                'H30376', 'H30377', 'H30378', 'H30379', 'H30380', 'H30381', 'H30382', 'H30383',
                                'H30384', 'H30418', 'H30422', 'H30457', 'H30464', 'H30484', 'H30533', 'H30547',
                                'H30551', 'H30564']

# joinquant有数据，由于没有跟踪标的，以下内容暂时不补齐，等有时间再补齐
# 000902  中证流通
# 000926  中证央企
# 000938  中证名企
# 000953  中证地企
# 000955  中证国企
code_not_equals_wind_csindex += ['000902', '000926', '000938', '000953', '000955']

# 950090 50AH优选 wind不正确
# H50069  上证港股通指数，  wind不正确
code_not_equals_wind_csindex += ['950090', 'H50069']
index_code_list = list(set(index_code_list).difference(set(code_not_equals_wind_csindex)))
index_code_list.sort()

print("found %s index from db" % str(len(index_code_list)))

def convert_code(code, exchange):
    code_len = len(str(code))
    if exchange == 'HKG' and code_len < 4:
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


def append_suffix(code, exchange):
    if exchange == 'SHH':
        return code + '.SH'
    elif exchange == 'SHZ':
        return code + '.SZ'
    elif exchange == 'CPT':
        return code + '.IB'

def update(index_code):
    # print("index_code: " + index_code)
    # get stock code from db
    stock_code_list_db = get_stock_code_from_db(index_code)

    # get index constituent from csindex website
    try:
        df = pd.read_excel('http://www.csindex.com.cn/uploads/file/autofile/cons/' + index_code + 'cons.xls', converters={4: str})
        df = df.set_index(df.columns[4])
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

    exchange_list = df.iloc[:, 6]
    stock_name_list = df.iloc[:, 4]
    stock_code_list_new = df.index
    stock_code_list_new = map(convert_code, stock_code_list_new, exchange_list)
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

