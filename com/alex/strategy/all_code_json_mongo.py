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
from com.alex.function.bbands import *
import common
import re

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
    all_code_index = all_code[1:1000].index
    count = 0
    all_code_index_x = num.array(all_code_index)
    zhishu_code_index = num.array(['399006','399001','000001'])
    for codeItem in all_code_index_x:
        #if (count == 100):
        #    break
        count = count + 1
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem + ',Count:' + str(count)
        try:

            #macd_30,macdsignal_30,macdhist_30,jsonResult_30,result_30,mairuresult_30,maichuresult_30  = MACD(codeItem,  '30')
            macd_60,macdsignal_60,macdhist_60,jsonResult_60,result_60,mairuresult_60,maichuresult_60  = MACD(codeItem,  '60')
            macd_D,macdsignal_D,macdhist_D,jsonResult_D,result_D,mairuresult_D,maichuresult_D  = MACD(codeItem,  'D')
            #macd_W,macdsignal_W,macdhist_W,jsonResult_W,result_W,mairuresult_W,maichuresult_W  = MACD(codeItem,  'W')
            #upperband_30, middleband_30, lowerband_30, jsonResult_b_30, result_bl_30,mairuresult_bl_30,maichuresult_bl_30 = BBANDS(codeItem, '30')
            upperband_60, middleband_60, lowerband_60, jsonResult_b_60, result_bl_60,mairuresult_bl_60,maichuresult_bl_60 = BBANDS(codeItem, '60')
            upperband_D, middleband_D, lowerband_D, jsonResult_b_D, result_bl_D,mairuresult_bl_D,maichuresult_bl_D = BBANDS(codeItem, 'D')
            #upperband_W, middleband_W, lowerband_W, jsonResult_b_W, result_bl_W,mairuresult_bl_W,maichuresult_bl_W = BBANDS(codeItem, 'W')
            real_D,tableresult_ma_d_20 = MA(codeItem, 'D', 20)
            real_60,tableresult_ma_60_20 = MA(codeItem, '60', 20)

            jsonDic = {}
            jsonDic['00_20天线信息'] =  tableresult_ma_d_20
            jsonDic['00_60分钟信息'] =  tableresult_ma_60_20
            jsonDic['01_日买入信息'] =  mairuresult_D + ' ' + mairuresult_bl_D
            jsonDic['01_时买入信息'] =  mairuresult_60 + ' ' + mairuresult_bl_60
            jsonDic['02_卖出信息'] = maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            jsonDic['03_上升通道'] = result_D + ' ' + result_bl_D
            jsonDic['04_Code'] = codeItem
            jsonDic['04_是否持有'] = common.shifouchiyou(codeItem)
            jsonDic['05_Name'] = common.gupiaomingcheng(codeItem)
            jsonDic['06_涨跌幅'] = common.zhangdiefu(codeItem)
            jsonDic['07_所属行业'] = all_code.loc[codeItem,'industry']

            jsonDic['90_Time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            jsonDic['91_PE'] = all_code.loc[codeItem,'pe']
            #jsonDic['验证_MACD_30'] =  '%.3f' % macd_30[-1] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-3]
            #jsonDic['验证_MACD_60'] =  '%.3f' % macd_60[-1] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-3]
            #jsonDic['验证_MACD_D'] =  '%.3f' % macd_D[-1] + '_' +  '%.3f' % macd_D[-2] + '_' +  '%.3f' % macd_D[-3]
            #jsonDic['验证_MACD_W'] =  '%.3f' % macd_W[-1] + '_' +  '%.3f' % macd_W[-2] + '_' +  '%.3f' % macd_W[-3]
            #jsonDic['验证_布林_30'] =  '%.3f' % middleband_30[-1] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-3]
            #jsonDic['验证_布林_60'] =  '%.3f' % middleband_60[-1] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-3]
            #jsonDic['验证_布林_D'] =  '%.3f' % middleband_D[-1] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-3]
            #jsonDic['验证_布林_W'] =  '%.3f' % middleband_W[-1] + '_' +  '%.3f' % middleband_W[-2] + '_' +  '%.3f' % middleband_W[-3]
            #jsonDic['验证_20MA_D'] =  '%.3f' % real[-1]

            #jsonParam = dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items()
            #                 + jsonResult_W.items() + jsonResult_b_30.items() + jsonResult_b_60.items()
            #                 + jsonResult_b_D.items() + jsonResult_b_W.items() + jsonDic.items())
            jsonParam = dict(jsonResult_60.items() + jsonResult_D.items()
                             + jsonResult_b_60.items()
                             + jsonResult_b_D.items() + jsonDic.items())
            insertRecord(jsonParam)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            print e
            logging.error("error:" + codeItem)

    for codeItem in zhishu_code_index:
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem + ',Count:' + str(count)
        try:

            macd_30,macdsignal_30,macdhist_30,jsonResult_30,result_30,mairuresult_30,maichuresult_30  = MACD(codeItem,  '30')
            macd_60,macdsignal_60,macdhist_60,jsonResult_60,result_60,mairuresult_60,maichuresult_60  = MACD(codeItem,  '60')
            macd_D,macdsignal_D,macdhist_D,jsonResult_D,result_D,mairuresult_D,maichuresult_D  = MACD(codeItem,  'D')
            macd_W,macdsignal_W,macdhist_W,jsonResult_W,result_W,mairuresult_W,maichuresult_W  = MACD(codeItem,  'W')
            upperband_30, middleband_30, lowerband_30, jsonResult_b_30, result_bl_30,mairuresult_bl_30,maichuresult_bl_30 = BBANDS(codeItem, '30')
            upperband_60, middleband_60, lowerband_60, jsonResult_b_60, result_bl_60,mairuresult_bl_60,maichuresult_bl_60 = BBANDS(codeItem, '60')
            upperband_D, middleband_D, lowerband_D, jsonResult_b_D, result_bl_D,mairuresult_bl_D,maichuresult_bl_D = BBANDS(codeItem, 'D')
            upperband_W, middleband_W, lowerband_W, jsonResult_b_W, result_bl_W,mairuresult_bl_W,maichuresult_bl_W = BBANDS(codeItem, 'W')
            real_D,tableresult_ma_d_20 = MA(codeItem, 'D', 20)
            real_60,tableresult_ma_60_20 = MA(codeItem, '60', 20)
            #real_D_10,tableresult_ma__20 = MA(codeItem, 'D', 10)

            jsonDic = {}
            jsonDic['00_20天线信息'] =  tableresult_ma_d_20
            #jsonDic['00_10天线信息'] =  tableresult_ma_d_20
            jsonDic['00_60分钟信息'] =  tableresult_ma_60_20
            jsonDic['01_日买入信息'] =  mairuresult_D + ' ' + mairuresult_bl_D
            jsonDic['01_时买入信息'] =  mairuresult_60 + ' ' + mairuresult_bl_60
            jsonDic['02_卖出信息'] = maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            jsonDic['03_上升通道'] = result_D + ' ' + result_bl_D
            jsonDic['04_Code'] = codeItem
            jsonDic['05_Name'] = common.gupiaomingcheng(codeItem)
            jsonDic['06_涨跌幅'] = common.zhangdiefu(codeItem)

            jsonDic['90_Time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            #jsonDic['验证_MACD_30'] =  '%.3f' % macd_30[-1] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-3]
            #jsonDic['验证_MACD_60'] =  '%.3f' % macd_60[-1] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-3]
            #jsonDic['验证_MACD_D'] =  '%.3f' % macd_D[-1] + '_' +  '%.3f' % macd_D[-2] + '_' +  '%.3f' % macd_D[-3]
            #jsonDic['验证_MACD_W'] =  '%.3f' % macd_W[-1] + '_' +  '%.3f' % macd_W[-2] + '_' +  '%.3f' % macd_W[-3]
            #jsonDic['验证_布林_30'] =  '%.3f' % middleband_30[-1] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-3]
            #jsonDic['验证_布林_60'] =  '%.3f' % middleband_60[-1] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-3]
            #jsonDic['验证_布林_D'] =  '%.3f' % middleband_D[-1] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-3]
            #jsonDic['验证_布林_W'] =  '%.3f' % middleband_W[-1] + '_' +  '%.3f' % middleband_W[-2] + '_' +  '%.3f' % middleband_W[-3]
            #jsonDic['验证_20MA_D'] =  '%.3f' % real[-1]

            jsonParam = dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items()
                             + jsonResult_W.items() + jsonResult_b_30.items() + jsonResult_b_60.items()
                             + jsonResult_b_D.items() + jsonResult_b_W.items() + jsonDic.items())
            insertRecord(jsonParam)
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
    remove("report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
    execute()
    rexExp1 = re.compile('^20*')
    rexExp2 = re.compile('^.*买入.*')
    rexExp3 = re.compile('^[\s]*$')
    toDataFrame({},{'$or':[{'00_20天线信息' : rexExp1, '01_日买入信息': rexExp2, '02_卖出信息':rexExp3}, {'04_Code':{'$in':[u'000001',u'399001',u'399006']},'07_所属行业': {'$exists':False}},{'04_是否持有' : 'yes'}]},'All_Code_JSON_Mongo','All_Part_Code_JSON_Mongo')
    #toDataFrame({},{'00_20天线信息' : rexExp1, '01_日买入信息': rexExp2},'All_Code_JSON_Mongo','All_Part_Code_JSON_Mongo')
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====All_code_json_mongo End====='