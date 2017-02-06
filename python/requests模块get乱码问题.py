# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.baidu.com')
#百度是用gbk来编码的，但是python控制台和文件是用utf-8编码的，如果不改变会报错或者出现乱码
r.encoding='utf-8'

bs = BeautifulSoup(r.text,'html.parser')
print(bs.find('title'))


'''
r.encoding
'utf-8'
r.encoding = 'ISO-8859-1'
如果你改变了编码，每当你访问 r.text ，Request都将会使用 r.encoding 的新值。
你可能希望在使用特殊逻辑计算出文本的编码的情况下来修改编码。
比如 HTTP 和 XML 自身可以指定编码。
这样的话，你应该使用 r.content 来找到编码，然后设置 r.encoding 为相应的编码。这样就能使用正确的编码解析 r.text 了。
'''