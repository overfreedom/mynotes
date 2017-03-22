# -*- coding:utf-8 -*-

def FormatPascal(str):
    if str.__len__() == 0:
        return None;
    result = str.lower()
    ls = result.split(sep='_')
    result = ''
    if len(ls)>1:        
        for i in ls:
            tmp = i.strip()    
            if len(tmp)>1:
                result += tmp[0].upper()+tmp[1:]+'_'                
            else:
                result += tmp+'_';      
        return result[0:-1];
    else:
        i = ls[0]
        return (i[0].upper()+i[1:]).strip()
    
if __name__ == "__main__":
    pls = """CI_ID
INVOICE_NO
INVOICE_SUM
INSURE_SUM
PL_SUM
SHOULDPAY_DATE
CORP_SERIAL_NO
CLIENT_NO
IMPORT_EDI_FLAG
CITIC_IMPORT_STATUS
REMARKS
APPLIED_AMOUNT
SHIPMENT_APPLY_TIME
UNIT_ID
BUSI_ROLE_ID
CREATED_BY
CREATION_DATE
LAST_UPDATED_BY
LAST_UPDATE_DATE
ATTRIBUTE1
ATTRIBUTE2
ATTRIBUTE3
ATTRIBUTE4
ATTRIBUTE5
ATTRIBUTE6
ATTRIBUTE7
ATTRIBUTE8
ATTRIBUTE9
ATTRIBUTE10
ATTRIBUTE11
ATTRIBUTE12
ATTRIBUTE13
ATTRIBUTE14
ATTRIBUTE15
PLNOTICE_REQ_DETAIL_ID
PLNOTICE_REQ_ID
SHIPMENT_DECLARE_DETAIL_ID       
"""

    comment = '''商业发票ID
发票编号
发票金额
投保金额
可损金额
应付款日
信保路由号
企业标识
导入接口标志
中信保导入状态
备注
已核销金额
申报日期
组织ID
角色ID
创建人
创建时间
修改人
修改时间
预留字段1
预留字段2
预留字段3
预留字段4
预留字段5
预留字段6
预留字段7
预留字段8
预留字段9
预留字段10
预留字段11
预留字段12
预留字段13
预留字段14
预留字段15
可损通知申请明细ID
可损通知申请ID
出运申报明细ID
'''

    comment2 = '''
'''

    type ='''NUMBER
VARCHAR2
NUMBER
NUMBER
NUMBER
DATE
NUMBER
VARCHAR2
VARCHAR2
NUMBER
VARCHAR2
NUMBER
DATE
NUMBER
NUMBER
NUMBER
DATE
NUMBER
DATE
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
NUMBER
NUMBER
NUMBER
'''


 
    l = pls.split(sep='\n')
    l2 = comment.split(sep='\n')
    l3 = comment2.split(sep='\n')
    l4 = type.split(sep='\n')
    for i in range(len(l)):
        if len(l3)<2:
            if l2[i]==l3[i]:
                print('/**'+l2[i]+'*/')
            else:           
                print('/**'+l2[i]+'   '+l3[i]+'*/')
        else:
            print('/**'+l2[i]+'*/')            
        if 'VARCHAR2'==l4[i]: 
            print('public String '+FormatPascal(l[i])+';')
        elif 'DATE' ==l4[i]:
            print('public Date '+FormatPascal(l[i])+';')
        elif 'NUMBER' == l4[i]:
            print('public BigDecimal '+FormatPascal(l[i])+';')
        else:
            print('it not math type')
