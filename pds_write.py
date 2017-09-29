# np.random.seed(42)
# a = np.random.randn(34000, 59)


# df = pd.DataFrame(a)

# df.to_excel("d:\\doc\\2.xlsx", sheet_name='Random Data')
# names = open_workbook("d:\\doc\\2.xlsx").sheet_names()
# print(names)





import requests

# https://xueqiu.com/v4/stock/quote.json?code=AAPL

proxys = {
    "http": "socks5://127.0.0.1:1080",
    "https": "socks5://127.0.0.1:1080",
}

cookies = {
    # 's': 'et11g8mrsv',
    # 'webp': '0',
    # 'device_id': 'ca237e35b66e0cca74c8d637f3838796',
    # 'aliyungf_tc': 'AQAAAHLFZRAWIwcAHHg/LVSDTbGDiCSe',
    'xq_a_token': 'ed965d6ca0f68aa2f0b4a80a510e86fe5c02784d',
    # 'xq_a_token.sig': '4h-a7hDw5OAWxQatJglpF46pYf4',
    # 'xq_r_token': 'fdcc8cfbe737cc4ba5146adb235fd757dc4acc3f',
    # 'xq_r_token.sig': 'ZE73n9TV1mAyquMYb7qty1JIO_4',
    # 'u': '971506670893158',
    # '__utma': '1.1261532839.1504691419.1504771554.1506671556.3',
    # '__utmc': '1',
    # '__utmz': '1.1504691419.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    # 'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1506671330,1506671347,1506671376,1506671471',
    # 'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '150667155',
}

headers = {
    # 'Host': 'xueqiu.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}
# s=et11g8mrsv; webp=0; device_id=ca237e35b66e0cca74c8d637f3838796; aliyungf_tc=AQAAAHLFZRAWIwcAHHg/LVSDTbGDiCSe; xq_a_token=ed965d6ca0f68aa2f0b4a80a510e86fe5c02784d; xq_a_token.sig=4h-a7hDw5OAWxQatJglpF46pYf4; xq_r_token=fdcc8cfbe737cc4ba5146adb235fd757dc4acc3f; xq_r_token.sig=ZE73n9TV1mAyquMYb7qty1JIO_4; u=971506670893158; __utma=1.1261532839.1504691419.1504771554.1506671556.3; __utmc=1; __utmz=1.1504691419.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1506671330,1506671347,1506671376,1506671471; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1506671556
result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=BABA", proxies=proxys, cookies=cookies, headers=headers)
print(result.content.decode(encoding="UTF-8"))
print(result.headers)



#
# import os
# import zipfile
#
# dest_path = "d:\\doc\\quant\\"
# for filename in os.listdir("d:\\doc\\quant"):
#     fullname = "d:\\doc\\quant\\" + filename
#     sheet_names = open_workbook(fullname).sheet_names()
#     for sheet_name in sheet_names:
#         data = pd.read_excel(fullname, sheet_name)
#         base_filename = dest_path + filename[:-5] + '_' + sheet_name
#         csv_filename = base_filename + ".csv"
#         data.to_csv(csv_filename, sep='\t', header=False, index=False)
#         zip_filename = base_filename + ".zip"
#         ziphandler = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
#         ziphandler.write(csv_filename)
#         ziphandler.close()


# load data local infile 'd:\\doc\\quant\\2_20170601.csv' into table random_data(c0,c1,c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27,c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40,c41, c42, c43, c44, c45, c46, c47, c48, c49, c50, c51, c52, c53, c54, c55, c56, c57, c58)


# n = data.shape[0]
# print("rows: %s" % n)
# print(data.columns.tolist())
# print(data.shape)
# print(data.dtypes)
# for i in range(n):
#     pass
#     print(data.loc[i][0])
# print(data.keys())
# print(data)
