create user quant identified by '123456';

grant all on *.* to quant@'%';

create database quant;

# drop table stock_hs;
# CREATE TABLE if not exists `stock_hs` (
#   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
#   `biz_date` varchar(15)  NOT NULL COMMENT '日期',
#   `code` varchar(64)  NOT NULL COMMENT '代码',
#   `name` varchar(128)  COMMENT '名称',
#   `pre_close`  decimal(20,10)  DEFAULT 0 COMMENT '前收盘价',
#   `open`  decimal(20,10)  DEFAULT 0  COMMENT '开盘价',
#   `high`  decimal(20,10)  DEFAULT 0  COMMENT '最高价',
#   `low`  decimal(20,10)  DEFAULT 0  COMMENT '最低价',
#   `close`  decimal(20,10)  DEFAULT 0  COMMENT '收盘价',
#   `change`  decimal(20,10)  DEFAULT 0  COMMENT '涨跌',
#   `pct_change`  decimal(25,15)  DEFAULT 0  COMMENT '涨跌幅',
#   `volume`  bigint(20)  DEFAULT 0  COMMENT '成交量',
#   `amount`  decimal(32,6)  DEFAULT 0  COMMENT '成交额',
#   `average`  decimal(20,10)  DEFAULT 0  COMMENT '均价',
#   `turn`  decimal(25,15)  DEFAULT 0  COMMENT '换手率',
#   `amplitude`  decimal(25,15)  DEFAULT 0  COMMENT '振幅',
#   `trade_status`  varchar(64) COMMENT '交易状态',
#   `t_num`  int(10)  DEFAULT 0  COMMENT '成交笔数',
#   `ta_factor`  decimal(25,15)  DEFAULT 0  COMMENT '复权因子（后）',
#   `buy_vol`  bigint(20)  DEFAULT 0  COMMENT '内盘成交量',
#   `sell_vol`  bigint(20) DEFAULT 0  COMMENT '外盘成交量',
#   `front_ta_factor`  decimal(25,15)  DEFAULT 0 COMMENT '前复权因子（定点复权）',
#   `is_st_stock`  varchar(16) COMMENT '是否ST',
#   `is_xst_stock`  varchar(16) COMMENT '是否*ST',
#   `mv2`  decimal(32, 6)  DEFAULT 0 COMMENT '总市值（证监会算法）',
#   `mv`  decimal(32, 6)  DEFAULT 0 COMMENT '总市值',
#   `pcf`  decimal(25, 15)  DEFAULT 0 COMMENT '市现率',
#   `pe`  decimal(25, 15)  DEFAULT 0 COMMENT '市盈率',
#   `ps`  decimal(25, 15)  DEFAULT 0 COMMENT '市销率',
#   `pb`  decimal(25, 15)  DEFAULT 0 COMMENT '市净率',
#   `dividend_yield`  decimal(25, 15)  DEFAULT 0 COMMENT '股息率',
#   `pe_ttm`  decimal(25, 15)  DEFAULT 0 COMMENT '市盈率(TTM)',
#   `ps_ttm`  decimal(25, 15)  DEFAULT 0 COMMENT '市销率(PS, TTM)',
#   `pcf_ttm`  decimal(25, 15)  DEFAULT 0 COMMENT '市现率(PCF, 现金净流量TTM)',
#   `pcf_ocf_ttm`  decimal(25, 15)  DEFAULT 0 COMMENT '市现率(PCF, 经营现金流TTM)',
#   `pcf_ocf`  decimal(25, 15)  DEFAULT 0 COMMENT '市现率(PCF, 经营现金流)',
#   `ev2`  decimal(32, 6)  DEFAULT 0 COMMENT '企业价值（剔除货币基金）（EV2）',
#   `ev1`  decimal(32, 6) COMMENT '企业价值（含货币基金）（EV1）',
#   `ev_to_ebitda`  decimal(25, 15)  DEFAULT 0 COMMENT '企业倍数（EV2/EBITDA)',
#   `ev`  decimal(32, 6)  DEFAULT 0 COMMENT '股权价值',
#   `mvb1`  decimal(32, 6)  DEFAULT 0 COMMENT 'B股市值（含限售股，折人民币）',
#   `mvb3`  decimal(32, 6)  DEFAULT 0 COMMENT 'B股市值（含限售股，交易币种）',
#   `mvb2`  decimal(32, 6)  DEFAULT 0 COMMENT 'B股市值（不含限售股，折人民币）',
#   `mvb4`  decimal(32, 6)  DEFAULT 0 COMMENT 'B股市值（不含限售股，交易币种）',
#   `mva1`  decimal(32, 6)  DEFAULT 0 COMMENT 'A股市值（含限售股）',
#   `mva2`  decimal(32, 6)  DEFAULT 0 COMMENT 'A股市值（不含限售股）',
#   `est_pe_ftm`  decimal(25, 15)  DEFAULT 0 COMMENT '预测市盈率（PE，未来12月）',
#   `est_pe`  decimal(25, 15)  DEFAULT 0 COMMENT '预测市盈率（PE，历史预测）',
#   `est_peg`  decimal(25, 15)  DEFAULT 0 COMMENT '预测PEG',
#   `pe_lyr`  decimal(25, 15)  DEFAULT 0 COMMENT '市盈率（PE, LYR)(按最新公告日）',
#   `prr_lyr`  decimal(25, 15)  DEFAULT 0 COMMENT '市研率（prr, lyr)',
#   `liq_mv`  decimal(32, 6)  DEFAULT 0 COMMENT '流通市值',
#   `last_est_dividend`  decimal(25, 15)  DEFAULT 0 COMMENT '最新股息率',
#   `pe_ttm_deducted`  decimal(25, 15)  DEFAULT 0 COMMENT '市盈率(TTM, 扣除非经常性损益)',
#   PRIMARY KEY (`id`),
#   KEY `idx_biz_date` (`biz_date`),
#   KEY `idx_code` (`code`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='沪深股票表';
#
#
#
# drop table stock_hs;
# CREATE TABLE if not exists `stock_hs` (
#   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
#   `biz_date` varchar(15)  NOT NULL COMMENT '日期',
#   `code` varchar(64)  NOT NULL COMMENT '代码',
#   `name` varchar(128)  COMMENT '名称',
#   `pre_close`  decimal(20,10)  COMMENT '前收盘价',
#   `open`  decimal(20,10)   COMMENT '开盘价',
#   `high`  decimal(20,10)   COMMENT '最高价',
#   `low`  decimal(20,10)   COMMENT '最低价',
#   `close`  decimal(20,10)  COMMENT '收盘价',
#   `change`  decimal(20,10)  COMMENT '涨跌',
#   `pct_change`  decimal(25,15)    COMMENT '涨跌幅',
#   `volume`  bigint(20)   COMMENT '成交量',
#   `amount`  decimal(32,6)   COMMENT '成交额',
#   `average`  decimal(20,10)    COMMENT '均价',
#   `turn`  decimal(25,15)   COMMENT '换手率',
#   `amplitude`  decimal(25,15)    COMMENT '振幅',
#   `trade_status`  varchar(64) COMMENT '交易状态',
#   `t_num`  int(10)    COMMENT '成交笔数',
#   `ta_factor`  decimal(25,15)   COMMENT '复权因子（后）',
#   `buy_vol`  bigint(20)   COMMENT '内盘成交量',
#   `sell_vol`  bigint(20)  COMMENT '外盘成交量',
#   `front_ta_factor`  decimal(25,15)   COMMENT '前复权因子（定点复权）',
#   `is_st_stock`  varchar(16) COMMENT '是否ST',
#   `is_xst_stock`  varchar(16) COMMENT '是否*ST',
#   `mv2`  decimal(32, 6) COMMENT '总市值（证监会算法）',
#   `mv`  decimal(32, 6)  COMMENT '总市值',
#   `pcf`  decimal(25, 15)  COMMENT '市现率',
#   `pe`  decimal(25, 15)   COMMENT '市盈率',
#   `ps`  decimal(25, 15)   COMMENT '市销率',
#   `pb`  decimal(25, 15)  COMMENT '市净率',
#   `dividend_yield`  decimal(25, 15)   COMMENT '股息率',
#   `pe_ttm`  decimal(25, 15) COMMENT '市盈率(TTM)',
#   `ps_ttm`  decimal(25, 15)  COMMENT '市销率(PS, TTM)',
#   `pcf_ttm`  decimal(25, 15)  COMMENT '市现率(PCF, 现金净流量TTM)',
#   `pcf_ocf_ttm`  decimal(25, 15)   COMMENT '市现率(PCF, 经营现金流TTM)',
#   `pcf_ocf`  decimal(25, 15)  COMMENT '市现率(PCF, 经营现金流)',
#   `ev2`  decimal(32, 6)   COMMENT '企业价值（剔除货币基金）（EV2）',
#   `ev1`  decimal(32, 6) COMMENT '企业价值（含货币基金）（EV1）',
#   `ev_to_ebitda`  decimal(25, 15)  COMMENT '企业倍数（EV2/EBITDA)',
#   `ev`  decimal(32, 6)  COMMENT '股权价值',
#   `mvb1`  decimal(32, 6)  COMMENT 'B股市值（含限售股，折人民币）',
#   `mvb3`  decimal(32, 6)   COMMENT 'B股市值（含限售股，交易币种）',
#   `mvb2`  decimal(32, 6)  COMMENT 'B股市值（不含限售股，折人民币）',
#   `mvb4`  decimal(32, 6)  COMMENT 'B股市值（不含限售股，交易币种）',
#   `mva1`  decimal(32, 6)   COMMENT 'A股市值（含限售股）',
#   `mva2`  decimal(32, 6)   COMMENT 'A股市值（不含限售股）',
#   `est_pe_ftm`  decimal(25, 15)  COMMENT '预测市盈率（PE，未来12月）',
#   `est_pe`  decimal(25, 15)  COMMENT '预测市盈率（PE，历史预测）',
#   `est_peg`  decimal(25, 15)  COMMENT '预测PEG',
#   `pe_lyr`  decimal(25, 15)   COMMENT '市盈率（PE, LYR)(按最新公告日）',
#   `prr_lyr`  decimal(25, 15)  COMMENT '市研率（prr, lyr)',
#   `liq_mv`  decimal(32, 6)   COMMENT '流通市值',
#   `last_est_dividend`  decimal(25, 15)  COMMENT '最新股息率',
#   `pe_ttm_deducted`  decimal(25, 15)  COMMENT '市盈率(TTM, 扣除非经常性损益)',
#   PRIMARY KEY (`id`),
#   KEY `idx_biz_date` (`biz_date`),
#   KEY `idx_code` (`code`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='沪深股票表';
#
#



