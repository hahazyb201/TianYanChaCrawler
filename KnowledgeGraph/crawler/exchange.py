#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib.parse import urlencode
from urllib.parse import urlopen
#----------------------------------
# 货币汇率调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/23
#----------------------------------
 
def main():
 
    #配置您申请的APPKey
    appkey = "*********************"
 
    #1.人民币牌价
    request1(appkey,"GET")
 
    #2.外汇汇率
    request2(appkey,"GET")
 
 
 
#人民币牌价
def request1(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/exchange/rmbquot"
    params = {
        "key" : appkey, #APP Key
        "type" : "", #两种格式(0或者1,默认为0)
 
    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print("request api error")
 
#外汇汇率
def request2(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/exchange/frate"
    params = {
        "key" : appkey, #APP Key
        "type" : "", #两种格式(0或者1,默认为0)
 
    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print("request api error")
 
 
 
if __name__ == '__main__':
    main()