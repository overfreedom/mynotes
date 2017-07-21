# -*- coding:utf-8 -*-
'''
Created on 2017年3月22日

@author: Administrator
'''

def Java2Delphi(_str):
    if _str.strip() =='': return    
    if _str.strip().startswith('/*'):
        print('//'+_str)
        return
    l = _str.strip().split(sep=' ')
    if len(l)<3 : return
    if l[1]=='String':
        print("F"+l[2][0:-1]+":string;")
    elif l[1]=='int':
        print("F"+l[2][0:-1]+":Integer;")
    elif l[1] == 'BigDecimal':
        print("F"+l[2][0:-1]+":double;")
    elif l[1] == 'Date':
        print("F"+l[2][0:-1]+":string;")
    elif l[1] == 'DataRelation':
        print("F"+l[2]+":TList;")        
    else:  
        print("未定义类型")
        
def Java2DelphiProperty(_str):
    if _str.strip() =='': return    
    if _str.strip().startswith('/*'):
        print('//'+_str)
        return
    l = _str.strip().split(sep=' ')
    if len(l)<3 : return
    if l[1]=='String':
        print("property "+l[2][0:-1]+":string read F"+l[2][0:-1]+"  write  F"+l[2][0:-1]+';')
    elif l[1]=='int':
        print("property "+l[2][0:-1]+":Integer read F"+l[2][0:-1]+"  write  F"+l[2][0:-1]+';')
    elif l[1] == 'BigDecimal':
        print("property "+l[2][0:-1]+":double read F"+l[2][0:-1]+"  write  F"+l[2][0:-1]+';')
    elif l[1] == 'Date':
        print("property "+l[2][0:-1]+":string read F"+l[2][0:-1]+"  write  F"+l[2][0:-1]+';')
    elif l[1] == 'DataRelation':
        print("property "+l[2]+":TList read F"+l[2]+"  write  F"+l[2]+';')        
    else:  
        print("未定义类型")
        
if __name__ =='__main__':
    pstr='''
p String ACC_DATE, 
p String AGING_DATE, 
p String HG_INV_NO, 
p String HG_ACC_DATE, 
'''

    l = pstr.split(sep='\n')
    for i in l:
        Java2Delphi(i)
    print('*'*20)
    for i in l:
        Java2DelphiProperty(i)