# 沪深股票表

drop table stock_hs;
CREATE TABLE if not exists `stock_hs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `biz_date` varchar(15)  NOT NULL COMMENT '日期',
  `code` varchar(64)  NOT NULL COMMENT '代码',
  `name` varchar(128)  COMMENT '名称',
  `pre_close`  DOUBLE  COMMENT '前收盘价',
  `open`  DOUBLE   COMMENT '开盘价',
  `high`  DOUBLE   COMMENT '最高价',
  `low`  DOUBLE   COMMENT '最低价',
  `close`  DOUBLE  COMMENT '收盘价',
  `change`  DOUBLE COMMENT '涨跌',
  `pct_change`  DOUBLE    COMMENT '涨跌幅',
  `volume`  bigint(20)   COMMENT '成交量',
  `amount`  DOUBLE   COMMENT '成交额',
  `average`  DOUBLE   COMMENT '均价',
  `turn`  DOUBLE   COMMENT '换手率',
  `amplitude`  DOUBLE    COMMENT '振幅',
  `trade_status`  varchar(64) COMMENT '交易状态',
  `t_num`  int(10)    COMMENT '成交笔数',
  `ta_factor`  DOUBLE   COMMENT '复权因子（后）',
  `buy_vol`  DOUBLE   COMMENT '内盘成交量',
  `sell_vol`  DOUBLE  COMMENT '外盘成交量',
  `front_ta_factor`  DOUBLE  COMMENT '前复权因子（定点复权）',
  `is_st_stock`  varchar(16) COMMENT '是否ST',
  `is_xst_stock`  varchar(16) COMMENT '是否*ST',
  `mv2`  DOUBLE COMMENT '总市值（证监会算法）',
  `mv`  DOUBLE  COMMENT '总市值',
  `pcf`  DOUBLE  COMMENT '市现率',
  `pe`  DOUBLE   COMMENT '市盈率',
  `ps`  DOUBLE   COMMENT '市销率',
  `pb`  DOUBLE COMMENT '市净率',
  `dividend_yield`  DOUBLE   COMMENT '股息率',
  `pe_ttm`  DOUBLE COMMENT '市盈率(TTM)',
  `ps_ttm`  DOUBLE  COMMENT '市销率(PS, TTM)',
  `pcf_ttm`  DOUBLE  COMMENT '市现率(PCF, 现金净流量TTM)',
  `pcf_ocf_ttm` DOUBLE   COMMENT '市现率(PCF, 经营现金流TTM)',
  `pcf_ocf`  DOUBLE  COMMENT '市现率(PCF, 经营现金流)',
  `ev2`  DOUBLE   COMMENT '企业价值（剔除货币基金）（EV2）',
  `ev1`  DOUBLE COMMENT '企业价值（含货币基金）（EV1）',
  `ev_to_ebitda`  DOUBLE  COMMENT '企业倍数（EV2/EBITDA)',
  `ev`  DOUBLE  COMMENT '股权价值',
  `mvb1`  DOUBLE  COMMENT 'B股市值（含限售股，折人民币）',
  `mvb3`  DOUBLE   COMMENT 'B股市值（含限售股，交易币种）',
  `mvb2`  DOUBLE  COMMENT 'B股市值（不含限售股，折人民币）',
  `mvb4`  DOUBLE  COMMENT 'B股市值（不含限售股，交易币种）',
  `mva1`  DOUBLE  COMMENT 'A股市值（含限售股）',
  `mva2`  DOUBLE  COMMENT 'A股市值（不含限售股）',
  `est_pe_ftm`  DOUBLE  COMMENT '预测市盈率（PE，未来12月）',
  `est_pe`  DOUBLE  COMMENT '预测市盈率（PE，历史预测）',
  `est_peg`  DOUBLE  COMMENT '预测PEG',
  `pe_lyr`  DOUBLE   COMMENT '市盈率（PE, LYR)(按最新公告日）',
  `prr_lyr`  DOUBLE  COMMENT '市研率（prr, lyr)',
  `liq_mv`  DOUBLE   COMMENT '流通市值',
  `last_est_dividend`  DOUBLE  COMMENT '最新股息率',
  `pe_ttm_deducted`  DOUBLE  COMMENT '市盈率(TTM, 扣除非经常性损益)',
  PRIMARY KEY (`id`),
  KEY `idx_biz_date` (`biz_date`),
  KEY `idx_code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='沪深股票表';






