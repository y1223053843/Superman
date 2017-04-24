#encoding=utf-8

import tushare as ts
import numpy as num
from com.alex.function.macd import *
from com.alex.function.bbands import *


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
     chiyou_code_index = num.array(['300349'])
     if (chiyou_code_index.__contains__(code)):
          return 'yes'

def dangqianjiage(code) :
     if (code == '000001'):
         code = 'sh'
     data_realTime = ts.get_realtime_quotes(code)

     realTimeArray = num.array(data_realTime['price'])
     realTimeArray = realTimeArray.astype(num.float)
     return realTimeArray[0]

def xiaomowangkuozhan(codeItem) :
     # MACD
     macd_60,macdsignal_60,macdhist_60,jsonResult_60,result_60,mairuresult_60,maichuresult_60  = MACD(codeItem,  '60')
     macd_D,macdsignal_D,macdhist_D,jsonResult_D,result_D,mairuresult_D,maichuresult_D  = MACD(codeItem,  'D')
     macd_W,macdsignal_W,macdhist_W,jsonResult_W,result_W,mairuresult_W,maichuresult_W  = MACD(codeItem,  'W')

     # 布林线
     upperband_60, middleband_60, lowerband_60, jsonResult_b_60, result_bl_60,mairuresult_bl_60,maichuresult_bl_60 = BBANDS(codeItem, '60')
     upperband_D, middleband_D, lowerband_D, jsonResult_b_D, result_bl_D,mairuresult_bl_D,maichuresult_bl_D = BBANDS(codeItem, 'D')

     xiaomowang = '<br>=============================='
     xiaomowang = xiaomowang + '<br>卖出信号：<br>' +  maichuresult_W + '<br>' + maichuresult_D + '<br>' + maichuresult_60 + '<br>' + maichuresult_bl_60 + '<br>' + maichuresult_bl_D
     xiaomowang = xiaomowang + '<br>买入信号：<br>' +  mairuresult_W + '<br>' + mairuresult_D + '<br> ' + mairuresult_60 + '<br>' + mairuresult_bl_60 + '<br>' + mairuresult_bl_D

     return xiaomowang


#print zhangdiefu('150212')
#print gupiaomingcheng('150212')
#print shifouchiyou('150212')
#print dangqianjiage('600547')