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

    upperband, middleband, lowerband = ta.BBANDS(num.asarray(closeArray,dtype='double'), timeperiod=26, nbdevup=2, nbdevdn=2, matype=0)

    result = ''
    jsonDic = {}
    if (middleband[-1] > middleband[-2] and middleband[-3] > middleband[-2]):
        jsonDic['bbans_M_' + type] = '[V]'

    if (middleband[-1] < middleband[-2] and middleband[-3] < middleband[-2]):
        jsonDic['bbans_M_' + type] = '[/\]'

    if (middleband[-1] > middleband[-2] and middleband[-2] > middleband[-3]):
        jsonDic['bbans_M_' + type] = '[/]'

    if (middleband[-1] < middleband[-2] and middleband[-2] < middleband[-3]):
        jsonDic['bbans_M_' + type] = '[\]'

    return jsonDic,result

#jsonDic,result = BBANDS('300201', 'D')
#print jsonDic
#print result