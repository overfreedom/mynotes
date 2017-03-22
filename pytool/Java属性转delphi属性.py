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
    pstr='''    /**商业发票ID*/
    public int Ci_Id;
    /**发票编号*/
    public String Invoice_No;
    /**发票金额*/
    public BigDecimal Invoice_Sum;
    /**投保金额*/
    public BigDecimal Insure_Sum;
    /**可损金额*/
    public BigDecimal Pl_Sum;
    /**应付款日*/
    public Date Shouldpay_Date;
    /**信保路由号*/
    public int Corp_Serial_No;
    /**企业标识*/
    public String Client_No;
    /**导入接口标志*/
    public String Import_Edi_Flag;
    /**中信保导入状态*/
    public int Citic_Import_Status;
    /**备注*/
    public String Remarks;
    /**已核销金额*/
    public BigDecimal Applied_Amount;
    /**申报日期*/
    public Date Shipment_Apply_Time;
    /**组织ID*/
    public int Unit_Id;
    /**角色ID*/
    public int Busi_Role_Id;
    /**创建人*/
    public int Created_By;
    /**创建时间*/
    public Date Creation_Date;
    /**修改人*/
    public int Last_Updated_By;
    /**修改时间*/
    public Date Last_Update_Date;
    /**预留字段1*/
    public String Attribute1;
    /**预留字段2*/
    public String Attribute2;
    /**预留字段3*/
    public String Attribute3;
    /**预留字段4*/
    public String Attribute4;
    /**预留字段5*/
    public String Attribute5;
    /**预留字段6*/
    public String Attribute6;
    /**预留字段7*/
    public String Attribute7;
    /**预留字段8*/
    public String Attribute8;
    /**预留字段9*/
    public String Attribute9;
    /**预留字段10*/
    public String Attribute10;
    /**预留字段11*/
    public String Attribute11;
    /**预留字段12*/
    public String Attribute12;
    /**预留字段13*/
    public String Attribute13;
    /**预留字段14*/
    public String Attribute14;
    /**预留字段15*/
    public String Attribute15;
    /**可损通知申请明细ID*/
    public int Plnotice_Req_Detail_Id;
    /**可损通知申请ID*/
    public int Plnotice_Req_Id;
    /**出运申报明细ID*/
    public int Shipment_Declare_Detail_Id;'''

    l = pstr.split(sep='\n')
    for i in l:
#         Java2Delphi(i)
        Java2DelphiProperty(i)