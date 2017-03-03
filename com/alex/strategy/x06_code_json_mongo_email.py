#encoding=utf-8

import sys
sys.path.append('/root/worksapce/Superman')
import logging
from pandas import DataFrame
import time as time
from com.alex.utils.mongo_util import *
from com.alex.utils.mysql_util import *
from com.alex.function.macd import *
from com.alex.function.bbands import *
import common

'''
##################################
常量 苹果供应链
##################################
'''
collectionName = "report_apple_" + time.strftime('%Y-%m-%d', time.localtime(time.time()))

'''
#################################
执行函数 execute
3D前置摄像头：
水晶光电 002273
光讯科技 002281


apple AR
苏大维格 300331
高新兴 300098

安洁科技 002635

无线充电：
硕贝德 300322
顺络电子 002138
东山精密 无线充电 002384

电池：
德赛电池 000049
欣旺达 电池 300207

玻璃机壳：
蓝思科技 2.5D玻璃 300433
劲胜精密 玻璃雕刻机 间接受惠 300083
#################################
'''
def execute():
    query_result = ['002273','002281','300331','300098','002635','300322','002138','002384','000049','300207','300433','300083']
    for codeItem in query_result:
        xinhao = ''
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

            jsonDic = {}
            jsonDic['90_Time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            jsonDic['02Code'] = '_' + codeItem
            jsonDic['03Name'] = common.gupiaomingcheng(codeItem)
            jsonDic['04涨跌幅'] = common.zhangdiefu(codeItem)
            jsonDic['051日买入信息'] = mairuresult_D + ' ' + mairuresult_bl_D
            #print  mairuresult_D + ' ' + mairuresult_bl_D
            jsonDic['052时买入信息'] =  mairuresult_60 + ' ' + mairuresult_bl_60

            #if (mairuresult_D !='' and (mairuresult_60  != '' or mairuresult_bl_60 != '')):
            if (mairuresult_60  != '' or mairuresult_bl_60 != ''):
                i = 0
                for i in [0] :
                    xinhao = xinhao + codeItem + '买入信号出现：<br>' +  mairuresult_D + '<br> ' + mairuresult_60 + '<br>' + mairuresult_bl_60 + ' '
                    email_util.sendMail(codeItem + '买入信号出现：<br>' + mairuresult_D + '<br>' + mairuresult_60 + '<br>' + mairuresult_bl_60, codeItem + '买入，谨慎谨慎再谨慎')
                    i = i + 1
                    time.sleep(1)

            jsonDic['06卖出信息'] = maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            #print  maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            if (maichuresult_60 != '' or  maichuresult_bl_60 != ''):
                j = 0
                for j in [0] :
                    xinhao = xinhao + codeItem + '卖出信号出现：<br>' +  maichuresult_D + '<br>' + maichuresult_60 + '<br>' + maichuresult_bl_60 + ' '
                    email_util.sendMail(codeItem + '卖出信号出现：<br>' +  maichuresult_D + '<br>' +maichuresult_60 + '<br>' + maichuresult_bl_60, codeItem + '卖出，果断果断再果断')
                    j = j + 1
                    time.sleep(1)

            jsonDic['07上升通道'] = result_D + ' ' + result_bl_D
            jsonDic['验证_MACD_30'] =  '%.3f' % macd_30[-1] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-3]
            jsonDic['验证_MACD_60'] =  '%.3f' % macd_60[-1] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-3]
            jsonDic['验证_MACD_D'] =  '%.3f' % macd_D[-1] + '_' +  '%.3f' % macd_D[-2] + '_' +  '%.3f' % macd_D[-3]
            jsonDic['验证_MACD_W'] =  '%.3f' % macd_W[-1] + '_' +  '%.3f' % macd_W[-2] + '_' +  '%.3f' % macd_W[-3]
            jsonDic['验证_布林_30'] =  '%.3f' % middleband_30[-1] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-3]
            jsonDic['验证_布林_60'] =  '%.3f' % middleband_60[-1] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-3]
            jsonDic['验证_布林_D'] =  '%.3f' % middleband_D[-1] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-3]
            jsonDic['验证_布林_W'] =  '%.3f' % middleband_W[-1] + '_' +  '%.3f' % middleband_W[-2] + '_' +  '%.3f' % middleband_W[-3]


            jsonParam = dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items()
                             + jsonResult_W.items() + jsonResult_b_30.items() + jsonResult_b_60.items()
                             + jsonResult_b_D.items() + jsonResult_b_W.items() + jsonDic.items())

            insertRecord_param(jsonParam, collectionName)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            logging.error("error:" + codeItem)
            print e

        xiaomowang = '<br>卖出信号：<br>' +  maichuresult_D + '<br>' + maichuresult_60 + '<br>' + maichuresult_bl_60 + '<br>' + maichuresult_bl_D
        xiaomowang = xiaomowang + '<br> 买入信号：<br>' +  mairuresult_D + '<br> ' + mairuresult_60 + '<br>' + mairuresult_bl_60 + '<br>' + mairuresult_bl_D

        caozuo = ''
        if xinhao.__contains__('买入'):
            caozuo = ',【操作】买入'
        elif xinhao.__contains__('卖出'):
            caozuo = ',【操作】卖出'

        caozuo2 = ''
        if xinhao.__contains__('V型翻转'):
            caozuo = ',【操作】买入点'
            toDataFrame_param_content({}, '★★★★★My_Code_JSON_Mongo_' + time.strftime('%Y-%m-%d_%H:%M', time.localtime(time.time())) + '#【长期关注】'+ common.gupiaomingcheng(codeItem) + caozuo + caozuo2 +',【主题】手机供应链#',xinhao + xiaomowang, collectionName)
        elif xinhao.__contains__('下降1') or xinhao.__contains__('上穿'):
            caozuo = ',【操作】卖出点'
            #toDataFrame_param_content({}, '★★★★★My_Code_JSON_Mongo_' + time.strftime('%Y-%m-%d_%H:%M', time.localtime(time.time())) + '#【长期关注】'+ common.gupiaomingcheng(codeItem) + caozuo + caozuo2 +'#',xinhao, collectionName)

    return xinhao

