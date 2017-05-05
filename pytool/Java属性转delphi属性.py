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
    pstr='''    /**备用12*/
    public String Attribute12;
    /**备用13*/
    public String Attribute13;
    /**备用14*/
    public String Attribute14;
    /**备用15*/
    public String Attribute15;
    /**出运变更明细ID*/
    public int Alter_Details_Id;
    /**出运变更批ID*/
    public int Alter_Batch_Id;
    /**流水号*/
    public String Corp_Alter_Serial_No;
    /**信保通出运ID*/
    public String Shipment_Id;
    /**企业内部申报流水号  路由号*/
    public String Corp_Serial_No;
    /**企业标识*/
    public String Client_No;
    /**保险单号*/
    public String Policy_No;
    /**中国信保买方代码*/
    public String Buyer_No;
    /**企业买方代码*/
    public String Corp_Buyer_No;
    /**买方中文名称*/
    public String Buyer_Chn_Name;
    /**买方英文名称*/
    public String Buyer_Eng_Name;
    /**买方国家代码*/
    public String Buyer_Country_Code;
    /**买方英文地址*/
    public String Buyer_Eng_Addr;
    /**买方中文地址*/
    public String Buyer_Chn_Addr;
    /**买方注册号*/
    public String Buyer_Reg_No;
    /**买方电话*/
    public String Buyer_Tel;
    /**买方传真*/
    public String Buyer_Fax;
    /**信保开证行SWIFT*/
    public String Bank_No;
    /**企业开证行代码*/
    public String Corp_Bank_No;
    /**开证行中文名称*/
    public String Bank_Chn_Name;
    /**开证行英文名称*/
    public String Bank_Eng_Name;
    /**开证行国家代码*/
    public String Bank_Country_Code;
    /**开证行国家名称*/
    public String Bank_Country_Name;
    /**开证行地址*/
    public String Bank_Addr;
    /**发票编号*/
    public String Invoice_No;
    /**发票金额 */
    public BigDecimal Invoice_Sum;
    /**投保金额 */
    public BigDecimal Insure_Sum;
    /**出运货币代码*/
    public String Money_Id;
    /**合同支付期限*/
    public int Pay_Term;
    /**合同支付方式*/
    public String Pay_Mode;
    /**缴费支付方式*/
    public String Fee_Pay_Mode;
    /**运输方式*/
    public String Traffic_Code;
    /**出运日期*/
    public Date Transport_Date;
    /**海关10位商品代码*/
    public String Code10;
    /**商品名称*/
    public String Goods_Name;
    /**合同号*/
    public String Contract_No;
    /**提单号*/
    public String Transport_Bill_No;
    /**报关单号*/
    public String Customs_Bill_No;
    /**保户特别说明*/
    public String Shipment_Remark;
    /**是否需要申请融资*/
    public String If_Financing;
    /**业务员名称*/
    public String Employee_Name;
    /**变更原因*/
    public String Alter_Reason;
    /**申请人姓名*/
    public String Applicant_Name;
    /**申请时间*/
    public String Apply_Time;
    /**附件数*/
    public int File_Num;
    /**变更说明*/
    public String Modify_Msg;
    /**状态*/
    public String Status;
    /**备用1*/
    public String Item1;
    /**备用2*/
    public String Item2;
    /**备用3*/
    public String Item3;
    /**备用4*/
    public String Item4;
    /**备用5*/
    public String Item5;
    /**客户ID*/
    public int Customer_Id;
    /**出口组织*/
    public int Export_Org_Id;
    /**保险单号ID*/
    public int Insurance_Policy_Id;
    /**原出运申报明细ID*/
    public int Shipment_Declare_Detail_Id;
    /**组织ID*/
    public int Unit_Id;
    /**角色ID*/
    public int Busi_Role_Id;
    /**版本*/
    public int Version;
    /**创建人*/
    public int Created_By;
    /**创建时间*/
    public Date Creation_Date;
    /**修改人*/
    public int Last_Updated_By;
    /**修改时间*/
    public Date Last_Update_Date;
    /**备用1*/
    public String Attribute1;
    /**备用2*/
    public String Attribute2;
    /**备用3*/
    public String Attribute3;
    /**备用4*/
    public String Attribute4;
    /**备用5*/
    public String Attribute5;
    /**备用6*/
    public String Attribute6;
    /**备用7*/
    public String Attribute7;
    /**备用8*/
    public String Attribute8;
    /**备用9*/
    public String Attribute9;
    /**备用10*/
    public String Attribute10;
    /**备用11*/
    public String Attribute11;'''

    l = pstr.split(sep='\n')
    for i in l:
#         Java2Delphi(i)
        Java2DelphiProperty(i)