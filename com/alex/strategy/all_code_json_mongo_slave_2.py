#encoding=utf-8

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
from com.alex.strategy.strategy001 import *

import common

'''
##################################
常量
##################################
'''
cf = ConfigParser.RawConfigParser()
cf.read('../config/spark002_dev.conf')

'''
#################################
执行函数 execute
说明：
#################################
'''
def execute():
    time.sleep(1)
    all_code = ts.get_stock_basics()
    all_code_index = all_code[1350:1950].index
    count = 0
    all_code_index_x = num.array(all_code_index)
    for codeItem in all_code_index_x:
        #if (count == 100):
        #    break
        count = count + 1
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem + ',Count:' + str(count)
        try:
            strategy002({codeItem}, all_code.loc[codeItem,'industry'], "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
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
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====All_code_json_mongo Start====='
    #remove("report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
    execute()
    #toDataFrame({},{'01_日买入信息':'D_MACD在底部V型翻转，买入 D_最低值下穿布林线下轨，买入'},'All_Code_JSON_Mongo','All_Part_Code_JSON_Mongo')
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====All_code_json_mongo End====='