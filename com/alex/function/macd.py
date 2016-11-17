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
def MACD(codeCon, type):
    data_history = ts.get_k_data(codeCon, ktype = type)
    closeArray = num.array(data_history['close'])

    # macd 为快线 macdsignal为慢线，macdhist为柱体
    macd,macdsignal,macdhist = ta.MACD(num.asarray(closeArray,dtype='double'), fastperiod=12, slowperiod=26, signalperiod=9)

    result = ''
    jsonResult = {}
    if (macdhist[-1] > macdhist[-2] and macdhist[-3] > macdhist[-2]):
        jsonResult['macd_Z_' + type] = '[V]'
    if (macdhist[-1] < macdhist[-2] and macdhist[-3] < macdhist[-2]):
        jsonResult['macd_Z_' + type] = '[/\]'
    if (macdhist[-1] > macdhist[-2] and macdhist[-2] > macdhist[-3]):
        jsonResult['macd_Z_' + type] = '[/]'
    if (macdhist[-1] < macdhist[-2] and macdhist[-2] < macdhist[-3]):
        jsonResult['macd_Z_' + type] = '[\]'
    if (macdhist[-1] > 0 and macdhist[-2] < 0):
        jsonResult['macd_Z_' + type] = '[X]'

    if (macdsignal[-1] > macdsignal[-2]):
        jsonResult['macd_M_' + type] = '[/]'
    if (macdsignal[-1] < macdsignal[-2]):
        jsonResult['macd_M_' + type] = '[\]'


    if (macd[-1] > macd[-2]):
        jsonResult['macd_K_' + type] = '[/]'
    if (macd[-1] < macd[-2]):
        jsonResult['macd_K_' + type] = '[\]'

    return macd,macdsignal,macdhist,jsonResult,result

#macd,macdsignal,macdhist,jsonResult,result = MACD('300201', '60')
#print jsonResult
#print result