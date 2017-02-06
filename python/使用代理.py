# -*- coding:utf-8 -*-
import urllib.request
# # 通过urllib设置代理服务器来打开网页 
# proxy="113.66.147.42:9999"
# # 创建一个ProxyHandler对象
# proxy_support=urllib.request.ProxyHandler({'http':proxy})
# # 创建一个opener对象
# opener = urllib.request.build_opener(proxy_support)
# # 给request装载opener
# urllib.request.install_opener(opener)
# 打开一个url
# r = urllib.request.urlopen('http://www.baidu.com',timeout = 500)
# print(r.read())


#通过request 模块来使用代理
#代理格式是"http://127.0.0.1:80",如果要账号密码是"http://user:password@127.0.0.1:80"
import requests
proxies={
    'http:':'121.232.145.167:9000',
    'https:':'121.17.126.68:8081',
    }
# r =requests.get('http://bbs.north-plus.net',proxies=proxies)
r =requests.get('http://share.dmhy.org',proxies=proxies)
print(r.text) 