# encoding=utf-8

import sys

sys.path.append('/root/worksapce/Superman')
import logging
from pandas import DataFrame
import time as time
from com.alex.utils.mongo_util import *
from com.alex.function.macd import *
from com.alex.function.bbands import *
import common
from com.alex.function.union_func import *

'''
##################################
常量
##################################
'''
collectionName = "report_strategy001_" + time.strftime('%Y-%m-%d', time.localtime(time.time()))

'''
#################################
策略1执行函数 strategy002
#################################
'''
def strategy002(query_result, zhuti, collectionName):
    for codeItem in query_result:
        xinhao = ''
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem
        try:
            # MACD
            macd_30, macdsignal_30, macdhist_30, jsonResult_30, result_30, mairuresult_30, maichuresult_30 = MACD(codeItem, '30')
            macd_60, macdsignal_60, macdhist_60, jsonResult_60, result_60, mairuresult_60, maichuresult_60 = MACD(codeItem, '60')
            macd_D, macdsignal_D, macdhist_D, jsonResult_D, result_D, mairuresult_D, maichuresult_D = MACD(codeItem,'D')
            macd_W, macdsignal_W, macdhist_W, jsonResult_W, result_W, mairuresult_W, maichuresult_W = MACD(codeItem,'W')
            macd_M, macdsignal_M, macdhist_M, jsonResult_M, result_M, mairuresult_M, maichuresult_M = MACD(codeItem,'M')

            # 布林线
            upperband_30, middleband_30, lowerband_30, jsonResult_b_30, result_bl_30,mairuresult_bl_30,maichuresult_bl_30 = BBANDS(codeItem, '30')
            upperband_60, middleband_60, lowerband_60, jsonResult_b_60, result_bl_60,mairuresult_bl_60,maichuresult_bl_60 = BBANDS(codeItem, '60')
            upperband_D, middleband_D, lowerband_D, jsonResult_b_D, result_bl_D,mairuresult_bl_D,maichuresult_bl_D = BBANDS(codeItem, 'D')
            upperband_W, middleband_W, lowerband_W, jsonResult_b_W, result_bl_W,mairuresult_bl_W,maichuresult_bl_W = BBANDS(codeItem, 'W')
            upperband_M, middleband_M, lowerband_M, jsonResult_b_M, result_bl_M, mairuresult_bl_M, maichuresult_bl_M = BBANDS(
                codeItem, 'M')

            jsonDic = {}
            # jsonDic['90_Time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            jsonDic['aaaInfo_1股票编码'] = '_' + codeItem
            jsonDic['aaaInfo_2股票名称'] = common.gupiaomingcheng(codeItem)
            jsonDic['aaaInfo_股票涨跌幅'] = common.zhangdiefu(codeItem)

            # MACD
            jsonDic['basicInfo_30分钟MACD快线信息'] =  '%.3f' % macd_30[-3] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-1]
            jsonDic['basicInfo_30分钟MACD慢线信息'] = '%.3f' % macdsignal_30[-3] + '_' + '%.3f' % macdsignal_30[-2] + '_' + '%.3f' % macdsignal_30[-1]
            jsonDic['basicInfo_30分钟MACD柱体信息'] = '%.3f' % macdhist_30[-3] + '_' + '%.3f' % macdhist_30[-2] + '_' + '%.3f' % macdhist_30[-1]
            jsonDic['basicInfo_60分钟MACD快线信息'] =  '%.3f' % macd_60[-3] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-1]
            jsonDic['basicInfo_60分钟MACD慢线信息'] = '%.3f' % macdsignal_60[-3] + '_' + '%.3f' % macdsignal_60[-2] + '_' + '%.3f' % macdsignal_60[-1]
            jsonDic['basicInfo_60分钟MACD柱体信息'] = '%.3f' % macdhist_60[-3] + '_' + '%.3f' % macdhist_60[-2] + '_' + '%.3f' % macdhist_60[-1]
            jsonDic['basicInfo_日MACD快线信息'] = '%.3f' % macd_D[-3] + '_' + '%.3f' % macd_D[-2] + '_' + '%.3f' % macd_D[-1]
            jsonDic['basicInfo_日MACD慢线信息'] = '%.3f' % macdsignal_D[-3] + '_' + '%.3f' % macdsignal_D[-2] + '_' + '%.3f' % macdsignal_D[-1]
            jsonDic['basicInfo_日MACD柱体信息'] = '%.3f' % macdhist_D[-3] + '_' + '%.3f' % macdhist_D[-2] + '_' + '%.3f' % macdhist_D[-1]
            jsonDic['basicInfo_周MACD快线信息'] = '%.3f' % macd_W[-6] + '_' + '%.3f' % macd_W[-5] + '_' + '%.3f' % macd_W[-4] + '_' + '%.3f' % macd_W[-3] + '_' + '%.3f' % macd_W[-2] + '_' + '%.3f' % macd_W[-1]
            jsonDic['basicInfo_周MACD慢线信息'] = '%.3f' % macdsignal_W[-3] + '_' + '%.3f' % macdsignal_W[-2] + '_' + '%.3f' % macdsignal_W[-1]
            jsonDic['basicInfo_周MACD柱体信息'] = '%.3f' % macdhist_W[-3] + '_' + '%.3f' % macdhist_W[-2] + '_' + '%.3f' % macdhist_W[-1]
            jsonDic['basicInfo_月MACD快线信息'] = '%.3f' % macd_M[-3] + '_' + '%.3f' % macd_M[-2] + '_' + '%.3f' % macd_M[-1]
            jsonDic['basicInfo_月MACD慢线信息'] = '%.3f' % macdsignal_M[-3] + '_' + '%.3f' % macdsignal_M[-2] + '_' + '%.3f' % macdsignal_M[-1]
            jsonDic['basicInfo_月MACD柱体信息'] = '%.3f' % macdhist_M[-3] + '_' + '%.3f' % macdhist_M[-2] + '_' + '%.3f' % macdhist_M[-1]

            # BULL
            jsonDic['basicInfo_30分钟布林中线信息'] =  '%.3f' % middleband_30[-3] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-1]
            jsonDic['basicInfo_30分钟布林上线信息'] = '%.3f' % upperband_30[-3] + '_' + '%.3f' % upperband_30[-2] + '_' + '%.3f' % upperband_30[-1]
            jsonDic['basicInfo_30分钟布林下线信息'] = '%.3f' % lowerband_30[-3] + '_' + '%.3f' % middleband_30[-2] + '_' + '%.3f' % middleband_30[-1]
            jsonDic['basicInfo_60分钟布林中线信息'] =  '%.3f' % middleband_60[-3] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-1]
            jsonDic['basicInfo_60分钟布林上线信息'] = '%.3f' % upperband_60[-3] + '_' + '%.3f' % upperband_60[-2] + '_' + '%.3f' % upperband_60[-1]
            jsonDic['basicInfo_60分钟布林下线信息'] = '%.3f' % lowerband_60[-3] + '_' + '%.3f' % lowerband_60[-2] + '_' + '%.3f' % lowerband_60[-1]
            jsonDic['basicInfo_日布林中线信息'] =  '%.3f' % middleband_D[-3] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-1]
            jsonDic['basicInfo_日布林上线信息'] = '%.3f' % upperband_D[-3] + '_' + '%.3f' % upperband_D[ -2] + '_' + '%.3f' % upperband_D[-1]
            jsonDic['basicInfo_日布林下线信息'] = '%.3f' % lowerband_D[-3] + '_' + '%.3f' % lowerband_D[-2] + '_' + '%.3f' % lowerband_D[-1]
            jsonDic['basicInfo_周布林中线信息'] = '%.3f' % middleband_W[-3] + '_' + '%.3f' % middleband_W[-2] + '_' + '%.3f' % middleband_W[-1]
            jsonDic['basicInfo_周布林上线信息'] = '%.3f' % upperband_W[-3] + '_' + '%.3f' % upperband_W[-2] + '_' + '%.3f' % upperband_W[-1]
            jsonDic['basicInfo_周布林下线信息'] = '%.3f' % lowerband_W[-3] + '_' + '%.3f' % lowerband_W[2] + '_' + '%.3f' % lowerband_W[-1]
            jsonDic['basicInfo_月布林中线信息'] = '%.3f' % middleband_M[-3] + '_' + '%.3f' % middleband_M[-2] + '_' + '%.3f' %  middleband_M[-1]
            jsonDic['basicInfo_月布林上线信息'] = '%.3f' % upperband_M[-3] + '_' + '%.3f' % upperband_M[-2] + '_' + '%.3f' % upperband_M[-1]
            jsonDic['basicInfo_月布林下线信息'] = '%.3f' % lowerband_M[-3] + '_' + '%.3f' % lowerband_M[-2] + '_' + '%.3f' % lowerband_M[-1]

            # 策略1
            # MACD月线大于0，MACD月线处于上升阶段，布林周线下穿
            stra001 = ''
            if (macdsignal_M[-1] > 0):
                stra001 = stra001 + '1'
            if (macdhist_M[-1] > macdhist_M[-2]):
                stra001 = stra001 + '2'
            if ( (common.zuidijiage(codeItem, 'W') - lowerband_W[-1]) < 0):
                stra001 = stra001 + '3'
            jsonDic['aaaInfo_stra001_MACD月线大于0，MACD月线柱体处于上升阶段，布林周线下穿'] = stra001

            # 策略2
            # MACD月线大于0，MACD月线柱体转折，布林周线下穿
            stra002 = ''
            if (macdsignal_M[-1] > 0):
                stra002 = stra002 + '1'
            if (macdhist_M[-1] > macdhist_M[-2] and  macdhist_M[-3] > macdhist_M[-2]):
                stra002 = stra002 + '2'
            if ((common.zuidijiage(codeItem, 'W') - lowerband_W[-1]) < 0):
                stra002 = stra002 + '3'
            jsonDic['aaaInfo_stra002_MACD月线大于0，MACD月线柱体转折，布林周线下穿'] = stra002

            # 策略3
            # MACD月线大于0，MACD月线柱体转折，布林周线下穿
            stra003 = ''
            if (macdsignal_M[-1] > 0):
                stra003 = stra003 + '1'
            if (macdhist_M[-1] > macdhist_M[-2]):
                stra003 = stra003 + '2'
            if (macdhist_W[-1] < macdhist_W[-4] or  macdhist_W[-1] < macdhist_W[-5]):
                stra003 = stra003 + '3'
            jsonDic['aaaInfo_stra003_MACD月线大于0，MACD月线柱体处于上升阶段，MACD_周线_持续下跌，等待时机'] = stra003

            # 策略4
            if ( (common.zuidijiage(codeItem, 'W') - lowerband_W[-1]) < 0):
                jsonDic['aaaInfo_stra004_布林_周线_收在下方'] = 1

            # 策略5
            if ((common.zuidijiage(codeItem, 'D') - lowerband_D[-1]) < 0):
                jsonDic['aaaInfo_stra005_布林_日线_收在下方'] = 1
                if ((middleband_D[-1]-lowerband_D[-1])/lowerband_D[-1] > 0.05):
                    jsonDic['aaaInfo_stra005_布林_日线_收在下方,上升空间大于5%'] = 1
                    if((common.zuidijiage(codeItem, 'D')-lowerband_W[-1])/common.zuidijiage(codeItem, 'D') < 0.1):
                        jsonDic['aaaInfo_stra005_布林_日线_收在下方,距离布林周线小于10%'] = 1

        except (IOError, TypeError, NameError, IndexError, Exception) as e:
            logging.error("error:" + codeItem)
            print e

        # 插入数据库
        jsonParam = dict(jsonDic.items())
        insertRecord_param(jsonParam, collectionName)


'''
########################
主运行函数main
########################

count = len(sys.argv)
if (count == 2):
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email Start====='
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email Start====='
    remove(collectionName)
    query_result = ['600679']
    strategy001(query_result,'【主题】')
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='
'''
