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
常量 选股宝



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
    '''
    【主题】蚂蚁金服360
    蚂蚁金服上市
    002208 合肥城建
    601206 君正集团
    600895 张江高科

    360上市
    000839 中信国安
    300015 爱尔眼科
    600084 中葡股份
    '''
    query_result = ['002208','601206','600895','000839','300015','600084']
    strategy001(query_result, '【主题】蚂蚁360上市', collectionName)

    '''
    血制品
    300294 博雅生物
    002007 华兰生物

    涨价
    002449 国星光电 矾铁涨价
    002326 永太科技 萤石涨价

    钛白粉
    002136 安纳达
    002601 佰利联
    002145 中核钛白
    '''
    query_result = ['002136','002601','002145']
    strategy001(query_result, '【主题】钛白粉', collectionName)

    query_result = ['002449','002326']
    strategy001(query_result, '【主题】钒铁萤石制冷剂', collectionName)

    query_result = ['300294','002007']
    strategy001(query_result, '【主题】血制品', collectionName)

    '''
    共享单车
    600679 上海凤凰
    600818 中路股份
    002105 信隆健康

    华大基因上市
    002642 荣之联
    300009 安科生物
    300216 千山药机
    300016 北陆药业

    一带一路
    000425 徐工机械
    '''
    query_result = ['600679','600818','002105']
    strategy001(query_result, '【主题】共享经济', collectionName)

    query_result = ['002642','300009','300216','300016']
    strategy001(query_result, '【主题】基因', collectionName)

    query_result = ['000425']
    strategy001(query_result, '【主题】一带一路', collectionName)

    '''
    【主题】白酒
    600702 沱牌舍得
    000799 酒鬼酒
    600199 金种子酒
    '''
    query_result = ['600702','000799','600199']
    strategy001(query_result, '【主题】白酒', collectionName)

    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====my_code_json_mongo_email End====='