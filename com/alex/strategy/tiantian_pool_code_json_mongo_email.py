#encoding=utf-8

import sys
sys.path.append('/root/worksapce/Superman')
import logging
from pandas import DataFrame
import time as time
import lxml.html
import lxml.etree
import curl
from com.alex.utils.mongo_util import *
from com.alex.function.macd import *
from com.alex.function.bbands import *
import common
from com.alex.strategy.strategy001 import *

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
            query_result = [codeItem]
            strategy002(query_result, '【主题】【选】' + all_code.loc[codeItem,'hangye'], collectionName)
        except (IOError, TypeError, NameError, IndexError,Exception) as e:
            logging.error("error:" + codeItem)
            print e

'''
###############################################################################
主运行函数main
###############################################################################
'''
def download(url):
    c = curl.Curl()
    c.set_timeout(8)
    c.get(url)
    return c.body()

def get_all_code():
    base_url = 'http://www.ourkp.com/bk'
    ht_string = download(base_url)
    ht_doc = lxml.html.fromstring(ht_string, base_url)
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
    return all_code, all_title


param = sys.argv[0]
if (param == 1):
    print 'param:' + param
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====tiantian_code_json_mongo_email Start====='
    all_code, all_title = get_all_code()
    remove(collectionName)
    execute(all_code, all_title)

    #获取前两周时间数据
    toDataFrame_param({}, '★★★★★Tiantian_Pool_Code_JSON_Mongo' + time.strftime('%Y-%m-%d_%H:%M', time.localtime(time.time())) + '#【天天看盘】每30分更新#', collectionName)
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====tiantian_code_json_mongo_email End====='