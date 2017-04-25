#encoding=utf-8

import tushare as ts
import numpy as num
import talib as ta
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# macd慢线上升天数
def MACD_shangshengtianshu(codeCon, type, **values):
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

    shangshengtianshu = 0
    if (type == 'D'):
        if (macdsignal[-1] > macdsignal[-2]):
            shangshengtianshu = 1

            if (macdsignal[-2] > macdsignal[-3]):
                shangshengtianshu = 2

                if (macdsignal[-3] > macdsignal[-4]):
                    shangshengtianshu = 3

    return shangshengtianshu

#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D')
#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D', end = '2016-12-15')
#print macd
#print jsonResult
#print result