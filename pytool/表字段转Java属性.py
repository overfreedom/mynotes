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
    pls = """ATTRIBUTE12
ATTRIBUTE13
ATTRIBUTE14
ATTRIBUTE15
ALTER_DETAILS_ID
ALTER_BATCH_ID
CORP_ALTER_SERIAL_NO
SHIPMENT_ID
CORP_SERIAL_NO
CLIENT_NO
POLICY_NO
BUYER_NO
CORP_BUYER_NO
BUYER_CHN_NAME
BUYER_ENG_NAME
BUYER_COUNTRY_CODE
BUYER_ENG_ADDR
BUYER_CHN_ADDR
BUYER_REG_NO
BUYER_TEL
BUYER_FAX
BANK_NO
CORP_BANK_NO
BANK_CHN_NAME
BANK_ENG_NAME
BANK_COUNTRY_CODE
BANK_COUNTRY_NAME
BANK_ADDR
INVOICE_NO
INVOICE_SUM
INSURE_SUM
MONEY_ID
PAY_TERM
PAY_MODE
FEE_PAY_MODE
TRAFFIC_CODE
TRANSPORT_DATE
CODE10
GOODS_NAME
CONTRACT_NO
TRANSPORT_BILL_NO
CUSTOMS_BILL_NO
SHIPMENT_REMARK
IF_FINANCING
EMPLOYEE_NAME
ALTER_REASON
APPLICANT_NAME
APPLY_TIME
FILE_NUM
MODIFY_MSG
STATUS
ITEM1
ITEM2
ITEM3
ITEM4
ITEM5
CUSTOMER_ID
EXPORT_ORG_ID
INSURANCE_POLICY_ID
SHIPMENT_DECLARE_DETAIL_ID
UNIT_ID
BUSI_ROLE_ID
VERSION
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
"""

    comment = '''备用12
备用13
备用14
备用15
出运变更明细ID
出运变更批ID
流水号
信保通出运ID
企业内部申报流水号  路由号
企业标识
保险单号
中国信保买方代码
企业买方代码
买方中文名称
买方英文名称
买方国家代码
买方英文地址
买方中文地址
买方注册号
买方电话
买方传真
信保开证行SWIFT
企业开证行代码
开证行中文名称
开证行英文名称
开证行国家代码
开证行国家名称
开证行地址
发票编号
发票金额 
投保金额 
出运货币代码
合同支付期限
合同支付方式
缴费支付方式
运输方式
出运日期
海关10位商品代码
商品名称
合同号
提单号
报关单号
保户特别说明
是否需要申请融资
业务员名称
变更原因
申请人姓名
申请时间
附件数
变更说明
状态
备用1
备用2
备用3
备用4
备用5
客户ID
出口组织
保险单号ID
原出运申报明细ID
组织ID
角色ID
版本
创建人
创建时间
修改人
修改时间
备用1
备用2
备用3
备用4
备用5
备用6
备用7
备用8
备用9
备用10
备用11
'''

    comment2 = '''
'''

    type ='''VARCHAR2
VARCHAR2
VARCHAR2
VARCHAR2
NUMBER
NUMBER
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
NUMBER
NUMBER
VARCHAR2
NUMBER
VARCHAR2
VARCHAR2
VARCHAR2
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
NUMBER
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
NUMBER
NUMBER
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
'''


 
    l = pls.split(sep='\n')
    l2 = comment.split(sep='\n')
    l3 = comment2.split(sep='\n')
    l4 = type.split(sep='\n')
    for i in range(len(l)-1):
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
            print('public int '+FormatPascal(l[i])+';')
        else:
            print('it not math type')
