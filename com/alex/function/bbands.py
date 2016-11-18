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
def BBANDS(codeCon, type):
    data_history = ts.get_k_data(codeCon, ktype = type)
    closeArray = num.array(data_history['close'])

    doubleCloseArray = num.asarray(closeArray,dtype='double');
    upperband, middleband, lowerband = ta.BBANDS(doubleCloseArray, timeperiod=26, nbdevup=2, nbdevdn=2, matype=0)

    result = ''
    jsonResult = {}
    if (middleband[-1] > middleband[-2] and middleband[-3] > middleband[-2]):
        jsonResult['布林_M_' + type] = '[V]'

    if (middleband[-1] < middleband[-2] and middleband[-3] < middleband[-2]):
        jsonResult['布林_M_' + type] = '[/\]'

    if (middleband[-1] > middleband[-2] and middleband[-2] > middleband[-3]):
        jsonResult['布林_M_' + type] = '[/]'

    if (middleband[-1] < middleband[-2] and middleband[-2] < middleband[-3]):
        jsonResult['布林_M_' + type] = '[\]'


    if (doubleCloseArray[-1] < lowerband[-1]):
        jsonResult['布林_下穿_' + type] = 'Y'

    if (doubleCloseArray[-1] > upperband[-1]):
        jsonResult['布林_上穿_' + type] = 'Y'

    return upperband, middleband, lowerband, jsonResult, result

#upperband, middleband, lowerband, jsonResult, result = BBANDS('300201', 'D')
#print jsonResult
#print result