**CRM JAVA 后台框架概述 （业务类）：**
==========
*	符号定义
	*  \* 抽象类
	*   实体类
	*  × 接口
	* -> 继承类           
	* -->实现接口
	* (-- 个人猜测，未见全部代码 --)
  
例：
>    Crm_Soshipreq_Header  <br>
    ->*BusinessObject   -->×BusinessClass <br>
    ->*BasePathObject   
    ->*BaseObject       -->×BusinessClass

##Crm_Soshipreq_Header  : 
---------------- 
属于业务类，承担着和前台进行通信，进行业务逻辑实现，并通过封装好的工具对数据库进行操作。

命名规则： 数据库表名一致。 
*******************
**重要属性和方法**
    
**1.public 属性；**  
                    命名规则： 和表的字段命名一致 ， 变量采用 每个字母首字母大写，字母间用 _ 连接。 如    Is_Apply_Free，Item_Kind
                    常量用全大写表示。       
                    
#####重要的类属性：
                    
    1)  com.sinocc.util.DataRelation                
        ->com.sinocc.base.util.DataRelation   -->×Serializable                 
    
>这个类属性主要是作为保存前台传入的明细行使用的，其实现了序列化接口，用来实现与前台的通信。类在实例化的时候可以选择传进一个字符串， 字符串会被保存在 属性**relationName** 中， 同时会创建一个Vector列表  保存在 **jm52**；也可以传进一个object，会检测是否为   com.sinocc.base.util.DataRelation 的子类，如果是则提取其中的relationName和列表 Vector 保存。

保存Crm_Soshipreq_Header的明细行Crm_Soshipreq_Line表的数据    
            
                如：public DataRelation Crm_Soshipreq_LineofCrm_Soshipreq_Headers =
                    new DataRelation("crm_soshipreq_lineofcrm_soshipreq_header");
                       
 保存Crm_Soshipreq_Header的数据 
        
        public DataRelation Crm_Soshipreq_Headers = 
                    new DataRelation("crm_soshipreq_header");         
                
                 
**2.重要的方法：**

命名规则： 需要在前台调用的方法以do开头后每个单词首字母大写
                        
        1) public void doSearch() throws SinocpcException   
>这个方法一般是在前台进行搜索时调用，把搜索结果存储在DataRelation中
**（--服务器将结果序列化后成XML后，传递给前台--）**

        2) public void doInsert() throws SinocpcException
>这个方法在前台需要对数据库插入数据时调用，前台会把需要新增的数据**(-- 通过xml传给服务器，服务器还原成Vector（HashSet） --)**传递到后台，再利用封装好的数据库工具插入                            

        3) public void doInsert() throws SinocpcException
>同上差不多

        4) public void doDelete() throws SinocpcException
>同上差不多 用来删除数据
        
        5) public void doSelect() throws SinocpcException                                                        
>这个方法一般用在前台有子表的情况下，通过这个方法查找设置明细行， 
（一般是   \*\*_lineof\*\*) 如 **Crm_Soshipreq_LineofCrm_Soshipreq_Headers**                                               

这5个方法，不需要特别在前台声明（-- 应该是前台默认就有的5个方法，同样doCheck，doConfirm 应该也是一样不需要申明的。 --）
                                                        