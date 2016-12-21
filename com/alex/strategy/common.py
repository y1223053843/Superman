#encoding=utf-8

import tushare as ts
import numpy as num


def zhangdiefu(code):

     if (code == '000001'):
         code = 'sh'
     data_realTime = ts.get_realtime_quotes(code)

     realTimeArray = num.array(data_realTime['price'])
     realTimeArray = realTimeArray.astype(num.float)

     pre_close = num.array(data_realTime['pre_close'])
     pre_close = pre_close.astype(num.float)

     return "%.2f" % (((realTimeArray[0] - pre_close[0]) / pre_close[0]) * 100) + '%'

def gupiaomingcheng(code):

     if (code == '000001'):
          return '上证指数'
     data_realTime = ts.get_realtime_quotes(code)
     nameArray = num.array(data_realTime['name'])
     return nameArray[0]

def shifouchiyou(code) :
     chiyou_code_index = num.array(['600590', '002181'])
     if (chiyou_code_index.__contains__(code)):
          return 'yes'

#print zhangdiefu('150212')
#print gupiaomingcheng('150212')
#print shifouchiyou('150212')