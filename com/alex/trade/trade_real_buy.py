#encoding=utf-8

import sys
import time
sys.path.append('/root/worksapce/Superman')
sys.path.append('d:\workspace\Git\Superman')
import urllib2
import urllib
import cookielib
import ConfigParser
from splinter import Browser
from com.alex.strategy.common import *
import zlib

#读取配置配置文件
cf = ConfigParser.RawConfigParser()
cf.read("../config/config.conf")

'''
发送post请求
'''
def post(url, data,cookie):
    req = urllib2.Request(url)
    req.add_header('Accept','application/json, text/javascript, */*; q=0.01')
    req.add_header('Accept-Encoding','gzip, deflate, br')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    req.add_header('Cache-Control','no-cache')
    req.add_header('Connection','keep-alive')
    req.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
    req.add_header('Host','www.xrcj.com')
    req.add_header('Origin','https://www.xrcj.com')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36')

    #cookie
    req.add_header('Cookie','SESSION=' + cookie)
    req.add_header('Pragma','no-cache')
    req.add_header('X-Requested-With','XMLHttpRequest')
    req.add_header('x-site-id','100010')
    req.add_header('x-term','2')
    data = urllib.urlencode(data)
    #enable cookie
    cj=cookielib.CookieJar()
    #cj.set_cookie(cookie)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    response = opener.open(req, data, timeout=30)
    #print response.code
    #print 'message:' + response.msg
    return response

'''
买入
'''
def buy(fullcode,code, shipan):
    print dangqianjiage(code)
    browser = Browser('firefox')
    browser.visit(cf.get("URL", "url1"))
    browser.click_link_by_partial_text('登录')
    browser.find_by_xpath("//input[@class='w-input telephone']").fill(cf.get("Trade", "name"))
    browser.find_by_xpath("//input[@class='w-input password']").fill(cf.get("Trade", "password"))
    browser.find_by_xpath("//div[@class='btn-red loginBtn']").click()
    url = 'https://www.xrcj.com/api/trading-sec/create-stock'
    values = {
    'subjectId':fullcode,
    'createMode':'1',
    'strategyId': shipan + '0101-00-1000',
    'strategyType':shipan,
    'marginRate':'10',
    'openAsset':'1',
    'openPrice':dangqianjiage(code),
    'openEntrustCmd':'1',
    'stopSwitch':'0',
    'marginStopLossRate':'',
    'marginStopProfitRate':'',
    'sourceDealingNo':''
    }

    try :
        #print browser.cookies.all()['SESSION']
        response = post(url, values,browser.cookies.all()['SESSION'])
        content = response.read()
        gzipped = response.headers.get('Content-Encoding')
        if gzipped:
            html= zlib.decompress(content, 16+zlib.MAX_WBITS)
            print html
            #return html

        time.sleep(3)
    finally:
        browser.quit()
        print '======success======'

count = len(sys.argv)
if count == 1 :
    print "Please input the param:"
    print "1:Shan Dong Huang Jin"
    print "2:Ke Da Xun Fei"
    print "3:Jin Ma Gu Fen"
    print "4:Qiu Lin Ji Tuan"
    time.sleep(10)
else:
    param = sys.argv[1]
    if (param == '1'):
        buy('SH600547','600547','R')
    elif (param == '2'):
        buy('SZ002230','002230','R')
    elif (param == '3'):
        buy('SZ000980','000980','R')
    elif (param == '4'):
        buy('SH600891','600891','R')
    else:
        if (param.startswith('600') or param.startswith('601')):
            buy('SH' + param, param, 'R')
        elif (param.startswith('300') or param.startswith('000') or param.startswith('002')):
            buy('SZ' + param, param, 'R')
        else:
            print "Please input the param:"
            print "1:Shan Dong Huang Jin"
            print "2:Ke Da Xun Fei"
            print "3:Jin Ma Gu Fen"
            print "4:Qiu Lin Ji Tuan"
            time.sleep(10)