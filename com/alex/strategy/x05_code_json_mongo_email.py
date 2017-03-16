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
常量 军工 半导体

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
    # 太极实业 600667
    # 亚翔集成 603929

    #LED
    #三安光电 600703
    #华灿光电 300323

    #芯片 设计
    #中颖电子 300327
    #紫光国芯 002049（停牌）

    #芯片封装
    #长电科技 600584
    #通富微电 002156
    #华天科技 002185

    #上游材料
    #南大光电 300346
    #濮阳惠成 300481
    #上海新阳 300236

    query_result = ['600667','603929','600703','300323','300327','600584','002156','002185','300346','300481','300236']
    strategy001(query_result, '【主题】半导体产业链', collectionName)

    #000415 渤海金控
    #600830 香溢融通
    query_result = ['000415','600830']
    strategy001(query_result, '【主题】融资租赁', collectionName)

    #600183 生益科技
    #002636 金安国纪
    #603228 景旺电子
    query_result = ['600183','002636','603228']
    strategy001(query_result, '【主题】PCB覆铜板', collectionName)

    #300316 晶盛机电
    #601012 隆基股份
    query_result = ['300316','601012']
    strategy001(query_result, '【主题】单晶硅供不应求', collectionName)

    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='