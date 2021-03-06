#encoding=utf-8

import sys
sys.path.append('/root/worksapce/Superman')
import logging
from pandas import DataFrame
import time as time
import lxml.html
import lxml.etree
import curl
from com.alex.utils.mongo_util import *
from com.alex.function.macd import *
from com.alex.function.ma import *
from com.alex.function.bbands import *
import common
from com.alex.strategy.strategy001 import *
import math

'''
##################################
常量
##################################
'''
collectionName = "report_tiantain_" + time.strftime('%Y-%m-%d', time.localtime(time.time()))
collectionName2 = "report_tiantain_all_" + time.strftime('%Y-%m-%d', time.localtime(time.time()))

'''
#################################
执行函数 execute
说明：
#################################
'''
def execute2(all_code_index, all_title, all_time):

    all_code = DataFrame({'codeitem':all_code_index,'hangye':all_title,'time':all_time},index=all_code_index)
    all_code_drop = all_code.drop_duplicates('codeitem')

    all_code_time = DataFrame(all_time,index=all_code_index,columns=['time'])

    for codeItem in all_code_drop['codeitem']:
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem
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

            jsonDic = {}
            jsonDic['00_20天线信息'] =  tableresult_ma_d_20
            jsonDic['00_60分钟信息'] =  tableresult_ma_60_20
            jsonDic['01_日买入信息'] = mairuresult_D + ' ' + mairuresult_bl_D
            jsonDic['01_时买入信息'] =  mairuresult_60 + ' ' + mairuresult_bl_60
            jsonDic['02_卖出信息'] = maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            jsonDic['03_上升通道'] = result_D + ' ' + result_bl_D
            jsonDic['90_Time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            jsonDic['90_原始Time'] = all_code_drop.loc[codeItem,'time']
            jsonDic['04_Code'] = codeItem
            #jsonDic['02Code2'] = '_' + codeItem
            jsonDic['05_Name'] = common.gupiaomingcheng(codeItem)
            jsonDic['06_所属行业'] = all_code_drop.loc[codeItem,'hangye']
            jsonDic['07_涨跌幅'] = common.zhangdiefu(codeItem)

            #jsonDic['验证_MACD_30'] =  '%.3f' % macd_30[-1] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-3]
            #jsonDic['验证_MACD_60'] =  '%.3f' % macd_60[-1] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-3]
            #jsonDic['验证_MACD_D'] =  '%.3f' % macd_D[-1] + '_' +  '%.3f' % macd_D[-2] + '_' +  '%.3f' % macd_D[-3]
            #jsonDic['验证_MACD_W'] =  '%.3f' % macd_W[-1] + '_' +  '%.3f' % macd_W[-2] + '_' +  '%.3f' % macd_W[-3]
            #jsonDic['验证_布林_30'] =  '%.3f' % middleband_30[-1] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-3]
            #jsonDic['验证_布林_60'] =  '%.3f' % middleband_60[-1] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-3]
            #jsonDic['验证_布林_D'] =  '%.3f' % middleband_D[-1] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-3]
            #jsonDic['验证_布林_W'] =  '%.3f' % middleband_W[-1] + '_' +  '%.3f' % middleband_W[-2] + '_' +  '%.3f' % middleband_W[-3]

            jsonParam = dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items()
                             + jsonResult_W.items() + jsonResult_b_30.items() + jsonResult_b_60.items()
                             + jsonResult_b_D.items() + jsonResult_b_W.items() + jsonDic.items())

            insertRecord_param(jsonParam, collectionName2)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            logging.error("error:" + codeItem)
            print e

    zhishu_code_index = num.array(['399006','399001','000001'])
    for codeItem in zhishu_code_index:
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem
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

            jsonDic = {}
            jsonDic['00_20天线信息'] =  tableresult_ma_d_20
            jsonDic['00_60分钟信息'] =  tableresult_ma_60_20
            jsonDic['01_日买入信息'] = mairuresult_D + ' ' + mairuresult_bl_D
            jsonDic['01_时买入信息'] =  mairuresult_60 + ' ' + mairuresult_bl_60
            jsonDic['02_卖出信息'] = maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            jsonDic['03_上升通道'] = result_D + ' ' + result_bl_D
            jsonDic['90_Time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            jsonDic['04_Code'] = codeItem
            #jsonDic['02Code2'] = '_' + codeItem
            jsonDic['05_Name'] = common.gupiaomingcheng(codeItem)
            jsonDic['07_涨跌幅'] = common.zhangdiefu(codeItem)

            #jsonDic['验证_MACD_30'] =  '%.3f' % macd_30[-1] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-3]
            #jsonDic['验证_MACD_60'] =  '%.3f' % macd_60[-1] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-3]
            #jsonDic['验证_MACD_D'] =  '%.3f' % macd_D[-1] + '_' +  '%.3f' % macd_D[-2] + '_' +  '%.3f' % macd_D[-3]
            #jsonDic['验证_MACD_W'] =  '%.3f' % macd_W[-1] + '_' +  '%.3f' % macd_W[-2] + '_' +  '%.3f' % macd_W[-3]
            #jsonDic['验证_布林_30'] =  '%.3f' % middleband_30[-1] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-3]
            #jsonDic['验证_布林_60'] =  '%.3f' % middleband_60[-1] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-3]
            #jsonDic['验证_布林_D'] =  '%.3f' % middleband_D[-1] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-3]
            #jsonDic['验证_布林_W'] =  '%.3f' % middleband_W[-1] + '_' +  '%.3f' % middleband_W[-2] + '_' +  '%.3f' % middleband_W[-3]

            jsonParam = dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items()
                             + jsonResult_W.items() + jsonResult_b_30.items() + jsonResult_b_60.items()
                             + jsonResult_b_D.items() + jsonResult_b_W.items() + jsonDic.items())

            insertRecord_param(jsonParam, collectionName2)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            logging.error("error:" + codeItem)
            print e







def execute(all_code_index, all_title, all_time):

    all_code = DataFrame({'codeitem':all_code_index,'hangye':all_title,'time':all_time},index=all_code_index)
    all_code_drop = all_code.drop_duplicates('codeitem')

    all_code_time = DataFrame(all_time,index=all_code_index,columns=['time'])

    for codeItem in all_code_drop['codeitem']:
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem
        try:
            strategy002({codeItem},all_code_drop.loc[codeItem,'hangye'],collectionName2)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            logging.error("error:" + codeItem)
            print e



'''
###############################################################################
主运行函数main
###############################################################################
'''

param = sys.argv[0]
if (param == 1):
    print 'param:' + param
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====tiantian_all_code_json_mongo_email Start====='
    df = toDataFrame_param_for_tiantian({}, 'Tiantian_All_Pool_Code_JSON_Mongo', collectionName)
    all_code = df['02Code'].values
    all_title = df['04Hangye'].values
    all_time = df['90_Time'].values

    remove(collectionName2)
    execute(all_code, all_title,all_time)
    toDataFrame_param({}, '★★★★★Tiantian_All_Code_Json_Mongo_Email' + time.strftime('%Y-%m-%d_%H:%M', time.localtime(time.time())) , collectionName2)

    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====tiantian_all_code_json_mongo_email End====='