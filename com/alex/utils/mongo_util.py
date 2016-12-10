#encoding=utf-8
from pymongo import MongoClient
import time
import pandas as pd
import email_util
import datetime

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

def insertRecord_param(record,collectionName):
    #获取表
    table = db.get_collection(collectionName)
    table.insert(record)

'''
###################################################################################################
转化成DataFrame文件
###################################################################################################
'''
def toDataFrame(query_all, query_part, title_all, title_part):
    #获取表
    table = db.get_collection("report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
    cursor = table.find(query_all)
    df = pd.DataFrame(list(cursor))
    df.to_csv("./report/" + "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")
    email_util.sendQQMailWithAttatch(email_util.template2(""), title_all, "./report/" + "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv", "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")
    email_util.sendMailAttatch(email_util.template1(""), title_all, "./report/" + "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv", "report_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")

    cursor = table.find(query_part)
    df = pd.DataFrame(list(cursor))
    df.to_csv("./report/" + "report_part_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")
    email_util.sendQQMailWithAttatch(email_util.template2(""), title_part, "./report/" + "report_part_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv", "report_part_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")
    email_util.sendMailAttatch(email_util.template1(""), title_part, "./report/" + "report_part_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv", "report_part_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv")

    return df

def remove(collectionName):
    #获取表
    table = db.get_collection(collectionName)
    table.remove()

def toDataFrame_param(query, title, collectionName):
    #获取表
    table = db.get_collection(collectionName)
    cursor = table.find(query)
    df = pd.DataFrame(list(cursor))
    df.to_csv("./report/" + collectionName + ".csv")
    email_util.sendQQMailWithAttatch(email_util.template2(""), title, "./report/" + collectionName + ".csv", collectionName + ".csv")
    email_util.sendMailAttatch(email_util.template1(""), title, "./report/" + collectionName + ".csv", collectionName + ".csv")
    return df

def toDataFrame_param_for_tiantian(query, title, collectionName):
    #获取表
    table = db.get_collection(collectionName)
    cursor = table.find(query)
    listresult =list(cursor)
    print collectionName
    print listresult.__len__()

    today = datetime.date.today()
    #t = (1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15)
    t = (1,2,3,4,5,6,7)

    for i in t :
        nday = datetime.timedelta(days= i)
        curday = today - nday
        #print "report_tiantain_" + curday.strftime('%Y-%m-%d')
        table = db.get_collection("report_tiantain_" + curday.strftime('%Y-%m-%d'))
        cursor = table.find(query)
        listtmp = list(cursor)
        print "report_tiantain_" + curday.strftime('%Y-%m-%d')
        print listtmp.__len__()
        listresult = listresult + listtmp

    df = pd.DataFrame(listresult)

    #df.to_csv("./report/" + collectionName + ".csv")
    #email_util.sendQQMailWithAttatch(email_util.template2(""), title, "./report/" + collectionName + ".csv", collectionName + ".csv")
    return df


#df = ts.get_hist_data('600848',ktype='D')
#insertRecord(json.loads(df.to_json(orient='records')))

#json_str = { "course" : "chinese", "score" : 91, "name" : "wubiao"}
#insertRecord(json_str)
#print 'success'

#print toDataFrame({})
#toDataFrame_param_for_tiantian({}, 'B_Code_JSON_Mongo', "report_tiantain_" + time.strftime('%Y-%m-%d', time.localtime(time.time())))
