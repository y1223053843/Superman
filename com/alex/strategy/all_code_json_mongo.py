# encoding=utf-8

import sys

sys.path.append('/root/worksapce/Superman')
import logging
import ConfigParser
import tushare as ts
import time
import numpy as num
from com.alex.utils.mongo_util import *
from com.alex.function.macd import *
from com.alex.function.ma import *
from com.alex.function.liang import *
from com.alex.function.bbands import *
import common
from com.alex.strategy.strategy001 import *
import re

'''
##################################
常量
##################################
'''
cf = ConfigParser.RawConfigParser()
# cf.read('../config/spark002_dev.conf')

'''
#################################
执行函数 execute
说明：
#################################
'''
def execute():
    all_code = ts.get_stock_basics()
    all_code_index = all_code[1:750].index
    count = 0
    all_code_index_x = num.array(all_code_index)
    for codeItem in all_code_index_x:
        count = count + 1
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem + ',Count:' + str(
            count)
        try:
            strategy002({codeItem}, all_code.loc[codeItem, 'industry'],
                        "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
        except (IOError, TypeError, NameError, IndexError, Exception) as e:
            print e
            logging.error("error:" + codeItem)


'''
###############################################################################
主运行函数main
###############################################################################
'''
param = sys.argv[0]
if (param == 1):
    print 'param:' + param
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '=====All_code_json_mongo Start====='
    remove("report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
    execute()
    rexExp1 = re.compile('^20*')
    rexExp2 = re.compile('^.*买入.*')
    rexExp3 = re.compile('^[\s]*$')
    # 策略1
    toDataFrame({}, {'$or': [{'00_20天线信息': rexExp1, '01_日买入信息': rexExp2, '02_卖出信息': rexExp3, 'MACD_Z_W': '[V]'},
                             {'00_20天线信息': rexExp1, '01_日买入信息': rexExp2, '02_卖出信息': rexExp3, 'MACD_Z_W': '[/]'},
                             {'04_Code': {'$in': [u'000001', u'399001', u'399006']}, '07_所属行业': {'$exists': False}},
                             {'04_是否持有': 'yes'}]}, 'All_Code_JSON_Mongo', 'S1：:20 days upper，888 signal')

    # 策略2
    toDataFrame_param({'$or': [{'MACD_Z_W': '[V]'}, {'MACD_Z_W': '[/]'},
                               {'04_Code': {'$in': [u'000001', u'399001', u'399006']}, '07_所属行业': {'$exists': False}},
                               {'04_是否持有': 'yes'}]}, 'S2：week upper',
                      "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))

    # 策略3
    toDataFrame_param({'$or': [{'00_10天线信息': rexExp1, '00_20天线信息': rexExp1, '00_60分钟信息': rexExp1, '02_卖出信息': rexExp3},
                               {'04_Code': {'$in': [u'000001', u'399001', u'399006']}, '07_所属行业': {'$exists': False}},
                               {'04_是否持有': 'yes'}]}, 'S3：5、10、20 days upper',
                      "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))

    # toDataFrame({},{'00_20天线信息' : rexExp1, '01_日买入信息': rexExp2},'All_Code_JSON_Mongo','All_Part_Code_JSON_Mongo')
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '=====All_code_json_mongo End====='
