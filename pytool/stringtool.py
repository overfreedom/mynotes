#!/usr/bin/env python
# -*- coding:utf8 -*-

# # 字符串按分割符切割后返回
# # start_index 每个子字符串开始分割位置  length 分割长度  cut_char分割标志   str_target 传进字符串 
def StrCut(start_index, length, cut_char, str_target):    
    str_list = str_target.split(sep=cut_char)
    str_result = ''
    for i in str_list:
        if (length == -1) :
            str_result += i[start_index:] + cut_char
        else:
            str_result += i[start_index:length] + cut_char
    return str_result[:-1]    

"""
    字符串按分割符切分，然后追加一个字符串，再拼接返回
    str_source,传入的字符串   cut_char,分割的字符串    insert_str 插入的字符串
"""
def StrConnect(str_source, cut_char, insert_str_head='', insert_str_last=''):
    str_list = str_source.split(cut_char)    
    str_result = ''
    for i in str_list :
        if i == '' : continue 
        str_result += insert_str_head + i + insert_str_last + '\n'
    return str_result[:-2]    
    
        
# #print(StrCut(4, -1, ',', "bedtdes_port,bedtdes_country,bedtCONS_COUNTRY,bedttrans_man,bedttrans_tel,bedttrans_email,bedttrans_org"))        

source_str = """CRM_ITEM_PACK_ID
MRPORGID
ITEM_ID
ITEM_CODE
DRAW_ID
PKG_TYPE
CUST_ID
SHORT_NAME
PKG_QTY
NET_WEIGHT
GROSS_WEIGHT
PKG_GROSS_WEIGHT
LENGTH_WIDTH_HEIGHT
CUBAGE
MEASUREMENT
SINGLE_WEIGHT_OTHER
OUT_DRAWID
OUT_DRAWNAME
VOLTAGE_TYPE
POWER
POWER_FREQUENCY
BAND
NOTE
CREATOR
CREATE_TIME
UPDATOR
UPDATE_TIME
REF_NET_WEIGHT
REF_LENGTH_WIDTH_HEIGHT
REF_PKG_GROSS_WEIGHT
REF_PKG_QTY
REF_OUT_DRAWID
REF_BAND
REF_POWER
REF_VOLTAGE_TYPE
REF_POWER_FREQUENCY
REF_OUT_DRAWNAME
BASE_SIZE
LAST_UPDATER
LAST_UPDATETIME
LATEST_UPDATER
LATEST_UPDATETIME
"""
print(StrConnect(source_str, '\n', 'h.', insert_str_last=','))    
