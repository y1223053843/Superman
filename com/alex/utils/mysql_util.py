#encoding=utf-8
import mysql.connector

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

config={'host':'127.0.0.1',#默认127.0.0.1
        'user':'root',
        'password':'1qaz@WSX',
        'port':3306 ,#默认即为3306
        'database':'superman',
        'charset':'utf8'#默认即为utf8
        }

try:
    cnn=mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))


def chaxun():
    cursor=cnn.cursor()

    try:
        sql_query='select id,code,name,type,tag from superman_jiankong where enable_status = %s'
        cursor.execute(sql_query,(1,))
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print('query error!{}'.format(e))
    finally:
        cursor.close()
        cnn.close()
