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

    #print macdsignal[-1]
    #print macdsignal[-2]
    #print macdsignal[-3]
    #print macdsignal[-4]
    #print macdsignal[-5]

    shangshengtianshu = 0
    if (type == 'D'):
        if (macd[-1] > macd[-2]):
            shangshengtianshu = 1

            if (macd[-2] > macd[-3]):
                shangshengtianshu = 2

                if (macd[-3] > macd[-4]):
                    shangshengtianshu = 3

                    if (macd[-4] > macd[-5]):
                        shangshengtianshu = 4

    return shangshengtianshu

#print MACD_shangshengtianshu('300463', 'D')
#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D')
#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D', end = '2016-12-15')
#print macd
#print jsonResult
#print result