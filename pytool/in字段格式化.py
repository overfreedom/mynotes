# -*- coding:utf-8 -*-
'''
用来格式化sql语句中in 
@author: Administrator
'''
class Temp:
    str='''S1612260144
S1612260196
S1612260419'''

def inFormat(_str,isStr=False):
    result = 'in ('
    strls = _str.strip().split(sep="\n");
    if isStr:        
        for i in strls:
            result += "'"+i.strip()+"',"
        result = result[0:-1]+')'
        print(result)
    else:
        for i in strls:
            result += i.strip()+","
        result = result[0:-1]+')'
        print(result)

if __name__ =='__main__':
    t = Temp()        
    inFormat(t.str,1)