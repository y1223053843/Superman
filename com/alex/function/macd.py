#encoding=utf-8

import tushare as ts
import numpy as num
import talib as ta
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
###############################################################################
执行函数:执行MACD操作
说明：
参数1 codeCon 数据编码
参数2 type 类型
###############################################################################
'''
def MACD(codeCon, type, **values):
    data_history = ''
    if (values.get('end') == None):
        if (codeCon == '000001'):
            data_history = ts.get_k_data(codeCon, ktype = type,index='true')
        else:
            data_history = ts.get_k_data(codeCon, ktype = type)
    else:
        if (codeCon == '000001'):
            data_history = ts.get_k_data(codeCon, ktype = type,index='true', end=values.get('end'))
        else:
            data_history = ts.get_k_data(codeCon, ktype = type, end=values.get('end'))

    closeArray = num.array(data_history['close'])

    # macd 为快线 macdsignal为慢线，macdhist为柱体
    macd,macdsignal,macdhist = ta.MACD(num.asarray(closeArray,dtype='double'), fastperiod=12, slowperiod=26, signalperiod=9)

    tableresult = ''
    mairuresult = ''
    maichuresult = ''
    jsonResult = {}
    if (macdhist[-1] > macdhist[-2] and macdhist[-3] > macdhist[-2]):
        jsonResult['MACD_Z_' + type] = '[V]'
    #if (macdhist[-1] < macdhist[-2] and macdhist[-3] < macdhist[-2]):
    #    jsonResult['MACD_Z_' + type] = '[/\]'
    #    maichuresult += type + '_MACD顶部八字翻转，卖出'
    if (macdhist[-1] > macdhist[-2] and macdhist[-2] > macdhist[-3]):
        jsonResult['MACD_Z_' + type] = '[/]'


    if (type == 'D' or type == '60'):
        if (macdhist[-1] < macdhist[-2] ):
            jsonResult['10_MACD柱体_' + type] = '下降1 ' + type
            maichuresult = type + '_MACD柱体下降1_'+ type + '，卖出'
            if (macdhist[-2] < macdhist[-3] ):
                jsonResult['10_MACD柱体_' + type] = '下降2 ' + type
                maichuresult = type + '_MACD柱体下降2_'+ type + '，卖出'
                if (macdhist[-3] < macdhist[-4] ):
                    jsonResult['10_MACD柱体_' + type] = '下降3 ' + type
                    maichuresult = type + '_MACD柱体下降3_'+ type + '，卖出'
                    if (macdhist[-4] < macdhist[-5] ):
                        jsonResult['10_MACD柱体_' + type] = '下降4 ' + type
                        maichuresult = type + '_MACD柱体下降4_'+ type + '，卖出'

    #if (macdsignal[-1] > macdsignal[-2]):
    #    jsonResult['MACD_M_' + type] = '[/]'
    #if (macdsignal[-1] < macdsignal[-2]):
    #    jsonResult['MACD_M_' + type] = '[\]'
    if (codeCon == '000001' or codeCon == '600547'):
        jsonResult['MACD慢线小于0_' + type] = 'Y'
        if (macdhist[-1] > macdhist[-2] and macdhist[-3] > macdhist[-2]):
            jsonResult['MACD底部V型翻转_' + type] = 'Y'
            mairuresult += type + '_MACD在底部V型翻转，买入'

        #if (macdhist[-1] > macdhist[-2] and (codeCon == '000001' or codeCon == '399006' or codeCon =='399001' or codeCon =='600547')):
        if (macdhist[-1] > macdhist[-2]):
            tmp = ''
            if (macdhist[-2] > macdhist[-3]):
                tmp = type + '_MACD柱体上升2_'+ type + '，买入'
                if (macdhist[-3] > macdhist[-4]):
                    tmp = type + '_MACD柱体上升3_'+ type + '，买入'
                    if (macdhist[-4] > macdhist[-5]):
                        tmp = type + '_MACD柱体上升4_'+ type + '，买入'

            mairuresult += tmp
    else:
        if (macdsignal[-1] < 0):
            jsonResult['MACD慢线小于0_' + type] = 'Y'
            if (macdhist[-1] > macdhist[-2] and macdhist[-3] > macdhist[-2]):
                jsonResult['MACD底部V型翻转_' + type] = 'Y'
                mairuresult += type + '_MACD在底部V型翻转，买入'

            if (macdhist[-1] > macdhist[-2] and (codeCon == '000001' or codeCon == '399006' or codeCon =='399001')):
                tmp = ''
                if (macdhist[-2] > macdhist[-3]):
                    tmp = type + '_MACD柱体上升2_'+ type + '，买入'
                    if (macdhist[-3] > macdhist[-4]):
                        tmp = type + '_MACD柱体上升3_'+ type + '，买入'
                        if (macdhist[-4] > macdhist[-5]):
                            tmp = type + '_MACD柱体上升4_'+ type + '，买入'

                mairuresult += tmp

    tianshu = ''
    if (type == 'X'):
        if (macdsignal[-1] > macdsignal[-2]):
            tianshu = 'D_MACD上升通道1天'

            if (macdsignal[-2] > macdsignal[-3]):
                tianshu = 'D_MACD上升通道2天'

                if (macdsignal[-3] > macdsignal[-4]):
                    tianshu = 'D_MACD上升通道3天'

        tableresult = tianshu

    if (type == 'D' or type == '60'):
        if (macd[-1] > macd[-2]):
            jsonResult['10_MACD快线_' + type] = '上升1 ' + type
            if (macd[-2] > macd[-3]):
                jsonResult['10_MACD快线_' + type] = '上升2 ' + type
                if (macd[-3] > macd[-4]):
                    jsonResult['10_MACD快线_' + type] = '上升3 ' + type
                    if (macd[-4] > macd[-5]):
                        jsonResult['10_MACD快线_' + type] = '上升4 ' + type

        if (macd[-1] < macd[-2]):
            jsonResult['10_MACD快线_' + type] = '下降1 ' + type
            if (macd[-2] < macd[-3]):
                jsonResult['10_MACD快线_' + type] = '下降2 ' + type
                if (macd[-3] < macd[-4]):
                    jsonResult['10_MACD快线_' + type] = '下降3 ' + type
                    if (macd[-4] < macd[-5]):
                        jsonResult['10_MACD快线_' + type] = '下降4 ' + type
    #else:
        #if (macd[-1] > macd[-2]):
        #    jsonResult['MACD_K_' + type] = '[/]'
        #if (macd[-1] < macd[-2]):
        #    jsonResult['MACD_K_' + type] = '[\]'

    return macd,macdsignal,macdhist,jsonResult,tableresult,mairuresult,maichuresult

#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D')
#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D', end = '2016-12-15')
#print macd
#print jsonResult
#print result