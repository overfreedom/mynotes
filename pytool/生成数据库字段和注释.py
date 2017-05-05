# -*- coding:utf-8 -*-

    
if __name__ == "__main__":
    pls = """CLIENTNO
SINOSUREBUYERNO
IFREPEAT
CORPOPENBANKNO
CORPOPENBANKSWIFT
CORPEXBANKNO
CORPEXBANKSWIFT
IFHISTTRADE
LASTYEAR1
LASTPAYMODE1
LASTSUM1
LASTYEAR2
LASTPAYMODE2
LASTSUM2
LASTYEAR3
LASTPAYMODE3
LASTSUM3
BANKPAYBEHAVE
OWEFLAG
OWEELSERESON
REMARK
DECLARATION
FILENUM
IFSAMEWITHPOLICY
PRECREDITTERM
AFTERCREDITTERM
"""

    comment = '''企业标识
中国信保买方代码
是否循环
开证行企业内部编码
企业填写开证行SWIFT
保兑行企业内部编码
企业填写保兑行SWIFT
是否曾收到该银行开立的信用证
最近三年交易年份1
最近三年交易结算方式1
最近三年交易金额1
最近三年交易年份2
最近三年交易结算方式2
最近三年交易金额2
最近三年交易年份3
最近三年交易结算方式3
最近三年交易金额3
银行付款表现
银行付款异常原因代码
其他银行付款异常原因
其他说明
被保险人声明
附件个数
是否与保单出运前约定一致
出运前信用期限
出运后信用期限
'''

    comment2 = '''30
30
100
100
100
100
100
1
4
10
100
4
10
100
4
10
100
1
30
500
4000
1
2
1
3
3
'''

    type ='''VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
'''


 
    l = pls.split(sep='\n')
    l2 = comment.split(sep='\n')
    l3 = comment2.split(sep='\n')
    l4 = type.split(sep='\n')
    resultsql ='alter table Mms_Lc_Credit_Insurance add(\n' 
    for i in range(len(l)-1):
        resultsql +='  '+l[i]+'  '+l4[i]+'('+l3[i]+'),\n'
    resultsql+=');'

#     print(resultsql)
 
    for i in range(len(l)-1):
        reusltsql ="comment on column Mms_Lc_Credit_Insurance."+l[i]+" is '"+l2[i]+"';"
        print(reusltsql)