load data local infile '/Users/zhulx/workspace/python/quant/data/hs_drop/1995_1995.csv' into table stock_hs
(`biz_date`,
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
 `amplitude`,
 `trade_status`,
 `t_num`,
 `ta_factor`,
 `buy_vol`,
 `sell_vol`,
 `front_ta_factor`,
 `is_st_stock`,
 `is_xst_stock`,
 `mv2`,
 `mv`,
 `pcf`,
 `pe`,
 `ps`,
 `pb`,
 `dividend_yield`,
 `pe_ttm`,
 `ps_ttm`,
 `pcf_ttm`,
 `pcf_ocf_ttm`,
 `pcf_ocf`,
 `ev2`,
 `ev1`,
 `ev_to_ebitda`,
 `ev`,
 `mvb1`,
 `mvb3`,
 `mvb2`,
 `mvb4`,
 `mva1`,
 `mva2`,
 `est_pe_ftm`,
 `est_pe`,
 `est_peg`,
 `pe_lyr`,
 `prr_lyr`,
 `liq_mv`,
 `last_est_dividend`,
 `pe_ttm_deducted`
);




# 香港股票表
drop table stock_hk;
CREATE TABLE if not exists `stock_hk` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `biz_date` varchar(15)  NOT NULL COMMENT '日期',
  `code` varchar(64)  NOT NULL COMMENT '代码',
  `name` varchar(128)  COMMENT '名称',
  `pre_close`  DOUBLE  COMMENT '前收盘价',
  `open`  DOUBLE   COMMENT '开盘价',
  `high`  DOUBLE   COMMENT '最高价',
  `low`  DOUBLE   COMMENT '最低价',
  `close`  DOUBLE  COMMENT '收盘价',
  `change`  DOUBLE COMMENT '涨跌',
  `pct_change`  DOUBLE    COMMENT '涨跌幅',
  `volume`  bigint(20)   COMMENT '成交量',
  `amount`  DOUBLE   COMMENT '成交额',
  `average`  DOUBLE   COMMENT '均价',
  `turn`  DOUBLE   COMMENT '换手率',
  `liq_mv`  DOUBLE   COMMENT '流通市值',
  `mv`  DOUBLE  COMMENT '总市值',
  `pcf`  DOUBLE  COMMENT '市现率',
  `pe`  DOUBLE   COMMENT '市盈率',
  `ps`  DOUBLE   COMMENT '市销率',
  `pb`  DOUBLE COMMENT '市净率',
  `dividend_yield`  DOUBLE   COMMENT '股息率',
  `pe_ttm`  DOUBLE COMMENT '市盈率(TTM)',
  `ps_ttm`  DOUBLE  COMMENT '市销率(PS, TTM)',
  `pcf_ttm`  DOUBLE  COMMENT '市现率(PCF, 现金净流量TTM)',
  `ev`  DOUBLE  COMMENT '股权价值',
  `pe_lyr`  DOUBLE   COMMENT '市盈率（PE, LYR)(按最新公告日）',
  `ps_lyr`  DOUBLE   COMMENT '市销率（PS, LYR）',
  `pcf_lyr`  DOUBLE   COMMENT '市现率（PCF, LYR）',
  `pb_mrq`  DOUBLE   COMMENT '市净率（PB, MRQ）',
  `pb_lyr`  DOUBLE   COMMENT '市净率（PB, LYR）',
  PRIMARY KEY (`id`),
  KEY `idx_stock_hk_biz_date` (`biz_date`),
  KEY `idx_stock_hk_code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='香港股票表';




load data local infile '/Users/zhulx/workspace/python/quant/data/hk/1995_1995.csv' into table stock_hk
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
  `liq_mv`,
  `mv`,
  `pcf`,
  `pe`,
  `ps`,
  `pb`,
  `dividend_yield`,
  `pe_ttm`,
  `ps_ttm`,
  `pcf_ttm`,
  `ev`,
  `pe_lyr`,
  `ps_lyr`,
  `pcf_lyr`,
  `pb_mrq`,
  `pb_lyr`
);



# 中概股
drop table stock_ccs;
CREATE TABLE if not exists `stock_ccs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `biz_date` varchar(15)  NOT NULL COMMENT '日期',
  `code` varchar(64)  NOT NULL COMMENT '代码',
  `name` varchar(128)  COMMENT '名称',
  `pre_close`  DOUBLE  COMMENT '前收盘价',
  `open`  DOUBLE   COMMENT '开盘价',
  `high`  DOUBLE   COMMENT '最高价',
  `low`  DOUBLE   COMMENT '最低价',
  `close`  DOUBLE  COMMENT '收盘价',
  `change`  DOUBLE COMMENT '涨跌',
  `pct_change`  DOUBLE    COMMENT '涨跌幅',
  `volume`  bigint(20)   COMMENT '成交量',
  `amount`  DOUBLE   COMMENT '成交额',
  `average`  DOUBLE   COMMENT '均价',
  `turn`  DOUBLE   COMMENT '换手率',
  `liq_mv`  DOUBLE   COMMENT '流通市值',
  `mv`  DOUBLE  COMMENT '总市值',
  `pcf`  DOUBLE  COMMENT '市现率',
  `pe`  DOUBLE   COMMENT '市盈率',
  `ps`  DOUBLE   COMMENT '市销率',
  `pb`  DOUBLE COMMENT '市净率',
  `dividend_yield`  DOUBLE   COMMENT '股息率',
  `pe_ttm`  DOUBLE COMMENT '市盈率(TTM)',
  `ps_ttm`  DOUBLE  COMMENT '市销率(PS, TTM)',
  `pcf_ttm`  DOUBLE  COMMENT '市现率(PCF, 现金净流量TTM)',
  `ev`  DOUBLE  COMMENT '股权价值',
  `pe_lyr`  DOUBLE   COMMENT '市盈率（PE, LYR)(按最新公告日）',
  `ps_lyr`  DOUBLE   COMMENT '市销率（PS, LYR）',
  `pcf_lyr`  DOUBLE   COMMENT '市现率（PCF, LYR）',
  `pb_mrq`  DOUBLE   COMMENT '市净率（PB, MRQ）',
  `pb_lyr`  DOUBLE   COMMENT '市净率（PB, LYR）',
  PRIMARY KEY (`id`),
  KEY `idx_stock_ccs_biz_date` (`biz_date`),
  KEY `idx_stock_ccs_code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='中概股股票表';




load data local infile '/Users/zhulx/workspace/python/quant/data/ccs/1995_1995.csv' into table stock_ccs
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
  `liq_mv`,
  `mv`,
  `pcf`,
  `pe`,
  `ps`,
  `pb`,
  `dividend_yield`,
  `pe_ttm`,
  `ps_ttm`,
  `pcf_ttm`,
  `ev`,
  `pe_lyr`,
  `ps_lyr`,
  `pcf_lyr`,
  `pb_mrq`,
  `pb_lyr`
);



# 基金
drop table fund;
CREATE TABLE if not exists `fund` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `biz_date` varchar(15)  NOT NULL COMMENT '日期',
  `code` varchar(64)  NOT NULL COMMENT '代码',
  `name` varchar(128)  COMMENT '名称',
  `pre_close`  DOUBLE  COMMENT '前收盘价',
  `open`  DOUBLE   COMMENT '开盘价',
  `high`  DOUBLE   COMMENT '最高价',
  `low`  DOUBLE   COMMENT '最低价',
  `close`  DOUBLE  COMMENT '收盘价',
  `change`  DOUBLE COMMENT '涨跌',
  `pct_change`  DOUBLE    COMMENT '涨跌幅',
  `volume`  bigint(20)   COMMENT '成交量',
  `amount`  DOUBLE   COMMENT '成交额',
  `average`  DOUBLE   COMMENT '均价',
  `turn`  DOUBLE   COMMENT '换手率',
  `unit_nav` DOUBLE COMMENT '单位净值',
  `accumulated_nav` DOUBLE COMMENT '累计单位净值',
  `adjusted_nav` DOUBLE COMMENT '复权单位净值',
  `unit_nav_rate` DOUBLE COMMENT '单位净值增长率',
  `accumulated_nav_rate` DOUBLE COMMENT '累计单位净值增长率',
  `adjusted_nav_rate` DOUBLE COMMENT '复权单位净值增长率',
  `10k_unit_yield` DOUBLE COMMENT '万份基金单位收益',
  `yield_of_7days` DOUBLE COMMENT '7日年化收益率',
  `gf_sha_price` DOUBLE COMMENT '母基金影子价格',
  `gf_all_dis_pre_rate` DOUBLE COMMENT '整体折溢价率',
  `gf_lmp_yiled` DOUBLE COMMENT '隐含收益率',
  PRIMARY KEY (`id`),
  KEY `idx_fund_biz_date` (`biz_date`),
  KEY `idx_fund_code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='基金表';



