#encoding=utf-8
from pymongo import MongoClient
import time
import pandas as pd
import email_util

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


# 获取数据库链接
client = MongoClient('localhost', 27017)

# 获取数据库
db = client.get_database("Superman")

'''
###################################################################################################
插入记录
###################################################################################################
'''
def insertRecord(record):
    #获取表
    table = db.get_collection("report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
    table.insert(record)

def insertRecord(record,collectionName):
    #获取表
    table = db.get_collection(collectionName)
    table.insert(record)

'''
###################################################################################################
转化成DataFrame文件
###################################################################################################
'''
def toDataFrame(query,title):
    #获取表
    table = db.get_collection("report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
    cursor = table.find(query)
    df = pd.DataFrame(list(cursor))
    df.to_csv("./report/" + "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")
    email_util.sendMailAttatch(email_util.template2(""), title, "./report/" + "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv", "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")
    return df

def toDataFrame(query, title, collectionName):
    #获取表
    table = db.get_collection(collectionName)
    cursor = table.find(query)
    df = pd.DataFrame(list(cursor))
    df.to_csv("./report/" + collectionName + ".csv")
    email_util.sendQQMailWithAttatch(email_util.template2(""), title, "./report/" + collectionName + ".csv", collectionName + ".csv")
    return df


#df = ts.get_hist_data('600848',ktype='D')
#insertRecord(json.loads(df.to_json(orient='records')))

#json_str = { "course" : "chinese", "score" : 91, "name" : "wubiao"}
#insertRecord(json_str)
#print 'success'

#print toDataFrame({})
