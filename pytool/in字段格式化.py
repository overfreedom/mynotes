# -*- coding:utf-8 -*-
'''
用来格式化sql语句中in 
@author: Administrator
'''
class Temp:
    str=''' 
SOH201706300021
SOH201706290052
SOH201706150128
SOH201706230115
SOH201706170123
SOH201706220048'''

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