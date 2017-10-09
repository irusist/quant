# mysql -uquant -proot  mydb_name --local-infile=1 -e 'load data local infile "D:/ab.txt" into table mytbl(name,age)'


import os

command_pre = '''mysql -uquant -p123456 -h127.0.0.1 quant --local-infile=1 -e 'load data local infile "'''

command_suffix = '''" into table fund
(
  `biz_date`,
  `code`,
  `name`,
  `pre_close`,
  `open`,
  `high`,
  `low`,
  `close`,
  `change`,
  `pct_change`,
  `volume`,
  `amount`,
  `average`,
  `turn`,
  `unit_nav`,
  `accumulated_nav`,
  `adjusted_nav`,
  `unit_nav_rate`,
  `accumulated_nav_rate`,
  `adjusted_nav_rate`,
  `10k_unit_yield`,
  `yield_of_7days`,
  `gf_sha_price`,
  `gf_all_dis_pre_rate`,
  `gf_lmp_yiled`
)' '''

search_path = "/Users/zhulx/workspace/python/quant/data/fund/"
for filename in os.listdir(search_path):
    full_name = search_path + filename
    os.system(command_pre + full_name + command_suffix)


