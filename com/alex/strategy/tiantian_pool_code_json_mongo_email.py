#encoding=utf-8

import sys
sys.path.append('/root/worksapce/Superman')
import logging
import ConfigParser
from pandas import DataFrame
import tushare as ts
import time
import numpy
import lxml.html
import lxml.etree
import curl
from com.alex.utils.mongo_util import *
from com.alex.function.macd import *
from com.alex.function.bbands import *

'''
##################################
常量
##################################
'''
collectionName = "report_tiantain_" + time.strftime('%Y-%m-%d', time.localtime(time.time()))

'''
#################################
执行函数 execute
说明：
#################################
'''
def execute(all_code_index, all_title):

    all_code = DataFrame(all_title,index=all_code_index,columns=['hangye'])

    for codeItem in all_code_index:
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem
        try:

            macd_30,macdsignal_30,macdhist_30,jsonResult_30,result_30  = MACD(codeItem,  '30')
            macd_60,macdsignal_60,macdhist_60,jsonResult_60,result_60  = MACD(codeItem,  '60')
            macd_D,macdsignal_D,macdhist_D,jsonResult_D,result_D  = MACD(codeItem,  'D')
            macd_W,macdsignal_W,macdhist_W,jsonResult_W,result_W  = MACD(codeItem,  'W')
            upperband_30, middleband_30, lowerband_30, jsonResult_b_30, result_30 = BBANDS(codeItem, '30')
            upperband_60, middleband_60, lowerband_60, jsonResult_b_60, result_60 = BBANDS(codeItem, '60')
            upperband_D, middleband_D, lowerband_D, jsonResult_b_D, result_D = BBANDS(codeItem, 'D')
            upperband_W, middleband_W, lowerband_W, jsonResult_b_W, result_W = BBANDS(codeItem, 'W')

            jsonDic = {}
            jsonDic['1时间'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            jsonDic['2编码'] = '_' + codeItem
            jsonDic['3行业'] = all_code.loc[codeItem,'hangye']
            #jsonDic['所属行业'] = all_code.loc[codeItem,'industry']
            #jsonDic['PE'] = all_code.loc[codeItem,'pe']
            jsonDic['验证_MACD_30'] =  '%.3f' % macd_30[-1] + '_' +  '%.3f' % macd_30[-2] + '_' +  '%.3f' % macd_30[-3]
            jsonDic['验证_MACD_60'] =  '%.3f' % macd_60[-1] + '_' +  '%.3f' % macd_60[-2] + '_' +  '%.3f' % macd_60[-3]
            jsonDic['验证_MACD_D'] =  '%.3f' % macd_D[-1] + '_' +  '%.3f' % macd_D[-2] + '_' +  '%.3f' % macd_D[-3]
            jsonDic['验证_MACD_W'] =  '%.3f' % macd_W[-1] + '_' +  '%.3f' % macd_W[-2] + '_' +  '%.3f' % macd_W[-3]
            jsonDic['验证_布林_30'] =  '%.3f' % middleband_30[-1] + '_' +  '%.3f' % middleband_30[-2] + '_' +  '%.3f' % middleband_30[-3]
            jsonDic['验证_布林_60'] =  '%.3f' % middleband_60[-1] + '_' +  '%.3f' % middleband_60[-2] + '_' +  '%.3f' % middleband_60[-3]
            jsonDic['验证_布林_D'] =  '%.3f' % middleband_D[-1] + '_' +  '%.3f' % middleband_D[-2] + '_' +  '%.3f' % middleband_D[-3]
            jsonDic['验证_布林_W'] =  '%.3f' % middleband_W[-1] + '_' +  '%.3f' % middleband_W[-2] + '_' +  '%.3f' % middleband_W[-3]

            jsonParam = dict(jsonResult_30.items() + jsonResult_60.items() + jsonResult_D.items()
                             + jsonResult_W.items() + jsonResult_b_30.items() + jsonResult_b_60.items()
                             + jsonResult_b_D.items() + jsonResult_b_W.items() + jsonDic.items())

            insertRecord_param(jsonParam, collectionName)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            logging.error("error:" + codeItem)

'''
###############################################################################
主运行函数main
###############################################################################
'''
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====tiantian_code_json_mongo_email Start====='
def download(url):
    c = curl.Curl()
    c.set_timeout(8)
    c.get(url)
    return c.body()

base_url = 'http://www.ourkp.com/bk'
ht_string = download(base_url)
#print ht_string
ht_doc = lxml.html.fromstring(ht_string, base_url)
#print ht_doc
elms = ht_doc.xpath("//div[@class='hotT']/ul/li")

result = ''

all_code = []
all_title = []
for i in elms:
    title = i.xpath("./strong")[0].get("title")
    result += '<br><B>' + title + '</B><br>'
    print  '[' + time.strftime('%m-%d', time.localtime(time.time())) +  title + ']'
    ps = i.xpath("./p/a[@class='hot']")
    for p in ps:
        code = p.get('stockcode')
        print code
        all_code.append(code)
        all_title.append(title)

execute(all_code, all_title)
toDataFrame_param({}, 'Tiantian_Pool_Code_JSON_Mongo', collectionName)
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====tiantian_code_json_mongo_email End====='