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
import json

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
def list():
    browser = Browser('firefox')
    browser.visit(cf.get("URL", "url1"))
    browser.click_link_by_partial_text('登录')
    browser.find_by_xpath("//input[@class='w-input telephone']").fill(cf.get("Trade", "name"))
    browser.find_by_xpath("//input[@class='w-input password']").fill(cf.get("Trade", "password"))
    browser.find_by_xpath("//div[@class='btn-red loginBtn']").click()
    url = 'https://www.xrcj.com/api/index/sim-list'
    values = {
    'flgParam':'7',
    'start':'0',
    'length': '99'
    }

    try:
        #print browser.cookies.all()['SESSION']
        response = post(url, values,browser.cookies.all()['SESSION'])

        if (response.code == 200):
            print 'The List :'

        content = response.read()

        gzipped = response.headers.get('Content-Encoding')
        if gzipped:
            html= zlib.decompress(content, 16+zlib.MAX_WBITS)
            resultjson = json.loads(html)
            for a in resultjson['data']:
                print '%s %s %s profit:%s'%(a['subjectCode'],a['costPrice'],a['closeType'], a['clientProfit'])
                #print '%s %s %s %s profit:%s'%(a['subjectCode'],a['subjectName'],a['costPrice'],a['closeType'], a['clientProfit'])
                #print a
            #return resultjson

        time.sleep(10)
    finally:
        browser.quit()
        print '======success======'

list()




