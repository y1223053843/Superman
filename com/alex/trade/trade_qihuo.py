#encoding=utf-8

import sys
import time
sys.path.append('/root/worksapce/Superman')

import urllib2
import urllib
import cookielib
import ConfigParser

#读取配置配置文件
cf = ConfigParser.RawConfigParser()
cf.read("../config/config.conf")


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
    response = opener.open(req, data)
    print response.code
    print 'message:' + response.msg
    return response.read()


from splinter import Browser

browser = Browser('firefox')
browser.visit(cf.get("URL", "url1"))
browser.click_link_by_partial_text('登录')
browser.find_by_xpath("//input[@class='w-input telephone']").fill(cf.get("Trade", "name"))
browser.find_by_xpath("//input[@class='w-input password']").fill(cf.get("Trade", "password"))
browser.find_by_xpath("//div[@class='btn-red loginBtn']").click()


url = 'https://www.xrcj.com/api/trading-fu/create-futures'
values = {
'subjectId':'au1706',
'createMode':'1',
'strategyId':'S0402-10-1000',
'strategyType':'S',
'clientMarginRate':'0.7',
'openQty':'1',
'openPrice':'271.9',
'openEntrustCmd':'1',
'stopSwitch':'0',
'marginStopLossRate':'',
'marginStopProfitRate':'',
'exchange':'2',
'contractNo':'au1706',
'direction':'1',
'sourceDealingNo':''
}

print browser.cookies.all()['SESSION']
print post(url, values,browser.cookies.all()['SESSION'])


time.sleep(10)
browser.quit()


