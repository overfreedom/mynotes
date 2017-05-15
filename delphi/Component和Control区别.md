Delphi Component与Control的区别
=============

**区别**

  1. Component 包含了界面上的所有组件（包含可视/不可视)
  2. Control 只包含界面上的可视组件。（ 组件如果是可视的也叫做控件） 

可以得出Control其实属于Component的一个部分。实际上TControl是Tcomponent的子类`TControl = class(TComponent)`

`  TComponent(Comp).ComponentCount;` 得到一个**容器组件**包含的所有子组件的数量。`TControl(Comp).ControlCount`方法并没有定义，项目中一般一个控件是直接继承`TWinControl`的。`TWinControl(Comp).ControlCount`可以得到这个控件的子控件数量。

>很多时候会将一个Panel1放在Form1上，然后再将一个Button1放在Panel1上，这样的话，这个Button1的Owner就是Form1而Parent则是Panel1。

>所有的Delphi的Component都有Owner 属性，Owner属性表示这个Component的所有者是谁，比如上面的例子，Button1的所有者（Owner ）就是Form1，当Form1析构时，会先将Button1释放掉。也就是说，Owner会自动地控制Component的生命周期，它负责构件的创建和释放。如在上例中，系统默认Form上所有Component的所有者是Form1。顺便指出，Create方法应带有表示Component的Owner的参数.，如果Owner设置的为Nil值，那这个Component必须创建者编码析构它，Owner属性是只读的，并且在运行期是无法修改它的值。

> 类似，但不同于Owner属性，Parent 属性则表示Component从属于另一个Component，简单的说自身是其他Component的Child Component，例如 TForm,TGroupBox ,TPanel等。Parent是用来控制 在它的客户区范围内的Child Component，Parent决定如何展示包含的Child Component，例如：Left，Top等属性都是相对于Parent的位置。
> 
> Parent属性可以在运行期被修改。并非所有的Component都有Parent，Parent属性可以为Nil值，可以用HasParent 方法返回的Boolean值来判断Component是否拥有Parent。 我们可以设置Parent属性来做一些控制，例如：我们可以在Form1上置Panel1和Panel2，然后再放一个Button1在Panel1上，在Button1的OnClick事件中写上：Button1.Parent := Panel2;  运行这段代码你会发现，开始Button1是在Panel1上，然后按下Button1触发OnClick事件后，Button1‘跳’到了Panel2上。我们要在运行期间创建一个Button的话，就一定要注意指定它的Parent属性，否则Button不会显示出来，因为它必须拥有一个Parent的容器来显示自己。如果你在设计这个Button时察看下属性编辑器，你会看到ParentFont和ParentShowHint等属性，类似于这样的属性设置为True的话，就会使Button的Font以及ShowHint属性按Parent的Font和ShowHint的值来设置，保持一致的风格。比如Parent的Font是红色，那么Button的字体也将是红色。
>
>ControlCount和ComponentCount的区别也就取决于Parent与Owner的区别，还是拿上面的例子解释下Panel1的ControlCount为1而ComponentCount却为0，是因为Button1的Parent属性指向的是Panel1而Owner属性则还是Form1，所以Form1的ComponentCount值是2，包括Panel1和Button1。我们可以利用Controls属性与Components属性去遍历Parent所包含的Child Component和Owner所管理的Child Component。
>

关系图

		Form 窗体
			--->包含 pannel TPageControl ..TButton 等组件 这些组件的owner是Form
		pannel
			--->上放置了多个控件 如TButton TEdit TMemo ..等 这些组件的Parnent是pannel owner还是Form
		这时如果调用
			Form.componentcount   
	 		Form.controlcount
			pannel.controlcount
			这三个方法可以正确得到组件数量
			pannel.componentcount
		得到的是0，因为没有组件的owner是pannel