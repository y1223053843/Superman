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
def MA(codeCon, type, zhouqi):

    data_history = ''
    if (codeCon == '000001'):
        data_history = ts.get_k_data(codeCon, ktype = type,index='true')
    else:
        data_history = ts.get_k_data(codeCon, ktype = type)

    closeArray = num.array(data_history['close'])
    real = ta.MA(num.asarray(closeArray,dtype='double'),timeperiod=zhouqi, matype=0)

    tableresult = ''
    tianshu = ''
    if (type == 'D' or type == '60'):
        if (real[-1] > real[-2]):
            tianshu =  '20_' + type + '上升通道1天'

            if (real[-2] > real[-3]):
                tianshu =  '20_' + type + '上升通道2天'

                if (real[-3] > real[-4]):
                    tianshu =  '20_' + type + '上升通道3天'

                    if (real[-4] > real[-5]):
                        tianshu =  '20_' + type + '上升通道4天'

        tableresult = tianshu

    return real,tableresult

#real,tableresult = MA('002576', 'D', 20)
#print real,tableresult
#print result