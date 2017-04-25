#encoding=utf-8

import tushare as ts
import numpy as num
import talib as ta
import sys
sys.path.append('/root/worksapce/Superman')
from com.alex.function.bbandsSuper import *
from com.alex.function.macdSuper import *
'''
#####################################
执行函数:MACD 和 布林线上升并行天数，
如果并行天数为1，则为买入点
#####################################
'''
def MACD_Bull_bingxingtianshu(codeCon, type, **values):
    macd_shangshengtianshu = MACD_shangshengtianshu(codeCon,type)
    bbands_shangshengtianshu = BBANDS_shangshengtianshu(codeCon,type)
    min_shangshengtianshu = min(macd_shangshengtianshu, bbands_shangshengtianshu)

    return macd_shangshengtianshu,bbands_shangshengtianshu,min_shangshengtianshu

#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D')
#macd,macdsignal,macdhist,jsonResult,result,mairuresult,maichuresult = MACD('399006', 'D', end = '2016-12-15')
#print macd
#print jsonResult
#print result