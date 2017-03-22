CRM JAVA 后台框架概述 抽象类：
==========
-----------
*	符号定义
	*  \* 抽象类
	*   实体类
	*  × 接口
	* -> 继承类           
	* -->实现接口
	* (-- 个人猜测，未见全部代码 --)

---------------------------
###类继承结构
	*BusinessObject  -->×BusinessClass
	->*BasePathObject
	->BaseObject	 -->×BusinessClass

------------
###构造方法
		public BusinessObject() {
			//关联系统日志
			getSysLog().setBusinessObject(this);
		}
> 构造方法，关联系统日志 其中日志对象是单例实现，不过这个日志系统已经不用了。保留这个方法只是为了兼容旧代码。

###重要属性
	/** ERP数据库中心 */
	private DataCentre erpDC = null;
	
	/** bmsDC数据库中心 */
	private DataCentre bmsDC = null;
	
	/** zj 资金系统数据库中心 */
	private DataCentre zjDC = null;
	
	/** apsDC数据库中心 */
	private DataCentre apsDC = null;
	
	/** acErp数据库中心 */
	private DataCentre acerpDc = null;
	
	/** eamDc数据库中心 */
	private DataCentre eamDc = null;
	
	/** WLERP数据库中心 */
	private DataCentre wlerpDC = null;
	
	/** GERP数据库中心 */
	private DataCentre gerpDC = null;
>类里保存了所有可以连接的数据库,同时有所有数据库的get，set方法。
 
**例如**

>set方法

	public void setApsDataCentre(DataCentre newDataCentre) {	
		this.apsDC = newDataCentre;
	}
>get方法

	public DataCentre getApsDataCentre() {	
		if (this.apsDC != null) return this.apsDC;	
		if (this.isEntrance()) {	
			//取aps电子仓
			String apsVaultId = null;			 
			if (null == apsVaultId) {	
				// 取系统默认aps电子仓
				for (int i = 0; i < GlobalVariable.Vaults.size(); i++) {	
					Hashtable vaultInfo = (Hashtable) GlobalVariable.Vaults.get(i);
					String type = (String) vaultInfo.get("vaulttype");
					if (type != null && type.equalsIgnoreCase("scm")) {	
						apsVaultId = (String) vaultInfo.get("vaultid");
						break;
					}
				}
			}	
			if (apsVaultId == null)
				GlobalVariable.log.error("No aps vault.");
			else {	
				this.apsDC = new CPCDao(apsVaultId);
				this.getDaoTransaction().add(this.apsDC, "aps");
				this.apsDC.setTransation(this.getDaoTransaction()
						.isUsedTransation(this.apsDC));
			}
		}else if (this.getParent() != null && this.getParent() != this) {	
			//从父对象取
			this.apsDC = ((BusinessObject) getParent()).getApsDataCentre();
		}
		return this.apsDC;
	}
>主要是根据**vaultid**来新建一个CPCDAO实例，然后把它放入**DaoTransation**并设为可用。类有父对象，则直接从父对象取。


	// Excel导出参数
	public String Cloumns = null;
	public String Titles = null;
	public int IsExcel = 1; // 1 查询 2 导出
	// 返回链接
	public String Link_Name;	
	/** 最大查询记录数 */
	public int MaxSearchRltCmt = 0;
	/** 是否是导入文件操作 1-不导入 2-导入(不写日志) */
	public int ImportDataFlag = 1;

>剩下的这几个属性里面，**MaxSearchRltCmt**是最经常使用的一个属性。用来限制数据的查询条数的。当查询条数小于1时，取系统定义的最大查询条数`GlobalVariable.SearchMaxCount`,自定义的查询条数最大不能超过系统的最大查询条×20。`MaxSearchRltCmt = GlobalVariable.SearchMaxCount * 20`

--------------
###重要方法

	public String getTmpTableName() throws DatabaseException

>返回一个字符串为临时表名

 

