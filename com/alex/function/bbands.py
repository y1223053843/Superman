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
def BBANDS(codeCon, type, **values):
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
    highArray = num.array(data_history['high'])
    lowArray = num.array(data_history['low'])

    doubleCloseArray = num.asarray(closeArray,dtype='double')
    doubleHighArray = num.asarray(highArray,dtype='double')
    doubleLowArray = num.asarray(lowArray,dtype='double')

    upperband, middleband, lowerband = ta.BBANDS(doubleCloseArray, timeperiod=26, nbdevup=2, nbdevdn=2, matype=0)

    result = ''
    jsonResult = {}
    mairuresult = ''
    maichuresult = ''
    #if (middleband[-1] > middleband[-2] and middleband[-3] > middleband[-2]):
    #    jsonResult['布林_M_' + type] = '[V]'

    #if (middleband[-1] < middleband[-2] and middleband[-3] < middleband[-2]):
    #    jsonResult['布林_M_' + type] = '[/\]'

    #if (middleband[-1] > middleband[-2] and middleband[-2] > middleband[-3]):
    #    jsonResult['布林_M_' + type] = '[/]'

    #if (middleband[-1] < middleband[-2] and middleband[-2] < middleband[-3]):
    #    jsonResult['布林_M_' + type] = '[\]'

    tianshu = ''
    if (type == 'X'):
        if (middleband[-1] > middleband[-2]):
            tianshu = 'D_布林上升通道1天'

            if (middleband[-2] > middleband[-3]):
                tianshu = 'D_布林上升通道2天'

                if (middleband[-3] > middleband[-4]):
                    tianshu = 'D_布林上升通道3天'

                    if (middleband[-4] > middleband[-5]):
                        tianshu = 'D_布林上升通道4天'

        result = tianshu

    if (doubleLowArray[-1] < lowerband[-1]):
        jsonResult['布林_下穿_' + type] = 'Y'
        mairuresult = type + '_最低值下穿布林线下轨，买入'

    if (doubleHighArray[-1] > upperband[-1]):
        jsonResult['布林_上穿_' + type] = 'Y'
        maichuresult = type + '_最高值上穿布林线上轨，卖出'

    return upperband, middleband, lowerband, jsonResult, result,mairuresult,maichuresult

#upperband, middleband, lowerband, jsonResult, result,mairuresult,maichuresult = BBANDS('300201', 'D')
#print jsonResult
#print result