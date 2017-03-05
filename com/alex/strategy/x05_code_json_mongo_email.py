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
from com.alex.strategy.strategy001 import *
import common

'''
##################################
常量 军工

##################################
'''
collectionName = "report_GXDC_" + time.strftime('%Y-%m-%d', time.localtime(time.time()))

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
    #execute_param()
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email Start====='


    # 半导体 晶圆厂 帮人家盖晶圆厂及无尘室
    # 太极实业
    # 亚翔集成

    #LED
    #三安光电
    #华灿光电

    #芯片 设计
    #中颖电子
    #紫光国芯

    #芯片封装
    #长电科技
    #通富微电
    #华天科技

    #上游材料
    #南大光电
    #濮阳惠成
    #上海新阳

    query_result = ['600679','600818','002105']
    strategy001(query_result, '【主题】共享经济', collectionName)

    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='