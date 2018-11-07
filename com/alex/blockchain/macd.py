# encoding=utf-8

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
    data_history = ''
    data_history = ts.get_k_data(codeCon, ktype=type)

    closeArray = num.array(data_history['close'])

    # macd 为快线 macdsignal为慢线，macdhist为柱体
    macd, macdsignal, macdhist = ta.MACD(num.asarray(closeArray, dtype='double'), fastperiod=12, slowperiod=26,
                                         signalperiod=9)

    jsonResult = {}
    if (macdhist[-1] > macdhist[-2] and macdhist[-3] > macdhist[-2]):
        jsonResult['MACD_Z_' + type] = '[V]'

    return macd, macdsignal, macdhist, jsonResult

# macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D')
# macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D', end = '2016-12-15')
# print macd
# print jsonResult
# print result
