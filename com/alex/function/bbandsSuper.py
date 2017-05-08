#encoding=utf-8

import tushare as ts
import numpy as num
import talib as ta
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 布林中线上升天数
def BBANDS_shangshengtianshu(codeCon, type, **values):
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

    doubleCloseArray = num.asarray(closeArray,dtype='double')

    upperband, middleband, lowerband = ta.BBANDS(doubleCloseArray, timeperiod=26, nbdevup=2, nbdevdn=2, matype=0)

    #print middleband[-1]
    #print middleband[-2]
    #print middleband[-3]
    #print middleband[-4]
    #print middleband[-5]

    shangshengtianshu = 0
    if (type == 'D' or type == '60'):
        if (middleband[-1] > middleband[-2]):
            shangshengtianshu = 1

            if (middleband[-2] > middleband[-3]):
                shangshengtianshu = 2

                if (middleband[-3] > middleband[-4]):
                    shangshengtianshu = 3

                    if (middleband[-4] > middleband[-5]):
                        shangshengtianshu = 4

    return shangshengtianshu

#print BBANDS_shangshengtianshu('300463','D')
#upperband, middleband, lowerband, jsonResult, result,mairuresult,maichuresult = BBANDS('300201', 'D')
#print jsonResult
#print result