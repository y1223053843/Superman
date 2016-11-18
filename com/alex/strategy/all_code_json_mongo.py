#encoding=utf-8

import logging
import ConfigParser
import tushare as ts
from com.alex.utils.mongo_util import *
from com.alex.function.macd import *

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
    all_code = ts.get_stock_basics()
    all_code_index = all_code.index
    for codeItem in all_code_index:
        print "============================" + codeItem
        try:

            macd_30,macdsignal_30,macdhist_30,jsonResult_30,result_30  = MACD(codeItem,  '30')
            macd_60,macdsignal_60,macdhist_60,jsonResult_60,result_60  = MACD(codeItem,  '60')
            macd_D,macdsignal_D,macdhist_D,jsonResult_D,result_D  = MACD(codeItem,  'D')
            macd_W,macdsignal_W,macdhist_W,jsonResult_W,result_W  = MACD(codeItem,  'W')

            jsonDic = {}
            jsonDic['编码'] = codeItem
            jsonDic['名称'] = all_code.loc[codeItem,'name']
            jsonDic['所属行业'] = all_code.loc[codeItem,'industry']
            jsonDic['PE'] = all_code.loc[codeItem,'pe']

            insertRecord(dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items() + jsonResult_W.items() + jsonDic.items()))
        except (IOError, TypeError, NameError, IndexError) as e:
            logging.error("error:" + codeItem)

'''
###############################################################################
主运行函数main
###############################################################################
'''
execute()
toDataFrame({})