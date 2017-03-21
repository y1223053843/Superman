#encoding=utf-8

import sys
sys.path.append('/root/worksapce/Superman')
import logging
from pandas import DataFrame
import time as time
from com.alex.utils.mongo_util import *
from com.alex.utils.mysql_util import *
from com.alex.function.macd import *
from com.alex.function.bbands import *
import common
from com.alex.strategy.strategy001 import *

'''
##################################
常量 智能制造（人工智能，工业4.0）
002230 科大讯飞
300131 英唐智控
002439 启明星辰 投资达闼科技 人工智能机器人
##################################
'''
collectionName = "report_ZNZZ_" + time.strftime('%Y-%m-%d', time.localtime(time.time()))

'''
########################
主运行函数main
########################
'''

count = len(sys.argv)
if (count == 2):
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email Start====='
    #param = sys.argv[1]
    #print param
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email Start====='
    #002230 科大讯飞
    #300131 英唐智控
    #002439 启明星辰
    #300222 科大智能
    #300044 赛为智能
    query_result = ['002230','300131','002439','300222','300044']
    strategy001(query_result, '【主题】人工智能', collectionName)


    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='