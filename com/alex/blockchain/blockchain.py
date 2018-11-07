#encoding=utf-8

import sys
sys.path.append('/root/worksapce/Superman')
import ConfigParser
import tushare as ts
import time

'''
##################################
常量
##################################
'''
cf = ConfigParser.RawConfigParser()
cf.read('../config/spark002_dev.conf')

'''
#################################
执行函数 execute
说明：
#################################
'''
def execute():
    pro = ts.pro_api("a0a3a3ee133d6623bf9072236a5a8423c1c021d00aba3eb0c7bdfa5e")
    df = pro.coinbar(exchange='huobi', symbol='btcusdt', freq='60min', start_date='20181001', end_date='20181002')
    print(df)

    # all_code = ts.get_stock_basics()
    # all_code_index = all_code[1:750].index
    # count = 0
    # all_code_index_x = num.array(all_code_index)
    # zhishu_code_index = num.array(['399006','399001','000001'])
    # for codeItem in all_code_index_x:
    #     count = count + 1
    #     print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "=====" + codeItem + ',Count:' + str(count)
    #     try:
    #         strategy002({codeItem}, all_code.loc[codeItem,'industry'], "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
    #     except (IOError, TypeError, NameError, IndexError,Exception) as e:
    #         print e
    #        logging.error("error:" + codeItem)


'''
###############################################################################
#主运行函数main
###############################################################################
'''
param = sys.argv[0]
if (param == 1):
    print 'param:' + param
else:
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====ALL_BLOCK_CHAIN_CODE_JSON_MONGO Start====='
    execute()
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +  '=====ALL_BLOCK_CHAIN_CODE_JSON_MONGO End====='