load data local infile '/Users/zhulx/workspace/python/quant/data/fund/1995_1995.csv' into table fund
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
);


# 指数基本信息
drop table index_basic_info;
CREATE TABLE if not exists `index_basic_info` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `index_code` varchar(64)  NOT NULL COMMENT '指数编码',
  `index_name` varchar(256)  COMMENT '指数名称',
  `index_series` int COMMENT '指数系列， 1 : 中证指数, 2 : 上证指数, 3 : 深证指数, 4 : 国证指数, 5 : AMAC系列指数, 6 : 中信标普指数, 7 : 中华交易系列指数, 8 : 央视财经50, 9 : 新三板系列指数',
  `assert_type` int COMMENT '资产类别，  1： 股票  2： 债券  3： 基金  4： 期货  5： 多资产  6： 区域， 7: 定制， 8： 跨境， 9： 其他',
  `index_type` int COMMENT '指数分类，  1： 股票  2： 债券  3： 基金  4： 期货  5： 多资产  6： 区域， 7: 定制， 8： 跨境， 9： 其他',
  PRIMARY KEY (`id`),
  KEY `idx_index_basic_info_index` (`index_code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='指数基本信息';



# 指数当前成分股
drop table index_constituent_current;
CREATE TABLE if not exists `index_constituent_current` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `index_code` varchar(64)  NOT NULL COMMENT '指数编码',
  `index_name` varchar(256)  COMMENT '指数名称',
  `stock_code` varchar(64)  NOT NULL COMMENT '股票编码',
  `stock_name` varchar(256)  COMMENT '股票名称',
  PRIMARY KEY (`id`),
  KEY `idx_index_constituent_current_index` (`index_code`),
  KEY `idx_index_constituent_current_stock` (`stock_code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='当前指数成分股';


# 指数成分股历史记录
drop table index_constituent_history;
CREATE TABLE if not exists `index_constituent_history` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `biz_date` varchar(15)  NOT NULL COMMENT '日期',
  `index_code` varchar(64)  NOT NULL COMMENT '指数编码',
  `index_name` varchar(256)  COMMENT '指数名称',
  `stock_code` varchar(64)  NOT NULL COMMENT '股票编码',
  `stock_name` varchar(256)  COMMENT '股票名称',
  `status` tinyint(1) COMMENT '状态， 0： 剔除， 1：纳入',
  PRIMARY KEY (`id`),
  KEY `idx_index_constituent_history_index` (`index_code`),
  KEY `idx_index_constituent_history_stock` (`stock_code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='指数成分股进出记录';

# 聚宽记录表
drop table joinquant_stock_hs;
CREATE TABLE if not exists `joinquant_stock_hs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `biz_date` varchar(15)  NOT NULL COMMENT '日期',
  `code` varchar(64)  NOT NULL COMMENT '代码',
  `pe`  DOUBLE COMMENT '市盈率',
  `pb`  DOUBLE COMMENT '市净率',
  `ps`  DOUBLE   COMMENT '市销率',
  `pcf`  DOUBLE  COMMENT '市现率',
  PRIMARY KEY (`id`),
  KEY `idx_joinquant_stock_hs_biz_date` (`biz_date`),
  KEY `idx_joinquant_stock_hs_code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='聚宽沪深股票表';