def execute_param():
    query_result = ['002273','002281','300331','300098','002635','300322','002138','002384','000049','300207','300433','300083']
    xinhao = ''
    for codeItem in query_result:
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

            jsonDic = {}
            jsonDic['90_Time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            jsonDic['02Code'] = '_' + codeItem
            jsonDic['03Name'] = common.gupiaomingcheng(codeItem)
            jsonDic['04涨跌幅'] = common.zhangdiefu(codeItem)
            jsonDic['051日买入信息'] = mairuresult_D + ' ' + mairuresult_bl_D
            #print  mairuresult_D + ' ' + mairuresult_bl_D
            jsonDic['052时买入信息'] =  mairuresult_60 + ' ' + mairuresult_bl_60

            print '买入mairuresult_bl_60!='':'
            print  mairuresult_bl_60 != ''
            if ( mairuresult_bl_60 != ''):
                i = 0
                for i in [0] :
                    xinhao = xinhao + codeItem + '买入信号出现：<br>' +  mairuresult_D + '<br> ' + mairuresult_60 + '<br>' + mairuresult_bl_60 + ' '
                    email_util.sendMail(codeItem + '买入信号出现：<br>' + mairuresult_D + '<br>' + mairuresult_60 + '<br>' + mairuresult_bl_60, codeItem + '买入，谨慎谨慎再谨慎')
                    i = i + 1
                    time.sleep(3)

            jsonDic['06卖出信息'] = maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            #print  maichuresult_60 + ' ' + maichuresult_D + ' ' + maichuresult_bl_60 + ' ' + maichuresult_bl_D
            print '卖出mairuresult_bl_60!='':'
            print maichuresult_bl_60 != ''
            if ( maichuresult_bl_60 != ''):
                j = 0
                for j in [0] :
                    xinhao = xinhao + codeItem + '卖出信号出现：<br>' +  maichuresult_D + '<br>' + maichuresult_60 + '<br>' + maichuresult_bl_60 + ' '
                    email_util.sendMail(codeItem + '卖出信号出现：<br>' +  maichuresult_D + '<br>' +maichuresult_60 + '<br>' + maichuresult_bl_60, codeItem + '卖出，果断果断再果断')
                    j = j + 1
                    time.sleep(3)

            jsonDic['07上升通道'] = result_D + ' ' + result_bl_D
            jsonDic['验证_MACD_30'] =  '%.3f' % macd_30[-1] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-3]
            jsonDic['验证_MACD_60'] =  '%.3f' % macd_60[-1] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-3]
            jsonDic['验证_MACD_D'] =  '%.3f' % macd_D[-1] + '_' +  '%.3f' % macd_D[-2] + '_' +  '%.3f' % macd_D[-3]
            jsonDic['验证_MACD_W'] =  '%.3f' % macd_W[-1] + '_' +  '%.3f' % macd_W[-2] + '_' +  '%.3f' % macd_W[-3]
            jsonDic['验证_布林_30'] =  '%.3f' % middleband_30[-1] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-3]
            jsonDic['验证_布林_60'] =  '%.3f' % middleband_60[-1] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-3]
            jsonDic['验证_布林_D'] =  '%.3f' % middleband_D[-1] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-3]
            jsonDic['验证_布林_W'] =  '%.3f' % middleband_W[-1] + '_' +  '%.3f' % middleband_W[-2] + '_' +  '%.3f' % middleband_W[-3]


            jsonParam = dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items()
                             + jsonResult_W.items() + jsonResult_b_30.items() + jsonResult_b_60.items()
                             + jsonResult_b_D.items() + jsonResult_b_W.items() + jsonDic.items())

            #insertRecord_param(jsonParam, collectionName)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            logging.error("error:" + codeItem)
            print e

    return xinhao



'''
########################
主运行函数main
########################
'''

count = len(sys.argv)
if (count == 2):
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email Start====='
    #param = sys.argv[1]
    #print param
    execute_param()
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email Start====='
    remove(collectionName)
    execute()
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='