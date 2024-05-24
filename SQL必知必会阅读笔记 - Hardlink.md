关系代数与关系演算



可以将关系代数描述为一种( 高级的 ) 过程式语言， 即可用它告诉 DBMS 如何从数据库的一个或多个关系中构建新关系 ； 而将关系演算看成一种非过程式语言 ， 它用公式给出由数据库的一个或多个关系中构建新关系的定义。关系代数和关系演算形式上是相互等价的 。

演算和代数都是形式语言， 对用户不太友好。 它们通常用作其他高级关系数据库数据操作语言( DML )



关系演算用来衡量关系语言的选择能力 。如果一种语言可以生成所有由关系演算推导出来的关系，就称它具有关系完备性



## 关系代数

关系代数是一种纯理论语言， 它定义了一些操作， 运用这些操作可以从一个或多个关系中得到另一个关系，而不改变原关系。 因此它的操作数和操作结果都是关系， 而且一个操作的输出可以作为另一个操作的输入。故而关系代数的一个表达式中可以嵌套另一个表达式， 这种性质称为闭包 ( closure ) : 关系在关系代数下是封闭的 ， 正如数在算数运算下是封闭的一样。



关系代数中有 五个基本运算 ：选择、投影、笛卡尔乘积、集合并、集合差 ， 还有连接 、集合交、除运算等。

![image-20240422204512140](https://s2.loli.net/2024/05/07/A4CWhaz9bZcw76s.png)



### 一元运算



#### 选择

![image-20240422204612602](https://s2.loli.net/2024/05/07/H2QmFX5qvojgBSL.png)



![image-20240422204633382](https://s2.loli.net/2024/05/07/uVIaZ8dxsQGqWw1.png)



#### 投影

![image-20240422204656657](https://s2.loli.net/2024/05/07/nRtsxcOXMhGkLoW.png)





### 二元运算



#### 集合并

![image-20240422204756296](https://s2.loli.net/2024/05/07/l34tZ6vrx7iwG5F.png)

可以先用投影运算使得两个关系具有并相容性。



#### 集合差

![image-20240422204922618](https://s2.loli.net/2024/05/07/udZzlJRrUGLpEgB.png)



#### 集合交

![image-20240422204947217](https://s2.loli.net/2024/05/07/RrD9jH1qw2VvNXM.png)





#### 笛卡尔积

![image-20240422205024961](https://s2.loli.net/2024/05/07/7mOtsD8H9M2pnqy.png)

若一个关系有 I 个元组， N 个属性； 而另一个关系有 J 个元组，M 个属性， 则它们的笛卡尔乘积将会有 ( I * J ) 个元组， ( N + M ) 个属性。



![image-20240422205227421](https://s2.loli.net/2024/05/07/J6XDRVgUdNjwBOM.png)





#### 除法运算

![image-20240423143528067](https://s2.loli.net/2024/05/07/9lULbaEx6vFVi8O.png)

![image-20240423143545483](https://s2.loli.net/2024/05/07/31uz9BaODdcUZjC.png)





### 连接运算

一般用连接运算来代替笛卡尔乘积运算。

连接时由笛卡尔乘积导出的，相当于把连接谓词看做选择条件， 对两个参与运算关系的笛卡尔乘积执行一次选择运算。

**连接运算的多种形式 ：**

- θ连接
- 等接( θ连接 的特例 )
- 自然连接
- 外连接
- 半连接



#### θ连接

![image-20240422205708214](https://s2.loli.net/2024/05/07/7RweE8OHQVsniSr.png)

![image-20240422205719781](https://s2.loli.net/2024/05/07/8tvsKTRjuGaF34J.png)



#### 等接

在谓词 F 仅包含 = 的情况下， θ连接就变成了等接(` Equijoin` )

![image-20240422205840946](https://s2.loli.net/2024/05/07/mpWlfEqihS796t4.png)





#### 自然连接

![image-20240422205940573](https://s2.loli.net/2024/05/07/gOpDXnP7lihxaBG.png)





#### 外连接

连接两个关系时，常会出现一个关系中的某些元组无法在另一个关系中找到匹配元组的情况。 即这些元组在连接属性上不存在匹配值， 但仍希望这些元组出现在结果中。

![image-20240422210114146](https://s2.loli.net/2024/05/07/PpqYKdWv2AxTfUg.png)



![image-20240422210327634](https://s2.loli.net/2024/05/07/DvNtcZ6SVK7wIm4.png)

严格的说， 上图是左( 自然 ) 外连接， 因为它在结果中保留了左边关系的所有元组 。

类似的，右外连接，全外连接( 保留左右两个关系中的所有元组 ， 凡没有找到匹配元组的就在相应的属性中填入空 )



#### 半连接

![image-20240423143242497](https://s2.loli.net/2024/05/07/s6uXLWzt8Fm1oEO.png)

![image-20240423143400232](https://s2.loli.net/2024/05/07/G8CYTOsJNyxiWLU.png)

![image-20240423143420605](https://s2.loli.net/2024/05/07/lrtzhLOK1y4vm9f.png)



### 聚集运算和分组运算

![image-20240423143713254](https://s2.loli.net/2024/05/07/GcVNzpSHMWd7uvQ.png)





## 关系演算

在关系代数表达式中，一般都显式指定一个计值顺序，它隐含着执行查询的策略。在关系演算中， 不描述查询执行策略，即关系演算表达查询只说明要什么，不说明如何得到它 。

在一阶逻辑或谓词演算中， **谓词**是一个带参数的真值函数。如果将参数代入， 这个函数就会变成一个表达式， 称为**命题**， 它非真即假

如果某个谓词包含一个变量，例如 "x是一个员工"， 那么就一定有一个与 x 相关联的 **论域** ，将论域的某些值赋给x时， 命题可能为真， 而对于另一些值， 命题可能为假 。



### 元组关系演算

在元组关系演算中，我们感兴趣的是找出所有使谓词为真的元组。 这种演算是基于**元组变量**的， 元组变量是"定义于" 某个命名关系上的变量， 即该变量的论域仅局限于这个关系中的元组。



![image-20240423145017067](https://s2.loli.net/2024/05/07/uTa9Cq8IHbFeDgt.png)



![image-20240423145224148](https://s2.loli.net/2024/05/07/auh3QlrD7gj8tEn.png)

![image-20240423152232812](https://s2.loli.net/2024/05/07/OrhAPTpwt6kelRY.png)



### 域关系演算

在元组关系演算中， 使用了定义在关系上的元组变量。在域关系演算中， 同样也要用到变量， 但它的论域不再是关系中的元组， 而是属性的域 。

![image-20240423153536915](https://s2.loli.net/2024/05/07/Fkmoa1PYRc7X35u.png)



![image-20240423153557604](https://s2.loli.net/2024/05/07/rtwm3sJaMHZuRdo.png)

![image-20240423153624064](https://s2.loli.net/2024/05/07/4ZMB7wLH1cjW6fl.png)











# 数据库系统概述

数据库系统是由数据库，数据库管理系统(及其应用开发工具)，应用程序，数据库管理员(DBA) 组成的存储、管理、处理和维护数据的系统



**数据库管理系统**

**DataBase Management System( DBMS )**

功能 ：

- 数据定义 ：DDL ( DBMS 提供数据定义语言 Data Definition Language)
- 数据组织、存储和管理
- 数据操纵 ：DML ( Data Manipulation Language )



## 数据模型



### **两类数据模型 **

- 概念模型 ( conceptual model ) ， 也称信息模型， 按用户的观点对数据和信息建模，主要用于数据库设计

  - 常用概念 ：实体 、属性、码 、实体集( entity set , 同一类型实体的集合 )、 
  - 实体间的联系 ：
    - 1 : 1 实体集 A 中的任一实体， 实体集B 中至多一个实体与之联系， 反之依然 。
    - 1 : n  A 中的任一实体， B中有 n 个实体与之联系。 反之，B中的任一实体， A 中至多一个实体与之联系
    - n : m

- 逻辑模型和物理模型

  - 逻辑模型主要包括 ：层次模型( hierarchical model ), 网状模型( network model), 关系模型( relation model), 面向对象数据模型， 对象关系数据模型， 半结构化数据模型 。

    逻辑模型是按计算机系统的观点对数据建模，主要用于数据库管理系统的视线

  - 物理模型 ：对数据最底层的抽象。



#### **数据模型组成三要素**

- **数据结构** ：描述数据库的组成对象以及对象间的联系 ：静态特性
- **数据操作** ：主要有查询和更新(插入、删除、修改) 两大类操作：动态特性
- **完整性约束条件**( integrity constraints )



### 常用逻辑数据模型

层次模型和网络模型统称为**格式化模型** 

在格式化模型中实体用记录表示，实体的实行对应记录的数据项( 或字段 ) 。实体间的联系在格式化模型中转换成记录间的两两联系

![image-20240507150817654](https://s2.loli.net/2024/05/07/jJhPtZcEIMn4Tfo.png)



#### 层次模型 

层次模型用树形结构来表示各类实体以及实体间的联系，现实世界中许多实体间的联系本来就呈现出一种很自然的层次关系，如行政机构、家族关系等。



**层次模型的数据结构**

1. 有且只有一个结点没有双亲结点 ：根结点
2. 根以外的其他结点有且仅有一个双亲结点

层次模型中，每个结点表示一个记录类型，记录类型之间的联系用结点间的连线( 有相边 ) 表示，这种联系是父子之间的一对多联系。这就使得层次数据库系统只能处理一对多的实体联系。

层次模型 ：该层次模型有 4 个记录类型 ，均为一对多联系

![image-20240507153020996](https://s2.loli.net/2024/05/07/W8HCj3UfraPEp25.png)

该数据模型对应的一个值 ：

![image-20240507153313457](https://s2.loli.net/2024/05/07/rV6XhEUxTeYSDuF.png)





**层次模型的数据操纵与完整性约束**

层次模型的数据操纵主要有查询、插入、删除和更新。进行数据操纵时需要满足层次模型的完整性约束条件 ：进行插入操作时，若没有相应的双亲结点值进不能插入它的子女结点 ；删除操作时 ，若删除双亲结点值则相应的子女结点值也将被同时删除。





#### 网状模型

网状数据模型的典型代表是 DBTG 系统，亦称 CODASYL 系统



**网状模型的数据结构**

1. 允许一个以上的结点无双亲
2. 一个结点可以有多于一个的双亲

层次模型实际上是网状模型的一个特例

![image-20240508112713913](https://s2.loli.net/2024/05/08/rdtkLK5y9wblDmF.png)



example：学生选课，学生与课程之间是多对多关系，而 DBTG 模型不能表示记录间多对多的联系，为此引进一个学生选课的连接记录。

学生与选课间的联系是一对多的联系，联系名为 : S-SC , 课程与选课间的联系同理

![image-20240508113114444](https://s2.loli.net/2024/05/08/IRB9bvSPNwrdfX1.png)



#### 关系模型



**关系模型的数据结构**

关系模型与以往的模型不同，它是建立在严格的数学概念的基础上的

从用户观点看，关系模型由一组关系组成。每个关系的数据结构是一张规范化的二维表 。



**术语**

- 关系(relation) : 一个关系对应一张表

- 元组(tuple): 表中的一行

- 属性(attribute): 表中的一列

- 域(domain) : 一组具有相同数据类型的值的集合。属性的取值范围来自某个域

- 关系模式 ：对关系的描述，一般表示为 ：`关系名(属性1，属性2，属性3 ..)`




**关系模型的数据操纵和完整性约束**

关系模型中的数据操作时集合操作，操作对象和结果都是关系 ：即若干元组的集合，而不像格式化模型中那样是单记录的操作方式。







## 关系模型

![image-20240509160106490](https://s2.loli.net/2024/05/09/LhY7xQrafVzgD1A.png)



### 术语

- **关系模式**：用一组属性和域名对定义的具名的关系

  设属性 A1,A2,...An 对应的域分别是 D1,D2,...Dn , 则集合 `{A1:D1, A2:D2,...An:Dn}`就是一个关系模式，由关系模式 S 所定义的关系 R 是一组从属性名到其对应的域的映射 。关系R 就是如下 n 元组的集合 ： `(A1:d1, A2:d2,...An:dn)` d1∈A1 ...  这样就可以将关系模式中的每个关系看做属性对应域的笛卡尔积的子集 。表则是这种关系的简单表示

D1 x D2 x ... x Dn 的子集叫做在域 D1 ， D2 ， ... ， Dn 上的关系，表示为 `R(D1 ，D2 ，... ，Dn )`

n 是关系的目或度 (degree )



- 超关键字(super key) : 唯一标识出关系中的每个元组的属性组

- 候选码/候选关键字(candidate key) : 若关系中的某一属性组的值能唯一标识一个元组，而其子集不能，则称该属性组为 *候选码* ： 唯一性 & 不可约性
- 主码/主关键字(primary key): 若一个关系有多个候选码，则选定其中一个为主码
- 外部关键字/外码( Foreign Key): 当一个关系中的某个属性组 与 另一个关系(或自己) 的候选关键字匹配时 ，就称这个属性组为外部关键字 
- 主属性(prime attribute): 候选码的诸属性
- 非主属性(non-prime attribute) : 不包含在任何候选码中的属性





- 关系可以有三种类型 ：基本关系( 又称为基本表 )、查询表和视图表 

  基本表是实际存在的表：实际存储数据的逻辑表示；查询表是查询结果对应的表；视图表是由基本表或其他视图表导出的表。

- 关系模型要求关系必须是规范化的( normalization ) ,规范化的关系简称为范式( Normal Form, NF )









### ER 图 

**entity relationship diagrams** 实体关系图

摘自 https://drawio-app.com/blog/entity-relationship-diagrams-with-draw-io/

![](https://s2.loli.net/2024/05/07/qhefcp7RUm15uLr.png)



![](https://s2.loli.net/2024/05/07/fDaCOmYNeX5LU3J.png)

#### REDs的三个组成部分



##### 1.属性

**Attributes** : 组成实体的各个数据。 

- In the first style of diagram, they are drawn as circles floating around their entity. 
- In the second style, similar to  they are listed within the rectangle.
  - 主键并带有下划线。外键斜体表示

- 如果不是实际存储属性，而是根据其他属性计算属性，则该属性是派生属性，并且具有虚线轮廓。

![](https://s2.loli.net/2024/05/07/lJDAeN4FYgVQSnW.png)



##### 2.关系

- 可以用菱形表示，也可以在两个实体之间的连接器上写成文本。

- In the first style of diagram, you can see that both User and Coach write comments, and the User can perform a habit Checkin, these two ‘actions’ aren’t represented at all in the second style of diagram, which purely represents the data, not any interactions.

- Relationship connectors use Crow’s foot notation to show how many of each entity is related to another entity. 

  - For example, in the Habit Tracker app – A Coach can have 0 to many Users, but a User can only have 0 or 1 Coach. 

    Users may have many Habits, and each Habit may belong to many users.

- 将鼠标悬停在实体关系库中的每个形状上，以查看其类型。





##### 3.实体

- These represent a collection of data, using a rectangle with attributes ‘hanging’ off it, or box containing a list of its attributes.

- 一个弱实体（显示为双矩形），因为它没有自己的主键——它只存在于它所属的实体中。
- 关联实体（在第二种类型的图中更容易看到）以虚线轮廓和连接器显示——无论在哪里有多对多关系，都需要这种类型的实体。要在第一种图表样式中创建关联实体，请添加实体形状和关系形状，并将这两个形状组合在一起。



#### draw.io 使用技巧

**连接线**

- 滑动连接：绘制关系的连接线时，请确保将鼠标悬停实例上直到轮廓变为蓝色——不要将其连接到其中一个连接点。这样，当您拖动某个实例以腾出空间时，连接线将滑动到正确的位置(自动避免交叉)。
- 如果不希望连接线在实例周边滑动，可以将它们附着到固定连接点（小十字，悬停在形状上时以绿色突出显示）。



**编辑某行**

- 选择属性行，然后按Enter键编辑该行。完成后，按CTRL+Enter退出文本编辑。使用箭头键移动到下一个实体，或按CTRL+Enter（或在MacOS上按CMD+Enter）复制该实体。

   

- **Inserting entities from a text file:** You can insert entities directly from SQL code – click on **Arrange**, then **Insert**, then **Advanced**, then **From Text**. In the dialog, select **Table** from the drop down list. You’ll see example code – paste in your SQL, then click **Insert**.











## 数据库系统的结构











# SQL





## Introduction

Structured Query Language ( 结构化查询语言)  。

SQL语言是面向转换语言的例子， 它将输入关系转换为所需的输出关系。

SQL语言是非过程化语言： 用户只需描述所需信息， 不需要给出获取该信息的具体过程。 即SQL不需要指定数据的访问方法。

**ISO( 国际标准化组织 ) 发布的 SQL 标准包括两个主要部分 ：**

- **数据定义语言**( Data Definition Language , DDL ) , 用于定义数据结构和数据的访问控制( 建立表 和访问机制 )
- **数据操作语言**( Data Manipulation Language, DML ) 用于检索和更新数据。

SQL:1999 出现以前， SQL仅包括数据定义和数据操作命令， 不包括控制流命令， 如 `IF...THEN...ELSE` 、`GO TO ` 、`DO...WHILE	` 

这些命令的实现必须用变成语言或任务控制语言或由用户交互决定。由于缺乏计算完整性  ， 仅能以下两种方式使用SQL ：

1. 终端交互地输入SQL语句
2. 将SQL嵌入过程化语言中







### **注释**

```sql
SELECT 	-- This is a 注释
# This is another 注释，但有些DBMS 不支持

/*
多行注释
*/
```



### BNF

用扩展的巴克斯范式( Backus Naur Form, BNF ) 定义SQL语句 ：

- 大写字母用于保留字
- 小写字母用于表示用户自定义字
- `|` 表示从选项中进行选择 ， 如 `a|b|c`
- 大括号表示所需元素， 如 `{a}`
- 中括号表示可选择元素  如`[a]`
- `...` 表示某一项可选择重复零到多次。

example : `{a|b (,c...)}` 意思是a或b后紧跟着用逗号分开的零个或多个 c



### SQL标量数据类型

| 数据类型 | 声明                                                         | 描述                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 布尔型   | BOOLEAN                                                      |                                                              |
| 字符型   | CHAR, VARCHAR                                                | CHAR : 当字符串定义为定长时，若输入字符串小于该长度，则字符串右边用空格补足所需大小<br>VARCHAR : 定义为变长时，若输入字符串小于最大长度，则只存储输入的哪些字符 |
| 定点数   | `NUMERIC[precision [,scale]],` <br>`DECIMAL[precision [,scale]]`<br>, INTEGER, SMALLINT, BIGINT | 定点数据类型用于定义准确表示的数值。数值包括数字、可选的小数点和可选的正负号，数据类型包括精度(precision) 和小数位数(scale) <br>精度表示数的全部位数<br>小数位数表示小数部分的全部位数<br><br>NUMERIC 和 DECIMAL 用于表示十进制数，默认小数位数为 0 ，默认精度依赖于具体实现 |
| 浮点数   | `FLOAT[precision]` , REAL, DOUBLE PRECISION                  | 浮点数用于定义非精确数字，<br>精度决定了位数的精度           |
| 日期时间 | DATE, <br>`TIME[timePrecision][WITH TIME ZONE]`, `TIMESTAMP[timePrecision][WITH TIME ZONE]` | DATE 用于存储用 YEAR , MONTH , DAY 字段表示的日历日期<br>TIME 用于存储用 HOUR, MINUTE, SECOND 字段表示的时间<br>TIMESTAMP 用于存储日期和时间<br>timePrecision 是一个十进制数，给出秒的精度，TIME默认精度为0(整秒) ，TIMESTAMP默认值为6(微秒) 。<br>关键字 WITH TIME ZONE 决定了字段 TIMEZONE_HOUR ,  TIMEZONE_MINUTE 字段的表示 |
| 间隔型   | INTERVAL                                                     | 间隔数据类型表示一段时间，每个间隔类型由 YEAR, MONTH, DAY, HOUR, MINUTE, SECOND 字段的一个连续子集构成。 <br> 将数据类型分为两类 ：年-月间隔和 天-时间间隔 |
| 大对象型 | CHARACTER LARGE OBJECT, BINARY LARGE OBJECT                  |                                                              |

Numeric 和 Decimal 都保存着精确的数值，不会存在四舍五入的情况。它们之间的区别在于 Decimal 可以保存更大的数值，但占用的存储空间也更多。

Numeric 存储方式为变长的，根据实际存储的数值长度来分配存储空间，因此占用空间较小。而 Decimal 则是固定长度的，所以占用的空间比 Numeric 大。



### 标量运算符

SQL 提供若干预定义的标量运算符与函数



**ISO SQL 标量运算符**

![image-20240517132801777](https://s2.loli.net/2024/05/17/TV5S4q9YWnxpjbR.png)

![image-20240517132818760](https://s2.loli.net/2024/05/17/AmRJhxVMFBjPOlk.png)



#### CASE Expression

The `CASE` expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement).

- once a condition is true, it will stop reading and return the result. 
- If no conditions are true, returns the value in the `ELSE` clause.
- If there is no `ELSE` part and no conditions are true, it returns NULL.



```
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```



```sql
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;
```



### 完整性约束

共有 5 种类型 ：

- 必须有值的数据
- 域约束
- 实体完整性
- 引用完整性
- 一般性约束

这些约束可以用 CREATE 和 ALTER TABLE 语句定义



#### **必须有值的数据**

ISO 标准为 CREATE , ALTER TABLE 语句提供的 NOT NULL 列说明符实现了这种约束。 ISO 默认值为 NULL( NULL允许向列中插入空值 ，NOT NULL 不允许向列中插入控制)



#### **域约束**

每列都有一个域，即合法值的集合 。ISO 标准允许在 CREATE 和 ALTER TABLE 语句中提供两种定义域的方式 ： 

- CHECK 子句 ：允许对列或整个表定义约束

  ```sql
  CHECK(searchCondition)
  
  -- demo
  sex CHAR NOT NULL CHECK(sex IN ('M','F'))
  -- 在一个列约束中，CHECK 子句只能引用已定义列
  ```

  

- `CREATE DOMAIN`  : 更显示的定义域

  ```sql
  CREATE DOMAIN DomainName [AS] dataType
  [DEFAULT defaultOption]
  [DEFAULT (searchCondition)]
  ```

  

  demo

  ```sql
  CREATE DOMAIN SexType AS CHAR
  	DEFAULT 'M'
  	CHECK (VALUE IN('M','F'));
  ```

  定义列sex时， 可用域名 SexType 代替数据类型 CHAR ：`sex SexType NOT NULL`

  

  searchCondition 还能查表 ：

  ```sql
  CREATE DOMAIN BranchNumber AS CHAR(4)
  	CHECK(VALUE IN(SELECT branchNo FROM Branch));
  ```



定义域约束的首选方法是使用 CREATE DOMAIN 语句，从数据库中撤销域约束可用 DROP DOMAIN 语句 ：

```sql
DROP DOMAIN DomainName [RESTRICT | CASCADE]
```

RESTRICT : 若该域正被用于某个现存的表、视图或断言的定义，则撤销失败 。

CASCADE : 任一表中基于该域的列都会自动地变为用该域的基类型定义



##### MySQL CHECK ：

```sql
[CONSTRAINT [symbol]] CHECK (expr) [[NOT] ENFORCED]
```

- The optional *`symbol`* specifies a name for the constraint. If omitted, MySQL generates a name from the table name, a literal `_chk_`, and an ordinal number (1, 2, 3, ...).

- If omitted or specified as `ENFORCED`, the constraint is created and enforced.

  If specified as `NOT ENFORCED`, the constraint is created but not enforced.

  

A `CHECK` constraint is specified as either a table constraint or column constraint:

- A table constraint does not appear within a column definition and can refer to any table column or columns. Forward references are permitted to columns appearing later in the table definition.

- A column constraint appears within a column definition and can refer only to that column.

  

example :

```sql
CREATE TABLE t1
(
  CHECK (c1 <> c2),
  c1 INT CHECK (c1 > 10),
  c2 INT CONSTRAINT c2_positive CHECK (c2 > 0),
  c3 INT CHECK (c3 < 100),
  CONSTRAINT c1_nonzero CHECK (c1 <> 0),
  CHECK (c1 > c3)
);
```









#### 实体完整性

实体完整性：表中每一行的主关键字必须是唯一的非空值。

ISO 标准在 CREATE 和 ALTER TABLE 语句中用 PRIMARY KEY 子句支持实体完整性。

每个表中只能使用一个 PROMARY KEY 子句，但可用关键字 UNIQUE 保证列的唯一性( UNIQUE 子句中出现的每个列必须被声明为 NOT NULL )



#### 引用完整性

`FOREIGN KEY (columnName) REFERENCES tableName`

引用完整性 ：外部关键字必须是父表中已存在的有效的元组

在子表中若试图用 INSERT 和 UPDATE 操作，创建与父表中候选关键字不匹配的外部关键字，SQL会拒绝该操作。

而在父表中若尝试用 UPDATE 和 DELETE 操作更新或删除域子表有匹配行的候选关键字， SQL将根据 FOREIGN KEY 子句中的 ON UPDATE 或 ON DELETE 子句来决定如何执行该操作。

- CASCADE ：删除父表中的行并自动删除子表中匹配的行 / 子表中外部关键字设置为父表中新的候选关键字的值
- SET NULL：删除父表的元组并设置子表的外部关键字为 NULL(仅当外部关键字列未设置为 NOT NULL 时)
- SET DEFAULT ：仅当指定 DEFAULT 时有效
- NO ACITON : 拒绝对父表进行删除操作，ON DELETE 默认设置为 NO ACTION



##### MySQL FOREIGN KEY Constraints

```sql
[CONSTRAINT [symbol]] FOREIGN KEY
    [index_name] (col_name, ...)
    REFERENCES tbl_name (col_name,...)
    [ON DELETE reference_option]
    [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT
```









#### 用户定义完整性

ISO 标准允许用 CREATE 和 ALTER TABLE 中的 CHECK 和 UNIQUE 子句，及 CREATE ASSERTION语句 指定用户定义完整性

```sql
CREATE ASSERTION AssertionName
CHECK (searchCondition)
```

如果一般性约束作用于多个表，则较好的选择是使用一个 ASSERTION 语句

example :定义用户定义完整性，禁止员工同时管理100处以上房产

```sql
CREATE ASSERTION StaffNoHandlingTooMuch
	CHECK(NOT EXISTS(SELECT staffNo	
                    	FROM PropertyForRent
                    	GROUP BY staffNo
                    	HAVING COUNT(*)>100))
```







#### CONSTRAINT 定义

```sql
ALTER TABLE Vendors
ADD CONSTRAINT PROMARY KEY (vend_id);
```

`CONSTRAINT` 语法可用于 `CREATE TABLE` 和 `ALTER TABLE ` 语句

- SQLite 不允许使用 ALTER TABLE 定义键 ， 要求在初始的 CREATE TABLE 语句中定义它们 。











## DML 语句 

SQL DML语句有以下几种 ：

- SELECT : 查询数据库中的数据
- INSERT : 将数据插入表中
- UPDATE : 更新表中数据
- DELETE : 删除表中数据



### SELECT



#### 简单查询

```sql
SELECT [DISTINCT | ALL] {* | [columnExpression [AS newName]] [,...]}
FROM TableName[alias][,...]
[WHERE condition]
[GROUP BY columnList][HAVING condition]
[ORDER BY columnList]
```



**DISTINCT**   

只返回不同值

```sql
SELECT DISTINCT vend_id 
FROM Products
```

**不能部分使用 DISTINCT** 

DISTINCT 关键字作用于所有的列 ，不仅仅是跟在其后的那一列。 例如 `SELECT DISTINCT vend_id, prod_price` 会输出指定两列组合结果不同的所有数据



- **限制结果**

SELECT 语句返回指定表中所有匹配的行，如果只想返回第一行或一定数量的行该怎么办 ？

注意：各种数据库中这一SQL实现并不相同



**SQL Server** ：TOP 关键字限制最多返回多少行

```sql
SELECT TOP 5 prod_name
FROM Products
```



**DB2 ：**

```sql
SELECT prod_name
FROM Products
FETCH FIRST 5 ROWS ONLY;
```



**Oracle:**

```sql
SELECT prod_name
FROM Products
WHERE ROWNUM <=5
```



MySQL 、 MariaDB、SQLite , 需要使用 LIMIT 字句

```sql
SELECT prod_name
FROM Products
LIMIT 5
```

返回不超过5 行数据

*OFFSET 关键字*

```sql
SELECT prod_name
FROM Products
LIMIT 5 OFFSET 5
#返回从第5行起的5行数据
# 注意第一个被检索的行是第0行，不是第一行
```





##### SELECT 子句顺序

| 子句     | 说明                   |
| -------- | ---------------------- |
| FROM     | 从中检索数据的表       |
| WHERE    | 行级过滤               |
| GROUP BY | 将相同属性值的行分成组 |
| HAVING   | 过滤满足条件的组       |
| SELECT   | 指定查询结果中出现的列 |
| ORDER BY | 指定查询结果的顺序     |

SELECT 语句中子句的顺序不能改变， 仅 SELECT 和 FROM 是必须的， 其余子句均可选。

SELECT 操作为封闭的， 即查询表的结果将用另一张表显示。





##### Attention

 **数据未排序** 

- 若未明确排序查询的结果，则返回的数据没有特定的顺序 ( 不一定是数据被添加到表中的顺序  )



**结束SQL语句**

- **多条SQL语句必须以分号结束**
- 多数 DBMS 不需要在单条SQL语句后面加分号



**SQL语句大小写**

- SQL语句不区分大小写，因此 SELECT 和 select 是一样的 。

- SQL **关键字使用大写** ，而对 **列名和 表名使用小写**，使得代码更易于阅读和调试

- 使用**空格**

  - 在处理SQL语句时，其中所有的空格都被忽略 。因此以下三种表示效果相同

  - ```sql
    SELECT prod_name
    FROM Products;
    
    SELECT prod_name FROM Products;
    
    SELECT 
    prod_name
    FROM
    Products;
    ```

    

#### 计算字段

存储在数据库表中的数据一般不是应用程序所需要的格式 。

例如：城市、州、邮政编码存储在不同的列中 ，但邮件标签打印程序需要把它们作为一个有恰当格式的字段检索出来。

**直接从数据库中检索出转换、计算或格式化过的数据，而不是检索出数据，然后再在客户端应用程序中重新格式化。**

- 在SQL语句内可完成的许多转换和格式化工作都可以直接在客户端应用程序内完成。但一般来说，在数据库服务器上完成这些操作比在客户端中完成要快得多。
- 计算字段并不实际存在于数据库表中。计算字段是运行时在 SELECT 语句内创建的。
- 只有数据库知道 SELECT 语句中哪些列是实际的表列，哪些列是计算字段 。从客户端 ( 如应用程序 ) 来看 ，计算字段的数据与其他列的数据返回方式相同



##### 拼接字段

- SELECT 语句中拼接两个列：

  - SQL Server :  `+`
  - DB2 ，Oracle, PostegreSQL , SQLite :   `||`
  - MySQL , MariaDB 必须使用特殊函数

  

```sql
SELECT vend_name + '(' + vend_country + ')'
FROM Vendors
ORDER BY vend_name;
/*
SELECT Concat(vend_name, ' (' , vend_country, ')' )
*/
```

- TRIM() 函数 ：大多数DBMS 支持 

  ```sql
  RTRIM() 
  LTRIM() 
  TRIM()  -- 去掉字符串左右两边的空格
  ```

许多数据库保存**填充为列宽的文本值**，而结果不需要这些空格:

```sql
SELECT RTRIM(vend_name) + ' (' + RTRIM(vend_country) + ')'
FROM Vendors
ORDER BY vend_name;
```







![image-20240310224539355](https://s2.loli.net/2024/05/07/Z4BkgCUbEDPhsr6.png)

##### 使用别名

一个未命名的列不能用于客户端应用中，因为客户端没有办法应用它。

SQL 支持列 **别名 ( alias )** ,任何客户端都可以按名称应用这个列，就像它是一个实际的表列一样。

**AS 关键字赋予别名**

```sql
SELECT RTRIM(vend_name) + ' (' + RTRIM(vend_country) + ')'
AS vend_title
FROM Vendors
ORDER BY vend_name;
```

![image-20240310224607021](https://s2.loli.net/2024/05/07/aj1DJc7o64LWg5h.png)







##### 算数计算

Orders 表包含收到的所有订单 ，OrderItems 表包含每个·订单的各项物品。

```sql
SELECT prod_id,
	   quantity,
	   item_price,
	   quantity*item_price AS expanded_price
FROM OrderItems
WHERE order_num = 20008;   
```





#### WHERE 子句



 **WHERE 子句** 指定**过滤条件( filter condition)**

五个基本的条件运算( ISO 术语中的谓词 ) ：

- 比较( comparison ) 

  ```sql
  <> 	!=  	# 不等于
  =	< 	<=
  !<	>= # 不小于
  #冗余。 并非所有DBMS 支持这些操作符。
  ```

- 范围( range ) 

- 成员关系( set membership ) : 测试表达式的值是否在某一值集合内

- 模式匹配( pattern match) : 测试字符串是否与指定模式相匹配

- 空( null )  `IS NULL`





##### 操作符



**AND **

**每个条件间都要使用 AND 关键字。**

`WHERE predicate1 AND predicate2 AND predicate3`



**between**

`BETWEEN value1 AND value2 `

BETWEEN 匹配范围中的所有值，包括指定的开始值和结束值。BETWEEN 只是简化了范围运算条件的表达



**OR **

许多 DBMS 在 OR WHERE 子句的第一个条件满足时就不再计算第二个条件了

- **AND 优先级高于 OR **, NOT 优先级高于 AND 和  OR

```sql
SELECT prod_name, prod_price
FROM Products
WHERE vend_id = 'DLL01' OR vend_id = 'BRS01' AND prod_price >= 10;

-- vs

WHERE vend_id = ('DLL01' OR vend_id = 'BRS01') AND prod_price >= 10;
```



**IN **

指定条件范围 `WHERE column_name IN (value1, value2, value3)`

- ```sql
  SELECT prod_name, prod_price 
  FROM Products
  WHERE vend_id IN('DLL01','BRS01')
  ORDER BY prod_name;
  ```

- IN 操作符实际上完成了与 OR 相同的功能

- IN 操作符的优点：

  - 在有多个选项时， IN 操作符更清楚直观IN 操作符一般比一组 OR 操作符执行地更快
  - **IN 最大优点是可用于子查询** 



**NOT **

`WHERE NOT predicate`

- ```sql
  SELECT prod_name
  FROM Products
  WHERE NOT vend_id = 'DLL01' -- WHERE vend_id <> 'DLL01'
  ORDER BY prod_name;
  ```

- MariaDB 支持使用 NOT 否定 IN , BETWEEN, EXISTS 子句，大多数DBMS 允许使用 NOT 否定任何条件





##### 通配符

创建**匹配特定数据的搜索模式**。

- *搜索模式( search pattern )* ：由字面值、通配符组成构成的搜索条件

- *通配符( wildcard)*：用来匹配值的一部分的特殊字符

  - 为在搜索子句中使用通配符，必须使用 **LIKE 操作符**。 

    **LIKE （谓词）** 指示 DBMS 后跟的搜索模式利用通配符匹配而不是简单的相等匹配进行比较。

  - 通配符搜索只能用于*文本字段*，非文本数据类型字段不能使用通配符进行搜索。

  - SQL有两种模式匹配符号 ：`%` 和 `_`, 若查找的字符串本身包含上述模式匹配符， 则可用 转义字符 ：如匹配 '15%', 用谓词 ： `LIKE '15#%' ESCAPE '#' ` , 

    注意一些RDBMS, 使用 `*` 和` ?` 替代 `% `和`_ `

- 通配符检索一般比前面讨论的其他检索更耗时。因此若其他操作符能达到相同目的，应该使用其他操作符



**% 任何字符出现任意次数 （tips: 可以是 0个）**

```sql
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE 'Fish%';

WHERE prod_name LIKE '%bean bag%'；

-- 'Fish%' 将检索以 Fish开头的词. % 告诉DBMS接收 Fish 之后的任意字符，不管它有多少字符。
```

- **NULL** : ` WHERE prod_name LIKE '%'` 不会匹配产品名称为NULL 的行。
- 空格：有些 DBMS 通过空格来填补字段中的内容。例如，若某列有50 个字符，而存储的文本为 Fish bean bag toy (17 个) 则为填满该列需要在文本后附加 33 空格，可能对匹配造成影响: WHERE prod_name LIKE 'F%y' 若值后面跟空格则不是以y结尾。解决方法：**给搜索模式再增加一个 % 号或用函数去掉空格** `WHERE RTRIM(prod_name) LIKE 'F%y'`





**`_` 匹配单个字符**

```sql
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '__ inch teddy bear';

-- 注意 '8 inch teddy bear' 将不会被匹配，因为搜索模式要求匹配两个通配符而不是一个
```





**`[]` 指定一个字符集** ，

它匹配 通配符位置的一个字符。

- 与前面描述的通配符不一样，并不是所有 DBMS 都支持用来创建集合的[]。

  -  SQL Server 支持集合，但是 MySQL，Oracle，DB2，SQLite都不支持。

- 找出所有名字 以 J 或 M 开头的人

  - ```sql
    SELECT 	cust_contact
    FROM Customers
    WHERE cust_contact LIKE '[JM]%'
    ORDER BY cust_contact;
    ```

- [] 可用 前缀字符 ^ 来否定

  - ```sql
    WHERE cust_contact LIKE '[^JM]%'
    -- 匹配以 J 和 M之外任意字符开头的联系人名
    -- WHERE cust_contact NOT LIKE '[JM]%'
    ```







#### ORDER BY 子句

排序：如果不排序，数据一般将以它在表中出现的顺序显示，这有可能是数据最初添加到表中的顺序。但若数据随后进行过更新或删除，那么该顺序将会收到DBMS 重用回收存储空间的方式的影响 



```sql
SELECT prod_name
FROM Products
ORDER BY prod_name ;
# 对 prod_name 列以字母顺序排序数据
```



**按多个列排序**

例如，需要显示雇员名单，可能希望按姓和名排序 ( 首先按姓排序 ，然后在每个姓中再按名排序 )

- 仅在 prod_price 相同时才对 products按 prod_name 排序

```sql
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price, prod_name;
```



**按列位置排序**

```sql
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY 2, 3;

# ORDER BY 2表示按SELECT 中的第二个列 prod_price 进行排序 
```



**指定排序方向**

默认升序( ASC ) 。为使用降序排序，必须指定 **DESC** 关键字 ( **DESCENDING** )

- DESC 只应用到**直接位于其前面的列名** 。

  因此若想在多个列上进行降序排序，必须对每一列指定 `DESC` 关键字。

  ```sql
  SELECT prod_id, prod_price, prod_name
  FROM Products
  ORDER BY prod_price DESC, prod_name DESC;
  ```

  



#### 聚集函数

*当需要汇总出表中的数据，而不需要查出数据本身时 , 返回实际表数据浪费时间和处理资源 。 这些函数很高效，它们返回结果一般比你在自己的客户端应用程序中计算要快得多*

这些函数只对表中的单个列进行操作， 返回一个值 。

- ISO 标准定义了五个聚集函数 ：

  **COUNT, MIN, MAX 可以用于数值和非数值字段， 而 SUM 和 AVG 只能用于数值字段 。**

  

  除了 COUNT(*) 外， 每个函数首先要去掉空值， 然后计算其非空值 。`COUNT(*)` 是COUNT 的特殊用法， 计算表中所有行的数目， 而不管是否有空值或重复出现

  
  
  - `COUNT(column) [WHERE ..]` : 返回指定列中数据的个数
  
    -  **COUNT(*)**  : 对表中行数目进行计数，不管表列中的是NULL 还是非空值
    -  **COUNT(column**) :  对column列中非 NULL行进行计数
  
    ```sql
    SELECT COUNT(*) AS num_cust
    FROM Customers;
    
    SELECT COUNT(cust_email) AS num_cust
    FROM Customers;
    ```

    **ATTENTION** : 注意区分`COUNT() ` 和 `SUM() ` 的区别 ，`COUNT() ` 是统计表中行的数目， 而 SUM() 是求特定函数值的和 。

    
  
  - `SUM(column)` ：返回指定列中数据的总和
  
    
  
  - `AVG(column)` ：返回指定列中数据的平均值
  
    ```sql
    SELECT AVG(prod_price) AS avg_price
    FROM Products
    WHERE vend_id = 'DLL01';
    -- 该SELECT 语句包含 WHERE 子句，此WHERE 子句仅过滤出 vend_id 为DLL01 的产品，因此 avg_price 中返回的值仅是该供应商产品的平均值。
    ```
  
    
  
  - `MIN(column)` ：返回指定列中数据最小值
  
  - `MAX(column)`：返回指定列中数据最小值
  
    对非数值数据使用 MAX() : 许多DBMS 允许将它用来返回任意列中的最大值，包括数值、日期、文本数据( 返回该列排序后的最后一行)



- DISTINCT

  - 若需要在应用函数之前消除重复， 则必须在函数中的列名前使用关键字 DISTINCT

    DISTINCT 必须使用列名，不能用于计算或表达式

  `SELECT SUM(DISTINCT quantity)` 

  - 若对所有行执行计算，指定 ALL 参数 或不指定参数( ALL 是默认行为 )



- 注意聚集函数只能用于 SELECT 列表和 HAVING 子句中， 用在其它地方都是不正确的。

  若 SELECT 列表包括聚集函数， 却没有使用 GROUP BY 子句分组， 那么 SELECT 列表的任何项都不能引用列， 除了作为聚集函数的参数 。

  example ：`SELECT staffNo, COUNT(salary) FROM Staff;` 是非法的。



#### 合并结果集 UNION, INTERSECT, EXCEPT

SQL 中，可用标准的并、交、差集合操作将多个查询结果表合并为一个查询结果表

![image-20240509193856124](https://s2.loli.net/2024/05/09/8yNp2ALTi5ujmRv.png)

**ISO 标准的3个集合运算符分别是 ：UNION, INTERSECT( 交 ), EXCEPT(差)** 

集合操作子句格式 ：`operator [ALL][CORRESPONDING [BY {column1[,...]}]]`    

注意 ：`[]` 表示可选内容，`{}` 表示必选内容

- 若指定 CORRESPONDING BY, 则集合操作就在给定的列上执行
- 若指定 CORRESPONDING 而没有 BY 子句，则集合操作就在两表共同的列上执行
- 若指定 ALL, 则查询包括一切重复的行( 默认去重 )



- **不一致的列名**
  如果运算使用的SELECT 语句遇到不同的列名，返回第一个名字。
  - 这种行为带来一个副作用：由于只使用第一个名字，那么想要排序也只能用这个名字。

- 对组合查询结果排序

  只能使用一条ORDER BY 子句，位于最后一条SELECT 语句之后。不允许使用多条ORDER BY 子句。

  

##### UNION

```sql
(SELECT city
FROM Branch
WHERE city IS NOT NULL)
UNION
(SELECT city 
FROM PropertyForRent
WHERE city IS NOT NULL)

-- or

(SELECT *
FROM Branch
WHERE city IS NOT NULL)
UNION CORRESPONDING BY city
(SELECT *
FROM PropertyForRent
WHERE city IS NOT NULL)
```



```sql
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL','IN','MI')
UNION
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4ALL'
ORDER BY cust_name, cust_contact;
```



##### INTERSECT

```sql
(SELECT city
FROM Branch)
INTERSECT
(SELECT city
FROM PropertyForRent);

-- or
(SELECT *
FROM Branch)
INTERSECT CORRESPONDING BY city
(SELECT *
FROM PropertyForRent);
```

可以不用 INTERSECT 运算符重写该查询 ：

```sql
SELECT DISTINCT b.city
FROM Branch b, PropertyForRent p
WHERE b.city = p.city

-- or
SELECT DISTINCT city
FROM Branch b
WHERE EXISTS(SELECT *
            FROM PropertyForRent p
            WHERE b.city = p.city)
```

可用各种等价的形式书写查询是SQL语言的一大缺陷



##### EXCEPT

```sql
(SELECT city
FROM Branch)
EXCEPT
(SELECT city
FROM PropertyForRent);

-- or
(SELECT *
FROM Branch)
EXCEPT CORRESPONDING BY city
(SELECT *
FROM PropertyForRent);
```







#### 分组查询



##### GROUP BY

**使用分组可以将数据分为多个逻辑组，对每个组进行聚集计算**

ISO 标准要求 SELECT 子句和 GROUP BY 子句紧密结合。 

SELECT 子句仅可包含以下内容 ：

- 列名
- 聚集函数
- 常量
- 组合上述各项的表达式

SELECT 子句中的所有列除非用在聚集函数中， 否则必须在 GROUP BY 子句中出现。 反之， GROUP BY 子句中出现的列不一定出现在 SELECT 列表中。

当 WHERE 子句和 GROUP BY 子句同时使用时， 必须首先使用 WHERE 子句， 分组由满足 WHERE 子句查询条件的那些行产生。

- ISO 标准规定应用 GROUP BY 子句时， 两个空值被认为是相等的。

- 可以对分组进行嵌套

- 大多数SQL实现不允许 GROUP BY 列带有长度可变的数据类型 ( 如文本或备注型字段 )。

- 如果在SELECT 中使用表达式，则必须在 GROUP BY 子句中指定相同的表达式，不能使用别名

  

  



##### 分组约束 ： HAVING 子句

除了能用 GROUP BY 分组数据外 ，SQL 还允许**过滤**分组。

例如，你可能想要列出至少有两个订单的所有顾客。为此必须基于完整的分组而不是个别的行进行过滤 。

此例中 WHERE 不能完成任务 ，因为WHERE 过滤的是行而不是分组

-  *WHERE 在数据分组前进行过滤， HAVING 在数据分组后进行过滤。*

ISO 标准要求 HAVING 子句使用的列名必须出现在 GROUP BY 子句列表中， 或包括在聚集函数中。实际上，HAVING 子句的条件运算至少包括一个聚集函数，否则可把查询条件移到 WHERE 子句中来过滤单个行( 聚集函数不能用在WHERE 子句中 )

```sql
SELECT cust_id, COUNT(*) AS orders
FROM Orders
GROUP BY cust_id
HAVING COUNT(*) >=2;

# HAVING 子句过滤 COUNT(*) >= 2 的分组，WHERE 子句在此处无用，因为过滤是基于分组聚集值，而不是特定的行。
```



```sql
# 同时使用 WHERE和 HAVING 子句：
SELECT vend_id, COUNT(*) AS num_prods
FROM Products
WHERE prod_price >= 4
GROUP BY vend_id
HAVING COUNT(*) >= 2;
```



GROUP BY vs ORDER BY 



|              ORDER BY              |                        GROUP BY                         |
| :--------------------------------: | :-----------------------------------------------------: |
|          对任意的输出排序          |           对行分组，但输出可能不是分组的顺序            |
| 任意列都可以使用 ( 包括非选择的列) | 只能使用选择列或表达式列 ，且必须使用每个选择列或表达式 |

```sql
SELECT order_num, COUNT(*) AS items
FROM OrderItems
GROUP BY order_num
HAVING COUNT(*) >= 3
ORDER BY items, order_num;

# 检索包含三个或更多物品的order_num和items，并按 items 排序，需要添加 ORDER BY 子句 。
```

- GROUP BY 子句按 order_num 分组数据，以便 COUNT(*) 函数能够返回每个订单的物品数目 。
- HAVING 子句过滤数据，使得只返回包含 >=3 个物品的订单
- 最后用 ORDER_BY 子句排序输出



##### 挑战题

![image-20240314185845520](https://s2.loli.net/2024/05/07/yNdI9CTiQrEOF47.png)

```sql
# 1.
SELECT order_num ,COUNT(*) AS order_lines
FROM OrderItems
GROUP BY order_num
ORDER BY order_lines;

# 2.
SELECT MIN(prod_price) AS cheapest_item
FROM Products
GROUP BY vend_id
ORDER BY cheapest_item;

# 3.
SELECT order_num
FROM OrderItems
GROUP BY order_num
HAVING COUNT(*) >= 100;

# 4.
SELECT item_price*quantity AS total_price, order_num
FROM OrderItems
GROUP BY order_num,item_price*quantity
HAVING SUM(item_price*quantity) >= 1000;
```







#### 子查询

 **子查询** ( 或嵌套查询 **subquery** ) ：内部SELECT语句( 子查询 ) 的结果用在外部语句中用以决定最后的查询结果

子查询可以被使用在外部 SELECT 语句的 WHERE 和 HAVING 子句中，子查询也可出现在 INSERT, UPDATE, DELETE 语句中

可以认为 子查询产生一个临时表，便于外部语句访问和利用。在 WHERE 子句和 HAVING 子句中，子查询可以紧邻着关系运算符 ( =, <, > , <=, >=, <>)

**子查询有 3 种类型 ：**

- **标量子查询**返回单个列和单个行，即单个值。原则上，标量子查询可用于任何需要单个值的地方
- **行子查询**返回多个列，但只有单个行。行子查询可用于任何需要行值构造器的时候，如在谓词中
- **表子查询**返回多个行，每行有一个或多个列。表子查询用于需要一个表的情况，例如，作为谓词 IN 的操作数



**子查询需遵循的规则**

1. 子查询 SELECT 列表必须由单个列名或表达式组成，除非子查询使用了关键词 EXISTS
2. 当子查询时比较表达式中的一个操作数时，子查询必须出现在表达式右边





##### **相等判断的子查询**

```sql
SELECT staffNo, fName, lName, position
FROM Staff
WHERE branchNo = (SELECT branchNo
                 	FROM Branch
                 	WHERE street = '163 Main St')
# 若只有一个分公司编号，就是标量查询
```



##### 聚集函数的子查询



**example 1 ：**

```sql
SELECT COUNT(*) AS orders
FROM Orders
WHERE cust_id = 100000001;
```

要对每个顾客执行 COUNT(*) , 应该将它作为一个子查询：

```sql
SELECT cust_name,
	   cust_state,
	   (SELECT COUNT(*)
        FROM Orders
        WHERE Orders.cust_id = Customers.cust_id) AS orders
FROM Customers
ORDER BY cust_name;
```



**example 2**  ：

```sql
SELECT staffNo, fName, lName, position,
	salary - (SELECT AVG(salary) FROM Staff) AS salDiff
FROM Staff
WHERE salary > (SELECT AVG(salary) FROM Staff) ;

-- 列出个人工资高于平均工资的所有员工，并求出多于平均数的值
--  注意不能写 WHERE salary > AVG (salary) : 聚集函数不能用于 WHERE 子句。应先用子查询求出 AVG (salary) (标量子查询)
```





##### 嵌套子查询 ：IN的使用 

 如需要列出订购物品 RGAN01 的所有顾客，怎样检索？

1. 检索包含物品 GRAN01 的所有订单的编号。
2. 检索具有前一步骤列出的订单编号所有顾客的ID
3. 检索前一步骤返回的所有顾客ID 的顾客信息

上述每个步骤都可以单独作为一个查询来执行。可以把一条 SELECT 语句返回的结果用于另一条SELECT 语句的 WHERE 子句。

也可以使用子查询来把3个查询组合成一条语句。

```sql
SELECT order_num
FROM OrderItems
WHERE prod_id = 'GRAN01';
"""
output :
order_num
--------
20007
20008
"""

-- next 
SELECT cust_id
FROM Orders
WHERE order_num IN (20007, 20008);
```



结合这两个查询，将查询订单号的查询变为子查询

```sql
SELECT cust_id
FROM Orders
WHERE order_num IN (SELECT order_num 		   
                    FROM OrderItems 					   
                    WHERE prod_id = 'RGAN01');
                    
                    
SELECT cust_name, cust_contact
FROM Customers
WHERE cust_id IN (SELECT cust_id
                  FROM Orders
                  WHERE order_num IN (SELECT order_num 
                                      FROM OrderItems
                                      WHERE prod_id = 'RGAN01'));
```





##### ANY 和 ALL

关键字 ANY 和 ALL 用于产生单个列的子查询。

- ALL ：仅当子查询产生的所有值都满足条件时，条件才为真
- ANY ：子查询产生的任何一个值满足条件时，条件就为真。ISO标准允许用 限定词 SOME 代替 ANY
- 若子查询为空值，ALL 条件返回真值，ANY 条件返回假值。



##### `EXISTS` 和 `NOT EXISTS`

`EXISTS` 和 `NOT EXISTS`仅用于子查询中，返回结果为真 / 假 。 EXISTS 为真当且仅当子查询返回的结果表至少存在一行 ，为空时则为假。



example : 找出在伦敦分公司工作的所有员工

```sql
SELECT staffNo, fName, lName
FROM Staff s
WHERE EXISTS (SELECT *
              	FROM Branch b
              	WHERE s.branchNo = b.branchNo AND city = 'London') ;
              	
-- 用连接重写 ：
SELECT staffNo, fName, lName
FROM Staff s, Branch b
WHERE s.branchNo = b.branchNo AND b.city = 'London'
```









##### 挑战题

![image-20240315183036922](https://s2.loli.net/2024/05/07/mUI1VNSr4ePJwqY.png)

```sql
# 1.
SELECT cust_id
FROM Orders
WHERE order_num IN (SELECT order_num
					FROM orderItems
					WHERE prod_price >= 10);


# 2.
SELECT cust_id, order_date
FROM Orders
WHERE order_num IN (SELECT order_num
					FROM OrderItems
					WHERE prod_id = 'BR01')
ORDER BY order_date;


# 3.
SELECT cust_email 
FROM Customers
WHERE cust_id IN (SELECT cust_id 
				  FROM Customers 
				  WHERE cust_id IN (SELECT cust_id 
									FROM OrderItems
									WHERE prod_id = 'BR01'));
									
									
# 4.
SELECT cust_id, ( SELECT SUM(item_price*quantity)
				 FROM OrderItems
				 WHERE OrderItems.order_num = Orders.order_num
				 ) AS total_ordered
FROM Orders
GROUP BY cust_id
ORDER BY total_ordered DESC; -- bug: 若一个用户有多个订单怎么办？

# 5.
SELECT prod_name, (SELECT SUM(quantity)
				   FROM OrderItems
				   WHERE Products.prod_id = OrderItems.prod_id) AS quant_sold
FROM Products;
```



##### Problem Record

![image-20240321185426136](https://s2.loli.net/2024/05/07/l9fYIFJCgQcMa3T.png)

报错原因 ：一个 cust_id 可能对应多个 order_num , 因此报错 ：子查询返回的值不止一个 。

改正：

![image-20240321185849326](https://s2.loli.net/2024/05/07/sBYapxcCqAbNnEi.png)

或许此例的最佳表达是 联结 而不是子查询。





```sql
# 返回顾客名称和订单号，添加第三列 OrderTotal，其中包含每个订单的总价

 -- 子查询版本
 SELECT	(SELECT cust_name
				FROM Customers
				WHERE Orders.cust_id = Customers.cust_id) AS cust_name,
				order_num, 
				(SELECT SUM(item_price*quantity)
				FROM OrderItems
				WHERE OrderItems.order_num = Orders.order_num
				GROUP BY order_num) AS orderTotal
FROM Orders;
```



#### 多表查询

SQL 连接操作通过配对相关行(这两行在两个表的匹配列上具有相同值)来合并两个表中的信息。

- WHERE 子句指明连接列
- FROM 子句列出多个表名，可用别名替代表名，用空格隔开



##### 简单连接

最普通的多表查询包括**一对多( 1:n )(或父/子) 联系的两个表** (主关键字所在的表是父表，外部关键字所在的表是子表 )

```sql
SELECT Customers.cust_id,
		COUNT(Orders.order_num) AS num_ord
FROM Customers
INNER JOIN Orders ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_id
```

注意执行顺序 

- FROM 子句获取表数据
- INNER JOIN 子句将 Customers 和 Orders 表相互关联
- GROUP BY 分组数据
- 聚集函数 `COUNT(Orders.order_num) `计算每个顾客的订单数
- 作为 `num_ord `返回 



- SQL标准提供了以下可选择的方式来指定连接 ：
  - `FROM Client c JOIN Viewing v ON c.clientNo = v.clientNo`
  - `FROM Client JOIN Viewing USING clientNo`
  - `FROM Client NATURAL JOIN Viewing`



- 多表连接 ：AND 分隔

  ```sql
  SELECT b.branchNo, b.city, s.staffNo, fName, lName, propertyNo
  FROM Branch b, Staff s, PropertyForRent p
  WHERE b.branchNo = s.branchNo AND s.staffNo = p.staffNo
  
  
  -- 可选表示法 ：
  FROM (Branch b JOIN Staff s USING branchNo) AS bs
  	JOIN PropertyForRent p USING staffNo
  	
  -- INNER JOIN 嵌套 
  -- FROM table1 
  -- INNER JOIN (table2 INNER JOIN (table3 INNER JOIN table4 on..) on..)on ..
  
  SELECT cust_email
  FROM Customers
  INNER JOIN ( Orders INNER JOIN OrderItems 
  				ON OrderItems.order_num = Orders.order_num) 
  	ON Orders.cust_id = Customers.cust_id;
  ```



上面使用的联结称为 **等值连接( equijoin ) ，也称为 内连接 ( inner join )**, 它基于两个表之间的相等测试 。

- **ANSI SQL 规范首选 INNER JOIN 语法**

```sql
SELECT vend_name, prod_name, prod_price
FROM Vendors
INNER JOIN Products ON Vendors.vend_id = Products.vend_id;
```





##### outer-join

内连接：找在匹配列上具有相同值的行，若表中某一行不匹配另一表的任何行，则该行从结果表中删除 。

外连接：保留不满足条件的行，包括左外连接，右外连接和全外连接 。



example

```sql
SELECT Customers.cust_id, Orders.order_num
FROM Customers
LEFT OUTER JOIN Orders ON Customers.cust_id = Orders.cust_id
-- LEFT or RIGHT or FULL JOIN 
```





##### self-join

example :

假如要给与Jim Jones 同一公司的所有顾客发送一封信件。这个查询要求
首先找出Jim Jones 工作的公司，然后找出在该公司工作的顾客。

version 1 :

```sql
SELECT cust_id, cust_name, cust_contact
FROM Customers
WHERE cust_name = (SELECT cust_name
                  FROM Customers
                  WHERE cust_contact = 'Jim Jones')
```



version 2 :

```sql
SELECT c1.cust_id, c1.cust_name, c1.cust_contact
FROM Customers AS c1, Customers AS c2
WHERE c1.cust_name = c2.cust_name
AND c2.cust_contact = 'Jim Jones'
```

此查询中需要的两个表实际上是相同的表，因此Customers 表在FROM
子句中出现了两次。虽然这是完全合法的，但对Customers 的引用具有
歧义性，因为DBMS 不知道你引用的是哪个Customers 表。
解决此问题，需要使用表别名。Customers 第一次出现用了别名c1，第
二次出现用了别名c2。

需要表前缀来明确给出所需列的全名
WHERE 首先联结两个表，然后按第二个表中的cust_contact 过滤数据，返回所需的数据。



**Tips : 用自l连接而不用子查询**

自联结通常作为外部语句，用来代替从相同表中检索数据的子查询语句 。虽然最终结果相同，但许多DBMS 处理联结远比处理子查询快得多。







##### 连接运算的计算过程



- **笛卡尔积** CARTESIAN PRODUCT

  由没有联结条件的表 返回的结果为笛卡尔积 

没有 WHERE 子句，表一的每一行与表二的每一行配对，而不管它们逻辑上是否能配在一起

ISO 标准为笛卡尔乘积提供了特殊的 SELECT 语句格式 ：

```sql
SELECT [DISTINCT|ALL] {* | columnList}
FROM TableName1 CROSS JOIN TableName2
```























**回顾**

```sql
SELECT cust_name, cust_contact
FROM Customers
WHERE cust_id IN (SELECT cust_id
                  FROM Orders
                  WHERE order_num IN (SELECT order_num FROM OrderItems WHERE prod_id = 'RGAN01'))
```

子查询并不总是执行复杂 SELECT 操作的最有效方法，下面是使用联结的相同查询：

```sel
SELECT cust_name, cust_contact
FROM Customers, Orders, OrderItems
WHERE Customers.cust_id = Orders.cust_id
AND OrderItems.order_num = Orders.order_num
AND prod_id = 'RGAN01'

```

使用两个联结来连接表 ，这里有三个 WHERE 子句条件，前两个关联联结中的表，后一个过滤产品 RGAN01 



##### 挑战题

![image-20240321130325069](https://s2.loli.net/2024/05/07/7eorYwkC1M6EAjs.png)

![image-20240321130340805](https://s2.loli.net/2024/05/07/pKuhONvoAlkmxXq.png)

```sql
# 1.
SELECT cust_name, order_num
FROM Customers, Orders
WHERE Customers.cust_id = Orders.cust_id
ORDER BY cust_name, order_num;

-- INNER JOIN syntax
SELECT cust_name, order_num
FROM Customers
INNER JOIN Orders ON Orders.cust_id = Customers.cust_id
ORDER BY cust_name, order_num;

# 2.
SELECT cust_name, Orders.order_num, SUM(item_price*quantity) AS OrderTotal
FROM Customers,Orders,OrderItems
WHERE OrderItems.order_num = Orders.order_num
AND Orders.cust_id = Customers.cust_id
GROUP BY Orders.order_num, cust_name
ORDER BY cust_name, order_num;
 -- 注意 联结仅仅是建立映射关系，但 SUM() 聚集函数需要分组后的数据，因此分组还是需要 GROUP BY 子句， 同时所有非聚集函数的列都要 GROUP BY
 
 -- 子查询版本
 SELECT	(SELECT cust_name
				FROM Customers
				WHERE Orders.cust_id = Customers.cust_id) AS cust_name,
				order_num, 
				(SELECT SUM(item_price*quantity)
				FROM OrderItems
				WHERE OrderItems.order_num = Orders.order_num
				GROUP BY order_num) AS orderTotal
FROM Orders;


# 3.
SELECT order_date
FROM OrderItems, Orders
WHERE Orders.order_num = OrderItems.order_num
		AND prod_id = 'BR01'
		
		
# 4.
SELECT cust_email
FROM Customers
INNER JOIN ( Orders INNER JOIN OrderItems 
				ON OrderItems.order_num = Orders.order_num) 
				ON Orders.cust_id = Customers.cust_id
	
WHERE prod_id = 'BR01';


# 5.
SELECT cust_name , SUM(quantity*item_price) AS TotalOrder
FROM Customers, OrderItems, Orders
WHERE 
Customers.cust_id = Orders.cust_id
AND OrderItems.order_num = Orders.order_num
GROUP BY OrderItems.order_num,cust_name
HAVING SUM(quantity*item_price) >= 1000
ORDER BY cust_name;

SELECT cust_name , SUM(quantity*item_price) AS totalOrder
FROM Orders
INNER JOIN Customers ON Orders.cust_id = Customers.cust_id
INNER JOIN OrderItems ON Orders.order_num = OrderItems.order_num
GROUP BY Orders.order_num ,cust_name
HAVING SUM(quantity*item_price) >= 1000
ORDER BY cust_name;

```





### 数据更新

修改数据库内容的三种SQL语句 ：INSERT ,UPDATE ,DELETE 



#### INSERT

两种 INSERT 语句 



##### `INSERT ... VALUES`

- 插入一个行 ：

  ```
  INSERT INTO TableName [(columnList)]
  VALUES (dataValueList)
  ```

  - 若省略columnList , SQL 将严格按它们在 CREATE TABLE 命令中的顺序。
  - 若给出 columnList ，则 columnList 中未出现的列在建表时不能声明为 NOT NULL, 除非建表时使用 DEFAULT 选项



##### `INSERT ... SELECT `

- 把一个或多个表中的多个行复制到另一个表

  ```sql
  INSERT INTO TableName [(columnList)]
  SELECT ... -- 子查询表达式
  
  # 任何 SELECT 选项和子句都可以使用，也可利用联结从多个表插入数据
  ```

example :

用 `Staff` 表和 `PropertyForRent` 中的数据产生表 `StaffPropCount`

```sql
INSERT INTO StafPropCount
(SELECT s.staffNo, fName, lName, COUNT(*)
FROM Staff s, PropertyForRent p
WHERE s.staffNo = p.staffNo
GROUP BY s.staffNo,fName, lName)
UNION 
(SELECT staffNo,fName, lName,0
FROM Staff s
WHERE NOT EXISTS(SELECT *	
                	FROM PropertyForRent p
                	WHERE p.staffNo = s.staffNo));
-- 若省略此部分，则得到的是至少管理一处房产的员工的列表 
```





- **INSERT SELECT 中的列名**

  为简单起见，这个例子在INSERT 和SELECT 语句中使用了相同的列名。但是，不一定要求列名匹配。事实上，DBMS 一点儿也不关心SELECT返回的列名。它使用的是列的位置，因此SELECT 中的第一列（不管其列名）将用来填充表列中指定的第一列，第二列将用来填充表列中指定的第二列

  



##### `CREATE SELECT`

要将一个表的内容复制到一个全新的表（运行中创建的表），可以使用CREATE SELECT 语句（或者在SQL Server 里也可用SELECT INTO 语句）。

与INSERT SELECT 将数据添加到一个已经存在的表不同，CREATE SELECT 将数据复制到一个新表（有的DBMS 可以覆盖已经存在的表，这依赖于所使用的具体DBMS）。

```sql
CREATE TABLE CustCopy AS SELECT * FROM Customers

-- SQL Server :
SELECT * INTO CustCopy FROM Customers
```





#### 更新数据 UPDATE

UPDATE 允许改变已存在行的内容

```sql
UPDATE TableName
SET columnName1 = dataValue1 [, columnName2 = dataValue2 ...]
[WHERE searchCondition]
```



- **更新所有行**

```sql
UPDATE Staff
SET salary = salary*1.03
```



- 使用子查询

```sql
UPDATE Vendors
SET vend_state = (SELECT UPPER(vend_state)
					FROM Vendors AS V
					WHERE Vendors.vend_state = V.vend_state)
```





#### 删除数据 DELETE

DELETE 从给定表中删除行

DELETE 不需要列名或通配符。DELETE 删除整行而不是删除列。要删除指定的列，请使用UPDATE 语句(将值设置为 NULL)。



```sql
DELETE FROM TableName
[WHERE searchCondition]
-- 若省略where则删除全部数据
```

- **外键约束**

  简单联结两个表只需要这两个表中的公用字段。
  也可以让DBMS 通过使用外键来严格实施关系。

  存在外键时，DBMS 使用它们实施引用完整性。例如要向Products 表中插入一个新产品，DBMS 不允许通过未知的供应商id插入它，因为vend_id 列是作为外键连接到Vendors 表的。

  那么，这与DELETE 有什么关系呢？使用外键确保引用完整性的一个好处是，DBMS 通常可以防止删除某个关系需要用到的行。例如，要从Products 表中删除一个产品，而这个产品用在OrderItems 的已有订单中，那么DELETE 语句将抛出错误并中止。这是总要定义外键的另一个理由。

  

- 删除表的内容而不是表
  DELETE 语句从表中删除行但是不删除表本身， 若想删除表使用 `DROP TABLE`

  **更快的删除**
  如果想从表中删除所有行，不要使用DELETE。可使用TRUNCATE TABLE
  语句，它完成相同的工作，而速度更快（因为不记录数据的变动）。















## DDL 语句

DDL(Data Define Language) :SQL数据定义语言允许创建和删除模式、域、表、视图、索引等数据库对象。



SQL 主要数据定义语句 ：

```sql
CREATE SCHEMA
CREATE DOMAIN
CREATE TABLE
CREATE VIEW

ALTER DOMAIN
ALTER TABLE

DROP SCHEMA
DROP DOMAIN
DROP TABLE
DROP VIEW

-- 许多DBMS 提供以下两个语句，虽然SQL标准不支持 ：
CREATE INDEX
DROP INDEX
```





### 创建数据库

根据 ISO 标准，关系和其他数据库对象都存在于某个环境中。每个环境包含一个或多个目录，每个目录中包含一组模式。模式是一组数据库对象的命名集合，该集合中的对象以某种方式相互关联。模式中的对象可以是表、视图、域、声明、序列、转变规则和字符集。模式中的所有对象有相同的所有者并共享若干模式值。



**模式定义语句 ：**

```sql
CREATE SCHEMA [Name | AUTHORIZATION CreatorIdentifier]

-- 模式 SqlTests 创建者是 Smith :
CREATE SHCEMA SqlTests AUTHORIZATION Smith;
```



**删除模式 ：**

```sql
DROP SCHEMA Name [RESTRICT|CASCADE]
```

- 若指定了 RESTRICT( 也是默认值 ) :  则模式必须为空，否则删除操作失败
- CASCADE : 级联地删除域模式相关的所有对象。其中的任一删除操作失败 则 DROP SCHEMA 操作失败。



#### Schema

https://www.sqlshack.com/a-walkthrough-of-sql-schema/

A SQL database contains multiple objects such as tables, views, stored procedures, functions, indexes, triggers. We define SQL Schema as a logical collection of database objects.

Starting from SQL Server 2005, we have different meanings of user and schema. Now, the database object owner is a schema, and we define schema owners. We can have a single or multiple schema owners. It provides the following benefits:

- We can quickly transfer ownership of a SQL schema to another user
- We can share a schema among multiple users
- It allows you to move database objects among the schemas
- We get more control over database objects access and security

If we do not define any default schema for a user, SQL Server assumes **dbo** as the default schema. 

If not specify any schema in the `CREATE TABLE` statement. It automatically uses dbo schema for the table because the current user default schema is dbo:

##### Retrieve all schema and their owners in a database

```
SELECT s.name AS schema_name, 
       s.schema_id, 
       u.name AS schema_owner
FROM sys.schemas s
     INNER JOIN sys.sysusers u ON u.uid = s.principal_id
ORDER BY s.name
```

![image-20240511192010643](https://s2.loli.net/2024/05/11/NOTPtE7K1Vcu2so.png)





##### create schema

```sql
CREATE SCHEMA <schema_name>
[AUTHORIZATION owner_name]
```

Optionally, you can specify the schema owner as `AUTHORIZATION owner_name`.

the default user is`dbo`(database owner)



After you create a schema, you can create objects under this schema and grant permissions to other users.

example: creates a new table under `hrdbo` schema

```
CREATE TABLE hrdbo.Consultant
(
	ConsultantID int,
	FirstName nvarchar(50) NOT NULL,
	LastName nvarchar(50) NOT NULL
)
```













####  INFORMATION_SCHEMA

https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver16

In relational databases, the INFORMATION_SCHEMA is an ANSI-standard set of read-only views that provide information about all of the tables, views, columns, and procedures in a database

This view can be called from any of the databases in an instance of SQL Server 



The information schema views are defined in a special schema named INFORMATION_SCHEMA. This schema is contained in each database. 

the relationships between the SQL Server names and the SQL standard names.

| SQL Server name        | Maps to this equivalent SQL standard name |
| :--------------------- | :---------------------------------------- |
| Database               | Catalog                                   |
| Schema                 | Schema                                    |
| Object                 | Object                                    |
| user-defined data type | Domain                                    |



##### TABLES

> Returns one row for each table or view **in the current database** for which the current user has permissions.

| Column name   | Data type       | Description                               |
| :------------ | :-------------- | :---------------------------------------- |
| TABLE_CATALOG | `nvarchar(128)` | Table qualifier.                          |
| TABLE_SCHEMA  | `nvarchar(128)` | Name of schema that contains the table.   |
| TABLE_NAME    | `sysname`       | Table or view name.                       |
| TABLE_TYPE    | `varchar(10)`   | Type of table. Can be VIEW or BASE TABLE. |



![image-20240510212428126](https://s2.loli.net/2024/05/10/GohD6P7r3xE54Wq.png)



##### COLUMNS

Returns one row for each column that can be accessed by the current user in the current database.

| Column name                  | Data type                | Description                                                  |
| :--------------------------- | :----------------------- | :----------------------------------------------------------- |
| **TABLE_CATALOG**            | **nvarchar(128)**        | Table qualifier.                                             |
| **TABLE_SCHEMA**             | **nvarchar(128)**        | Name of schema that contains the table.                      |
| **TABLE_NAME**               | **nvarchar(128)**        | Table name.                                                  |
| **COLUMN_NAME**              | **nvarchar(128\**)**     | Column name.                                                 |
| **ORDINAL_POSITION**         | **int**                  | Column identification number.                                |
| **COLUMN_DEFAULT**           | **nvarchar(\**4000\**)** | Default value of the column.                                 |
| **IS_NULLABLE**              | **varchar(\**3\**)**     | Nullability of the column. If this column allows for NULL, this column returns YES. Otherwise, NO is returned. |
| **DATA_TYPE**                | **nvarchar(\**128\**)**  | System-supplied data type.                                   |
| **CHARACTER_MAXIMUM_LENGTH** | **int**                  | Maximum length, in characters, for binary data, character data, or text and image data.  -1 for **xml** and large-value type data. Otherwise, NULL is returned. For more information, see [Data Types (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver16). |
| **CHARACTER_OCTET_LENGTH**   | **int**                  | Maximum length, in bytes, for binary data, character data, or text and image data.  -1 for **xml** and large-value type data. Otherwise, NULL is returned. |
| **NUMERIC_PRECISION**        | **tinyint**              | Precision of approximate numeric data, exact numeric data, integer data, or monetary data. Otherwise, NULL is returned. |
| **NUMERIC_PRECISION_RADIX**  | **smallint**             | Precision radix of approximate numeric data, exact numeric data, integer data, or monetary data. Otherwise, NULL is returned. |
| **NUMERIC_SCALE**            | **int**                  | Scale of approximate numeric data, exact numeric data, integer data, or monetary data. Otherwise, NULL is returned. |
| **DATETIME_PRECISION**       | **smallint**             | Subtype code for **datetime** and ISO **interval** data types. For other data types, NULL is returned. |
| **CHARACTER_SET_CATALOG**    | **nvarchar(\**128\**)**  | Returns **master**. This indicates the database in which the character set is located, if the column is character data or **text** data type. Otherwise, NULL is returned. |
| **CHARACTER_SET_SCHEMA**     | **nvarchar(\**128\**)**  | Always returns NULL.                                         |
| **CHARACTER_SET_NAME**       | **nvarchar(\**128\**)**  | Returns the unique name for the character set if this column is character data or **text** data type. Otherwise, NULL is returned. |
| **COLLATION_CATALOG**        | **nvarchar(\**128\**)**  | Always returns NULL.                                         |
| **COLLATION_SCHEMA**         | **nvarchar(\**128\**)**  | Always returns NULL.                                         |
| **COLLATION_NAME**           | **nvarchar(\**128\**)**  | Returns the unique name for the collation if the column is character data or **text** data type. Otherwise, NULL is returned. |
| **DOMAIN_CATALOG**           | **nvarchar(\**128\**)**  | If the column is an alias data type, this column is the database name in which the user-defined data type was created. Otherwise, NULL is returned. |
| **DOMAIN_SCHEMA**            | **nvarchar(\**128\**)**  | If the column is a user-defined data type, this column returns the name of the schema of the user-defined data type. Otherwise, NULL is returned.  **Important:** Don't use INFORMATION_SCHEMA views to determine the schema of a data type. The only reliable way to find the schema of a type is to use the TYPEPROPERTY function. |
| **DOMAIN_NAME**              | **nvarchar(\**128\**)**  | If the column is a user-defined data type, this column is the name of the user-defined data type. Otherwise, NULL is returned. |











### 创建表 



```sql
CREATE TABLE TableName
{(columnName dataType [NOT NULL][UNIQUE]
[DEFAULT defaultOption][CHECK (searchCondition)][,...]}
[PRIMARY KEY (listOfColumns),]
{[UNIQUE(listOfColumns)][,...]} 
{[FOREIGN KEY(listOfForeignKeyColumns) REFERENCES ParentTableName [(listOfCandidateKeyColumns)]
 	[MATCH {PARTIAL|FULL}
    [ON UPDATE referentialAction]
    [ON DELETE referentialAction]] [,...]}
{[CHECK (searchCondition)]})
```

- CONSTRAINT

  - PRIMARY KEY : 

    - 主关键字的每一列默认为 NOT NULL
    - SQL 拒绝任何使 PRIMARY KEY 列值重复的 INSERT 和 UPDATE 操作，保证主关键字的唯一性

  - FOREIGN KEY

    - 若省略 REFERENCES 的 listOfCandidateKeyColumns ，则认为外部关键字和父表的主关键字相匹配。此时父表的 CREATE TABLE 语句必须含有 PRIMARY KEY 子句

    - 当与子表外部关键字匹配的父表中候选关键字更新时，可选的联系更新规则( ON UPDATE ) 指定应采取的动作。

      父表中候选关键字被删除 ： ON DELETE 

      referentialAction : CASCADE/SET NULL / SET DEFAULT / NO ACTION 

  - CHECK 和 CONSTRAINT 子句允许定义另外的约束。


























## 更新表 ALTER TABLE

![image-20240408163950695](https://s2.loli.net/2024/05/07/qef7YOy1BU946bi.png)





- 在ALTER TABLE 之后给出要更改的表名（该表必须存在，否则将出错）；
- 列出要做哪些更改

```sql
ALTER TABLE Vendors
ADD vend_phone CHAR(20)
```

![image-20240408164528595](https://s2.loli.net/2024/05/07/2WT6P47jqEHoVtu.png)



- 小心使用ALTER TABLE

  使用ALTER TABLE 要极为小心，应该在进行改动前做完整的备份（表结构和数据的备份）。数据库表的更改不能撤销，如果增加了不需要的列，也许无法删除它们。类似地，如果删除了不应该删除的列，可能会丢失该列中的所有数据。



## 删除表 DROP 

删除表没有确认步骤，也不能撤销，执行这条语句将永久删除该表。

```sql
DROP TABLE CustCopy;
```

- 使用关系规则防止意外删除

  许多DBMS允许强制实施有关规则，防止删除与其他表相关联的表。在实施这些规则时，如果对某个表发布一条DROP TABLE 语句，且该表是某个关系的组成部分，则DBMS 将阻止这条语句执行，直到该关系被删除为止。如果允许，应该启用这些选项，它能防止意外删除有用的表





# 视图

- **基本关系 vs 视图**
  - base relation ：与概念模式中的一个实体相对应的具名关系 ，它的元组都存储在数据库的物理结构中。
  - 视图 ( **虚关系** 或 **导出关系** )：对一个或多个基本关系进行关系操作得到的动态结果。
    - 视图是动态的 ：对导出视图的基本关系的修改将立即反映到视图上，当用户对视图做允许的修改时，这些修改将作用到基本关系上。
    - 并不真正存在于数据库中(虽然它的定义存储在系统目录中)。



- 当 DBMS 遇到视图引用时
  - 一种方法是查找视图定义，并将请求转换为对视图源表的等价请求：**视图分解(view resolution)**
  - 把视图存储在数据库的临时表中，并在基表变化时更新临时表以及时维护视图：**视图物化(view materialization)**



- **视图应用** ：

  - 简化复杂的SQL 操作，不必知道其基本查询细节。

  - 隐藏部分数据库信息。授予用户访问表的特定部分的权限

  - 更改数据格式和表示。视图可返回与底层表的表示和格式不同的数据。

    

## **规则和限制**

- 视图可以嵌套，即可以利用从其他视图中检索数据的查询来构造视图。

- 许多DBMS 禁止在视图查询中使用ORDER BY 子句。

  SQL Server 报错 ：`除非另外还指定了 TOP、OFFSET 或 FOR XML，否则，ORDER BY 子句在视图、内联函数、派生表、子查询和公用表表达式中无效`

- 视图不能索引，也不能有关联的触发器或默认值。

- 若视图中某个列是基于聚集函数的，那么在访问该视图的查询语句中，该列只能出现在 SELECT 和 ORDER BY 子句里，即在基于该视图的查询语句中，该列不能出现在 WHERE 子句中 ，也不能作为任何聚集函数的参数

- 分组视图不能与基表或视图连接



### 可更新性

为了使视图可更新，对于任何一个行或列，DBMS 必须都能追溯到其源表中相应的行或列。

![image-20240517173009814](https://s2.loli.net/2024/05/17/ZjdJh9vr6OaSEUk.png)



ISO 标准指出视图可更新的充要条件为 ：

- 未指定 DISTINCT, 即重复元组未从查询结果中消除
- 定义查询的 SELECT 列表中的每个元素均为列名 ( 而不是常量、表达式或聚集函数)，且列名出现次数不多于一次
- FROM 子句只指定一个表。因此排除了基于连接、并交叉操作的所有视图
- WHERE 子句不能包括任何引用了 FROM 子句中的表的嵌套 SELECT 操作
- 定义查询中不能有 GROUP BY 或 HAVING 子句

添加到视图的每一行都不能违反基表的完整性约束。例如，如果通过视图插入一个新行，则视图中没有涉及的列可以设置为空，但这不能违反基表的 NOT NULL 约束。













## 视图创建与删除



### 创建视图

视图通过指定 SQL SELECT 语句定义。

```sql
CREATE VIEW ViewName [(newColumnName[,...])]
AS subselect [WITH [CASCADED |LOCAL] CHECK OPTION]
```

若省略列名表，则视图中列的名字即采用 subselect 子句中相应列的名字

subselect 称为 **定义查询** ， 

若 WITH CHECK OPTION, SQL 将确保那些不满足 subselect 中 WHERE 子句的行不会被添加到视图的基表中。



- 创建水平视图

  ```sql
  CREATE VIEW Manager3Staff
  AS SELECT *
  	FROM Staff
  	WHERE branchNo = 'B003';
  	
  -- 执行
  SELECT * FROM Manager3Staff
  ```

  

- 创建垂直视图

  垂直视图限制用户只能访问一个或多个表中选定的列。

  ```sql
  CREATE VIEW Staff3
  AS SELECT staffNo, fName, lName, position, sex
  	FROM Staff
  	WHERE branchNo = 'B003';
  ```

  

- 分组或连接视图

  使用视图最常见的一个原因就是可以简单地进行多表查询。

  ```sql
  CREATE VIEW StaffPropCnt (branchNo, staffNo, cnt)
  AS SELECT s.branchNO, s.staffNo, COUNT(*)
  	FROM Staff s, PropertyFOrRent p
  	WHERE s.staffNo = p.staffNo
  	GROUP BY s.branchNo, s.staffNo;
  ```

  

  

### 删除视图

```sql
DROP VIEW ViewName [RESTRICT | CASCADE]
```

- CASCADE : 删除所有相关依赖的对象，即也删除定义在被删除视图上的所有视图
- RESTRICT : 若存在依赖被删除视图的其他对象，sql将不进行该删除操作，默认设置为 RESTRICT 





### WITH CHECK OPTION

视图中的行均满足**定义查询**中的 WHERE 条件。

如果某行被修改后不再满足这种条件，那么它应当从视图中去除。相似地，当对视图进行插入和更新时，若有新行满足 WHERE 条件，那么这些新行便会出现在视图中 。进入或离开视图的行称为 **迁移行** 。



- WITH CHECK OPTION 子句用于禁止行迁移出视图( 即不允许会导致行迁移出去的 UPDATE 操作 , 即需要 UPDATE 后的数据仍需要满足定义视图时的 WHERE 条件) 。：

  exmaple :

  ```sql
  CREATE VIEW IS_Class
  AS
  SELECT * 
  FROM Class
  WHERE className LIKE '注册会计%'
  WITH CHECK OPTION
  
  -- 把“注册会计08_01班”改为“会计08_01班” : 报错
  -- 把“注册会计08_01班”改为“注册会计08_02班” :成功
  ```

  

- 可选修饰词 LOCAL/ CASCADED 应用于层次视图 （由视图导出的视图 ）

  `WITH LOCAL|CASCADED CHECK OPTION`

> WITH LOCAL CHECK OPTION：在该视图或由该视图直接导出的视图上进行插入或更新操作时，不允许行迁移出视图，除非该行也迁移出底层视图或表

> WITH CASCADED CHECK OPTION : 在该视图或由该视图直接导出的视图上进行插入或更新操作时，都不允许行迁移出视图

![image-20240517192337353](https://s2.loli.net/2024/05/17/rjVKbE3Bl2YyPmw.png)

















## 视图分解



example ：

```sql
SELECT staffNo, cnt
FROM StaffPropCnt
WHERE branchNo = 'B003'
ORDER BY staffNo;
```

视图分解是将以上查询与 StaffPropCnt 视图的定义查询合并 ：



1. 将 SELECT 列表中给出的视图列名转换为定义查询中相应的列名

   `SELECT s.staffNo AS staffNo, COUNT(*) AS cnt`

2. FROM 子句中的视图名用定义查询中相应的FROM 列表替代

   `FROM Staff s, PropertyForRent p`

3. 用逻辑运算符 AND 合并来自用户查询的 WHERE 子句和 定义查询的 WHERE 子句 ：

   `WHERE s.staffNo = p.staffNo AND branchNo = 'B003'`

4. 从定义查询复制 GROUP BY 和 HAVING 子句

   ```sql
   GROUP BY s.branchNo, s.staffNo
   ```

5. 从用户查询复制 ORDER BY 子句, 视图列名转换为定义查询的列名

   `ORDER BY s.branchNo, s.staffNo`

6. 合并查询





## 视图物化

**将第一次访问视图的结果存储为数据库的临时表**。这样，基于物化视图的查询比每次计算视图要快得多。当查询频繁且视图复杂，以至于每次查询都计算视图不现实时，这种速度上的差异在应用中就显得非常重要了 。

这种方法的困难之处在于基表更新的同时还要保证视图的实时性。更新基表的同时引起物化视图更新的过程称为**视图维护** 。









# 存储过程

![image-20240409121444135](https://s2.loli.net/2024/05/07/ZkhOQyMbUt4Fp9g.png)

可以单独编写每条SQL 语句，并根据结果有条件地执行其他语句。在每次需要这个处理时（以及每个需要它的应用中），都必须做这些工作。
也可以创建存储过程。简单来说，存储过程就是为以后使用而保存的一条或多条SQL 语句。可将其视为批文件，虽然它们的作用不仅限于批处理。

- SQLite 不支持存储过程





**意义**

由于不要求反复建立一系列处理步骤，因而保证了数据的一致性。如果所有开发人员和应用程序都使用同一存储过程，则所使用的代码都是相同的。

简化对变动的管理。如果表名、列名或业务逻辑（或别的内容）有变化，那么只需要更改存储过程的代码。使用它的人员甚至不需要知道这些变化。

![image-20240409121908657](https://s2.loli.net/2024/05/07/IYQrPUbtvAh8xZH.png)



## 执行存储过程

`EXECUTE ` 接受 存储过程名 和 需要传递给它的任何参数



example :

```sql
EXECUTE AddNewProduct('JTS01',
'Stuffed Eiffel Tower',
6.49,
'Plush stuffed toy with
➥the text La Tour Eiffel in red white and blue');
```

这里执行一个名为 `AddNewProduct `的存储过程，将一个新产品添加到`Products` 表中。

`AddNewProduct `有四个参数，这4 个参数匹配存储过程
中4 个预期变量（定义为存储过程自身的组成部分）。此存储过程将新行添加到Products 表，并将传入的属性赋给相应的列。
我们注意到，在Products 表中还有另一个需要值的列prod_id 列，它是这个表的主键。为什么这个值不作为属性传递给存储过程？

要保证恰当地生成此ID，最好是使生成此ID 的过程自动化（而不是依赖于最终用户的输入）。这也是这个例子使用存储过程的原因。



**以下是存储过程所完成的工作：**

- 验证传递的数据，保证所有4 个参数都有值；
- 生成用作主键的唯一ID；
- 将新产品插入Products 表，在合适的列中存储生成的主键和传递的数据。



对于具体的DBMS，可能包括以下的执行选择 

 参数可选，具有不提供参数时的默认值。
 不按次序给出参数，以“参数=值”的方式给出参数值。
 输出参数，允许存储过程在正执行的应用程序中更新所用的参数。
 用SELECT 语句检索数据。
 返回代码，允许存储过程返回一个值到正在执行的应用程序。





## 创建存储过程



example : 它对邮件发送清单中具有邮件地址的顾客进行计数

Oracle 版本

```sql
CREATE PROCEDURE MailingListCount(
	ListCount OUT INTEGER
)
IS
v_rows INTEGER;
BEGIN 
	SELECT COUNT(*) INTO v_rows
	FROM Customers
	WHERE NOT cust_email  IS NULL;
	ListCount := v_rows;
END;
```

- 这个存储过程有一个名为ListCount 的参数。此参数从存储过程返回一个值而不是传递一个值给存储过程. 关键字OUT 用来指示这种行为。

  Oracle 支持IN（传递值给存储过程）、OUT（从存储过程返回值）、
  INOUT（既传递值给存储过程也从存储过程传回值）类型的参数

- 存储过程的代码括在BEGIN 和END 语句中，这里执行一条简单的SELECT 语句，它检索具有邮件地址的顾客。然后用检索出的行数设置ListCount（要传递的输出参数）。



**调用 Oracle 例子** ：

```sql
var ReturnValue NUMBER
EXEC MailingListCount(:ReturnValue);
SELECT ReturnValue;
```

这段代码声明了一个变量来保存存储过程返回的任何值，然后执行存储过程，再使用SELECT 语句显示返回的值。





**SQL Server 版本**

```sql
CREATE PROCEDURE MailingListCount
AS 
DECLARE @cnt INTEGER
SELECT @cnt = COUNT(*)
FROM Customers
WHERE NOT cust_email IS NULL
RETURN @cnt
```

此存储过程没有参数。调用程序检索SQL Server 的返回代码提供的值。其中用DECLARE 语句声明了一个名为@cnt 的局部变量

**SQL Server 中所有局部变量名都以@打头**



**调用 SQL Server例子** 

```sql
DECLARE @ReturnValue INT
EXECUTE @ReturnValue=MailingListCount;
SELECT @ReturnValue;
```

这段代码声明了一个变量来保存存储过程返回的任何值，然后执行存储过程，再使用SELECT 语句显示返回的值。



example2 :

```sql
CREATE PROCEDURE NewOrder @cust_id CHAR(10)
AS
-- 为订单号声明一个变量
DECLARE @order_num INTEGER
-- 获取当前最大订单号
SELECT @order_num=MAX(order_num)
FROM Orders
-- 决定下一个订单号
SELECT @order_num=@order_num+1
-- 插入新订单
INSERT INTO Orders(order_num, order_date, cust_id)
VALUES(@order_num, GETDATE(), @cust_id)
-- 返回订单号
RETURN @order_num;
```

此存储过程在Orders 表中创建一个新订单。它只有一个参数，即下订单顾客的ID。订单号和订单日期这两列在存储过程中自动生成。



Another version :

```sql
CREATE PROCEDURE NewOrder @cust_id CHAR(10)
AS
-- 插入新订单
INSERT INTO Orders(cust_id)
VALUES(@cust_id)
-- 返回订单号
SELECT order_num = @@IDENTITY;
```

这次由DBMS 生成订单号。大多数DBMS 都支持这种功能；

SQL Server 中称这些自动增量的列为标识字段( identity field ), 而其他 DBMS 称之为 自动编号(auto number) 或序列( sequence )

怎样才能得到这个自动生成的ID？在SQL Server上可在全局变量@@IDENTITY 中得到，它返回到调用程序（这里使用SELECT 语句）。



# 事务处理

事务处理( transaction processing ) ： 通过确保成批的 SQL 操作要么完全执行，要么完全不执行，来维护数据库的完整性， 保证数据库不包含不完整的操作结果 。

- 事务( transaction ) : 指一组 SQL 语句
- 回退( rollback ) : 撤销指定 SQL 语句
- 提交( commit ) : 将未存储的 SQL 语句结果写入数据库表 ；
- 保留点（savepoint）指事务处理中设置的临时占位符（placeholder），可以对它发布回退（与回退整个事务处理不同）。

- **可以回退哪些语句？**

  事务处理用来管理INSERT、UPDATE 和DELETE 语句

  不能回退SELECT语句（回退SELECT 语句也没有必要）也不能回退CREATE 或DROP 操作。事务处理中可以使用这些语句，但进行回退时，这些操作不撤销







## 控制事务处理

管理事务的关键在于将SQL 语句组分解为逻辑块，并明确规定数据何时应该回退，何时不应该回退。



SQL Server:

```sql
BEGIN TRANSACTION
...
COMMIT TRANSACTION
```

在这个例子中，BEGIN TRANSACTION 和COMMIT TRANSACTION 语句之间的SQL 必须完全执行或者完全不执行。

MariaDB 和MySQL 中等同的代码为：

```sql
START TRANSACTION
...
```


Oracle 使用的语法：

```
SET TRANSACTION
...
```


其他DBMS 采用上述语法的变体。

你会发现，**多数实现没有明确标识事务处理在何处结束**。事务一直存在，直到被中断。

通常，`COMMIT` 用于保存更改，`ROLLBACK` 用于撤销



### `ROLLBACK`

ROLLBACK 命令用来回退（撤销）SQL 语句

```sql
DELETE FROM Orders;
ROLLBACK;
```

虽然这不是最有用的例子，但它的确能够说明，在事务处理块中，DELETE 操作（与 INSERT  和 UPDATE  操作一样）并不是最终的结果。





### `COMMIT`

一般的SQL 语句都是针对数据库表直接执行和编写的 。这就是所谓的隐式提交  ( implicit commit ) , 即提交( 写或保存操作是自动进行的 )

在事务处理块中，提交不会隐式进行。不过，不同DBMS 的做法有所不同。有的DBMS 按隐式提交处理事务端，有的则不这样。



SQL Server :

```sql
BEGIN TRANSACTION
DELECT OrderItems WHERE order_num = 12345
DELECT Orders WHERE order_num = 12345
COMMIT TRANSACTION
```

由于设计更新两个数据库表 Orders 和 OrderItems, 故使用事务处理来保证订单不被部分删除 。

末尾的 `COMMIT TRANSACTION` 仅在不出错时提交更改 。如果第一条DELETE 起作用，但第二条失败，则DELETE 不会提交。



Oracle:

```sql
SET TRANSACTION
DELETE OrderItems WHERE order_num = 12345;
DELETE Orders WHERE order_num = 12345;
COMMIT;
```



### 使用保留点

使用简单的ROLLBACK 和COMMIT 语句，就可以写入或撤销整个事务。但是，只对简单的事务才能这样做，复杂的事务可能需要部分提交或回退。

例如前面描述的添加订单的过程就是一个事务。如果发生错误，只需要返回到添加Orders 行之前即可。不需要回退到Customers 表（如果存在的话）。



要支持回退部分事务，必须在事务处理块中的合适位置放置**占位符 (保留点)**。

每个保留点都要取能标识它的唯一名字，以便在回退时 DBMS 知道要回退到何处 。



**创建保留点 ：**

- 在MariaDB、MySQL 和Oracle 中创建占位符，可使用`SAVEPOINT`  :

  ```sql
  SAVEPOINT delete1;
  ```

- SQL Server:

  ```sql
  SAVE TRANSACTION delete1
  ```

  

**回退到保留点 ：**

- MariaDB、MySQL 和Oracle :

  ```sql
  ROLLBACK TO delete1;
  ```

  

- SQL Server

  ```sql
  ROLLBACK TRANSACTION delete1;
  ```

  

## example : 给系统添加订单

(1) 检查数据库中是否存在相应的顾客，如果不存在，添加

(2) 检索顾客的ID；

(3) 在Orders 表添加一行，它与顾客ID 相关联；

(4) 检索Orders 表中赋予的新订单ID；

(5) 为订购的每个物品在OrderItems 表中添加一行，通过检索出来的ID把它与Orders 表关联（并且通过产品ID 与Products 表关联）。

现在假设由于某种数据库故障（如超出磁盘空间、安全限制、表锁等），这个过程无法完成。数据库中的数据会出现什么情况？

如果故障发生在添加顾客之后，添加Orders 表之前，则不会有什么问题。某些顾客没有订单是完全合法的。重新执行此过程时，所插入的顾客记录将被检索和使用。可以有效地从出故障的地方开始执行此过程。
但是，如果故障发生在插入Orders 行之后，添加OrderItems 行之前，怎么办？现在数据库中有一个空订单。
更糟的是，如果系统在添加OrderItems 行之时出现故障，怎么办？结果是数据库中存在不完整的订单，而你还不知道。

如何解决这种问题？这就需要使用事务处理了

**利用事务处理，可以保证一组操作不会中途停止，它们要么完全执行，要么完全不执行（除非明确指示）。如果没有错误发生，整组语句提交给（写到）数据库表；如果发生错误，则进行回退（撤销），将数据库恢复到某个已知且安全的状态。**



(1) 检查数据库中是否存在相应的顾客，如果不存在，添加他；
(2) 提交顾客信息；
(3) 检索顾客的ID；
(4) 在Orders 表中添加一行；
(5) 如果向Orders 表添加行时出现故障，回退；
(6) 检索Orders 表中赋予的新订单ID；
(7) 对于订购的每项物品，添加新行到OrderItems 表；
(8) 如果向OrderItems 添加行时出现故障，回退所有添加的OrderItems行和Orders 行。



SQL Server

```sql
BEGIN TRANSACTION
INSERT INTO Customers(cust_id, cust_name)
VALUES(10000000010, 'Toys Emporium');
SAVE TRANSACTION StartOrder;

INSERT INTO Orders(order_num, order_date, cust_id)
VALUES(20100, '2001/12/1', 10000000010)
IF @@ERROR <> 0 ROLLBACK TRANSACTION StartOrder;

INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price)
VALUES(20100, 2, 'BR03', 100, 10.99);
IF @@ERROR <> 0 ROLLBACK TRANSACTION StartOrder;
COMMIT TRANSACTION
```

**保留点越多越好**
可以在SQL 代码中设置任意多的保留点，越多越好。因为保留点越多，你就越能灵活地进行回退。







# 游标

SQL 检索操作返回一组称为结果集的行， 这组返回的行都是与SQL 语句相匹配的行( 0 行到多行 )， 简单使用SELECT 语句，无法得到第一行，下一行或前10 行。

有时需要在检索出来的行中前进或后退一行或多行， 这就是游标的用途所在 。

**游标( cursor ) 是一个存储在 DBMS 服务器上的数据库查询 ， 它不是一条 SELECT 语句，而是被该语句检索出来的结果集。**

**在存储了游标之后， 应用程序可以根据需要滚动或浏览其中的数据** 



- 不同的DBMS 支持不同的游标选项和特性。常见的一些选项和特性如下。
  - 标记游标为只读
  - 标记某些列为可编辑的，某些列为不可编辑的
  - 控制可以执行的定向操作( 向前， 向后， 第一，最后，绝对位置和相对位置等 )
  - 规定范围， 使游标对创建它的特定请求( 如存储过程 ) 或对所有请求可访问 
  - 指示DBMS 对检索出的数据进行复制，使数据在游标打开和访问期间不变化

**游标主要用于交互式应用，其中用户需要滚动屏幕上的数据，并对数据进行浏览或做出更改。**





## **STEPS** ：

1. **声明  (  定义 ）游标 **

   在使用游标前，必须声明（定义）它。这个过程实际上没有检索数据 ， 它只是定义要使用的 SELECT 语句和游标选项 。

2. **打开游标**

   一旦声明， 就必须打开游标以供使用。该过程用前面定义的 SELECT 语句把数据实际检索出来 。

3. **检索**

   对于填有数据的游标，根据需要取出（检索）各行。

4. **关闭游标**

   在结束游标使用时，必须关闭游标，可能的话，释放游标（取决于具体的DBMS）。





### **创建游标**

`DECLARE` 语句创建游标 ， 这条语句在不同的 DBMS 中有所不同。 

`DECLARE	` 命名游标， 并创建相应的 SELECT 语句 ， 根据需要带 WHERE 和其他 子句 。



example：

 DB2、MariaDB、MySQL 和SQL Server ：

```sql
DECLARE CustCursor CURSOR
FOR 
SELECT * FROM Customers
WHERE cust_email IS NULL;
```





### **使用游标**

`OPEN CURSOR` 打开游标

```sql
OPEN CURSOR CustCursor
```

在处理 `OPEN CURSOR` 语句时 ， 执行查询， 存储检索出的数据以供浏览和滚动。



- `FETCH` 访问游标数据

  `FETCH` 指出要检索哪些行， 从何处检索它们以及将它们放于何处（如变量名）。



example 1  Oracle:

```sql
DECLARE TYPE CustCursor IS REF CURSOR
	RETURN Customer%ROWTYPE;
DECLARE CustRecord Customers%ROWTYPE
BEGIN
	OPEN CustoCursor;
	FETCH CustCursor INTO CustRecord;
	CLOSE CustCursor;
END;
```

在这个例子中，FETCH 用来检索当前行（自动从第一行开始），放到声明的变量CustRecord 中。对于检索出来的数据不做任何处理。



example 2  Oracle:

```sql
DECLARE TYPE CustCursor IS REF CURSOR
	RETURN Customers%ROWTYPE;
DECLARE CustRecored Customers%ROWTYPE
BEGIN
	OPEN CustCursor;
	LOOP
	FETCH CustCUrsor INTO CustRecord;
	EXIT WHEN CUstCursor%NOTFOUND;
	...
	END LOOP;
	CLOSE CustCursor;
END;
```

，这个例子使用FETCH 检索当前行，放到一个名为
`CustRecord `的变量中。但不一样的是，这里的FETCH 位于LOOP 内，因此它反复执行。代码`EXIT WHEN CustCursor%NOTFOUND` 使在取不出更多的行时终止处理（退出循环）。



example 3 SQL Server:

```sql
DECLARE @cust_id CHAR(10),
		@cust_name CHAR(50),
		@cust_address CHAR(50),
		@cust_city CHAR(50).
		@cust_state CHAR(5)
		@cust_zip CHAR(10),
		@cust_country CHAR(50),
		@cust_contact CHAR(50),
		@cust_email CHAR(255)
OPEN CustCursor
FETCH NEXT FROM CustCursor
	INTO @cust_id, @cust_name, @cust_address,
@cust_city, @cust_state, @cust_zip,
@cust_country, @cust_contact, @cust_email
...
while @@FETCH_STATUS = 0
BEGIN

FETCH NEXT FROM CustCursor
		INTO @cust_id, @cust_name, @cust_address,
@cust_city, @cust_state, @cust_zip,
@cust_country, @cust_contact, @cust_email
...
END 
CLOSE CustCursor
```





### **关闭游标**

DB2、Oracle、 PostgreSQL

```sql
CLOSE CustCursor
```



Microsoft SQL Server:

```sql
CLOSE CustCursor
DEALLOCATE CURSOR CustCursor
```

CLOSE 语句用来关闭游标。一旦游标关闭，如果不再次打开，将不能使用。第二次使用它时不需要再声明，只需用OPEN 打开它即可。





# 高级SQL特性



- 





## 索引

**索引用来排序数据以加快搜索和排序操作的速度 。**



主键数据总是排序的，这是DBMS 的工作。因此，按主键检索特定行总是一种快速有效的操作。

但是，搜索其他列中的值通常效率不高。例如，如果想搜索住在某个州的客户，怎么办？因为表数据并未按州排序，DBMS必须读出表中所有行（从第一行开始），看其是否匹配。这就像要从没有索引的书中找出词汇一样。

解决方法是使用索引。 可以在一个或多个列上定义索引， 使 DBMS 保存其内容的一个排过序的列表。在定义了索引之后， DBMS 以使用书的索引类似的方法使用它。 DBMS 搜索排过序的索引， 找出匹配的位置， 然后检索这些行。



- 索引改善检索操作的性能，但降低了数据插入、修改和删除的性能。在执行这些操作时，DBMS 必须动态地更新索引。
- 索引数据可能要占用大量的存储空间。
- 并非所有数据都适合做索引。取值不多的数据（如州）不如具有更多可能值的数据（如姓或名），能通过索引得到那么多的好处。
- 索引用于数据过滤和数据排序。如果你经常以某种特定的顺序排序数据，则该数据可能适合做索引。
- 可以在索引中定义多个列（例如，州加上城市）。这样的索引仅在以州加城市的顺序排序时有用。如果想按城市排序，则这种索引没有用处。



### `CREATE INDEX` 创建索引

不同DBMS 创建索引的语句变化很大

```sql
-- 在Products 表的产品名列上创建一个简单的索引
CREATE INDEX prod_name_ind
ON Products (prod_name);
```

索引必须唯一命名。这里的索引名prod_name_ind 在关键字CREATE INDEX 之后定义。ON 用来指定被索引的表，而索引中包含的列（此例中仅有一列）在表名后的圆括号中给出。



## 触发器

触发器是特殊的存储过程，它在特定的数据库活动发生时自动执行。触发器可以与特定表上的INSERT、UPDATE 和DELETE 操作（或组合）相关联。



与存储过程不一样（存储过程只是简单的存储SQL 语句），触发器与单个的表相关联。与Orders 表上的INSERT 操作相关联的触发器只在
Orders 表中插入行时执行。类似地，Customers 表上的INSERT 和
UPDATE 操作的触发器只在表上出现这些操作时执行。



**触发器内的代码具有以下数据的访问权：**
 INSERT 操作中的所有新数据；
 UPDATE 操作中的所有新数据和旧数据；
 DELETE 操作中删除的数据。



**触发器的一些常见用途**
 保证数据一致。例如，在INSERT 或UPDATE 操作中将所有州名转换为大写。
 基于某个表的变动在其他表上执行活动。例如，每当更新或删除一行时将审计跟踪记录写入某个日志表。

 进行额外的验证并根据需要回退数据。例如，保证某个顾客的可用资金不超限定，如果已经超出，则阻塞插入。

 计算计算列的值或更新时间戳。



example ：

SQL Server:

```sql
CREATE TRIGGER customer_state
ON Customers
FOR INSERT, UPDATE
AS
UPDATE cUSTOMERS
SET cust_state = Upper(cust_state)
WHERE Customers.cust_id = inserted.cust_id;
```



Oracle , PostgreSQL:

```sql
CREATE TRIGGER customer_state
AFTER INSERT OR UPDATE
FOR EACH ROW
BEGIN
UPDATE Customers
SET cust_state = Upper(cust_state)
WHERE Customers.cust_id = :OLD.cust_id
END;
```











# T-SQL

Transact-SQL (T-SQL) is Microsoft's proprietary extension of SQL used in SQL Server and Azure SQL Database. It adds various programming constructs such as variables, control-of-flow language, and error handling to SQL's data manipulation language (DML).

Some common tasks performed using T-SQL include:

1. **Data Retrieval**: SELECT statement is used to query data from tables.
2. **Data Modification**: INSERT, UPDATE, DELETE statements are used to add, modify, or remove data from tables.
3. **Data Definition**: CREATE, ALTER, DROP statements are used to define, modify, or remove database objects like tables, views, stored procedures, etc.
4. **Data Control**: GRANT, REVOKE statements are used to control access to database objects.
5. **Transaction Control**: BEGIN TRANSACTION, COMMIT TRANSACTION, ROLLBACK TRANSACTION statements are used to control transactions.
6. **Error Handling**: TRY…CATCH blocks are used to handle errors in T-SQL scripts or stored procedures.





## data types

https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver16

![SQL Server Data Types](https://www.sqlservertutorial.net/wp-content/uploads/SQL-Server-Data-Types.png)

Notice that SQL Server will remove **ntext**, **text**, and **image** data types in its future version. Therefore, you should avoid using these data types and use **nvarchar(max)**, **varchar(max)**, and **varbinary(max)** data types instead.



### numeric

#### Exact numeric data types

Exact numeric data types store exact numbers such as integer, decimal, or monetary amount.



- The `bit `store one of three values : 0, 1 and Null
- The `int `, `bigint`, `smallint`, `tinyint` data types store integer data.
- The `decimal` and  `numeric` data types store numbers that have fixed precision and scale. Note that decimal and numeric are synonyms.
- The `money` and `smallmoney` data types store currency values.

![image-20240418192727258](https://s2.loli.net/2024/05/07/9p7BrWmYNxSsuzF.png)



#### Decimal and numeric

`decimal[(p[,s])]` and `numeric[(p[,s])]`

Fixed precision and scale numbers

When maximum precision is used , valid values are from  - 10^38^ + 1 through 10^38^ -1 ,

The ISO synonyms for decimal  are dec and dec(p, s)**. **numeric is functionally identical to decimal.



- **Arguments**

  - **p (precision)**

    The maximum total number of decimal digits to be stored. This number includes both the left and the right sides of the decimal point. 

    The precision must be a value from 1 through the maximum precision of 38. The default precision is 18.

  - **s (scale, 小数位数)**

    Can only be specified if precision is specified. The default scale is 0 and so 0 <= *s* <= *p*. 

    Number of decimal digits stored to the **right of the decimal point.** `p - s `determine the maximum number of digits to the left of the decimal point. 




- **Converting** 

  - In Transact-SQL statements, **a constant with a decimal point is automatically converted into a numeric data value, using the minimum precision and scale necessary.**

    Example : the constant 12.345 is converted into a numeric value with a precision of 5 and a scale of 3 .

  - Converting from decimal or numeric to float or  real can cause some loss of precision. 

  - Converting from int, smallint, tinyint, float**, **real**, **money, or smallmoney to either decimal or numeric can cause overflow.



#### Approximate numeric data types

![image-20240418193649848](https://s2.loli.net/2024/05/07/OiWkzqNaTpuXRHD.png)

**syntax**

`float[(n)]` : n is the number of bits that are used to store the mantissa of the float number in scientific notation and, therefore, dictates the precision and storage size.

 If *n* is specified, it must be a value between **1** and **53**. The default value of *n* is **53**.

| *n* value | Precision | Storage size |
| :-------- | :-------- | :----------- |
| **1-24**  | 7 digits  | 4 bytes      |
| **25-53** | 15 digits | 8 bytes      |

 Note

SQL Server treats *n* as one of two possible values. If **1**<=n<=**24**, *n* is treated as **24**. If **25**<=n<=**53**, *n* is treated as **53**.





### Strings



#### Character strings

**`char[(n)]`**

The ISO synonym for **char** is **character**. 

- Fixed-size string data. 
- *n* defines the string size in bytes 1 <= n <= 8000



**`varchar[(n|max)]`**

the ISO synonyms for **varchar** are **char varying** or **character varying**.

- Variable-size string data. 
- Use *n* to define the max string size in bytes ,1 <= n <= 8000 
- use 2 more bytes for the length information
- or use **max** to indicate a column constraint size up to a maximum of 2^31-1 bytes (2 GB)



**Remarks**

- *n* never defines numbers of characters that can be stored. 

  when using single-byte encoding, the storage size and the number of characters is both *n*. However, for multibyte encoding such as [UTF-8](https://www.wikipedia.org/wiki/UTF-8), higher Unicode ranges (128 to 1,114,111) result in one character using two or more bytes.



- When *n* isn't specified , the default length is 1. 















#### binary and varbinary



##### `binary[(n)]`

Fixed-length binary data with a length of *n* bytes, where *n* is a value from 1 through 8,000. The storage size is *n* bytes.



##### `varbinary [ ( n | max ) ]`

Variable-length binary data. *n* can be a value from 1 through 8,000. max indicates that the maximum storage size is 2^31^-1 bytes. The storage size is the actual length of the data entered + 2 bytes. The data that is entered can be 0 bytes in length.





##### truncation

```sql
DECLARE @BinaryVariable2 BINARY(2);
  
SET @BinaryVariable2 = 123456;
SET @BinaryVariable2 = @BinaryVariable2 + 1;
  
SELECT CAST( @BinaryVariable2 AS INT);
GO
```





Transact-SQL 语句可以使用下列方法进行编写并提交到 数据库引擎 ：

- 通过使用 SQL Server Management Studio。
- 通过使用 [sqlcmd](https://learn.microsoft.com/zh-cn/sql/tools/sqlcmd/sqlcmd-utility?view=sql-server-ver16) 实用工具。
- 通过从您创建的应用程序进行连接。

代码以相同方式和相同权限在 数据库引擎 上执行，而不管您如何提交代码语句



## DEMO



### 创建数据库

```sql
CREATE DATABASE TestData
GO
```

1. 使用指针选择词语 `CREATE DATABASE`，再按 **F1**。 `CREATE DATABASE` 文章将打开。 你可以使用此方法查找 `CREATE DATABASE` 以及在本教程中使用的其他语句的完整语法。
2. 按 **F5** 以执行语句



> Tips :**在单个批处理中提交多条语句时，可以用关键字 GO 分隔各语句。 当批处理只包含一条语句时，GO 是可选的。**



### 创建表

```sql
USE TestData
GO

CREATE TABLE dbo.Products
    (ProductID int PRIMARY KEY NOT NULL,
    ProductName varchar(25) NOT NULL,
    Price money NULL,
    ProductDescription varchar(max) NULL)
GO

```

架构是拥有表的数据库对象。 如果您是管理员，则 `dbo` 是默认架构。 `dbo` 代表数据库所有者。



### 插入和更新表中数据

```sql
-- Standard syntax
INSERT dbo.Products (ProductID, ProductName, Price, ProductDescription)
    VALUES (1, 'Clamp', 12.48, 'Workbench clamp')
GO
```



删除表中的所有行：

```sql
TRUNCATE TABLE TestData.dbo.Products;
GO
```





### 配置数据库对象权限

授予用户访问数据库的权限涉及三个步骤。 首先，创建登录名。 使用登录名，用户可以连接到 SQL Server 数据库引擎。 然后将登录名配置为指定数据库中的用户。 最后，授予该用户访问数据库对象的权限。



- **创建登录名**

   登录名可以将用户身份表示为 Windows 帐户或 Windows 组成员，登录名也可以是仅存在于 SQL Server 中的 SQL Server登录名。 应该尽可能使用 Windows 身份验证。

  

  - **创建新的windows账户**

  1. 选择“开始”后，选择“运行”，在“打开”框中，键入 `%SystemRoot%\system32\compmgmt.msc /s`，然后选择“确定”打开“计算机管理”程序。

  2. 在“系统工具”下，展开“本地用户和组”，右键单击“用户”，然后选择“新建用户”。

     ...

     

  - **创建SQL登录名**

    ```
    CREATE LOGIN [your_computer_name\Mary]
        FROM WINDOWS
        WITH DEFAULT_DATABASE = [TestData];
    GO
    ```

    

    

### 删除数据库对象



#### 删除数据库

正在使用 `TestData` 数据库时，无法删除该数据库；因此，请首先将上下文切换到其他数据库，再使用 `DROP` 语句删除 `TestData` 数据库：

```sql
USE MASTER;
GO
DROP DATABASE TestData;
GO
```



## DDL



### `CREATE TABLE`

```sql
CREATE TABLE
    { database_name.schema_name.table_name | schema_name.table_name | table_name }
    ( { <column_definition> } [ ,... n ] )
[ ; ]
```



```sql
<column_definition> ::=
column_name <data_type>
    [ [ CONSTRAINT constraint_name ] DEFAULT constant_expression ]
    [ [ CONSTRAINT constraint_name ] {NULL | NOT NULL} ]
    [ <column_constraint> [ ,... n ] ]
    [ <column_index> ]
   

<column_constraint> ::=
[ CONSTRAINT constraint_name ]
{
   { PRIMARY KEY | UNIQUE }
        [ ( <column_name> [ ,... n ] ) ]

  | [ FOREIGN KEY ]
        REFERENCES [ schema_name. ] referenced_table_name [ ( ref_column ) ]
        [ ON DELETE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ ON UPDATE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        
  | CHECK [ NOT FOR REPLICATION ] ( logical_expression )
}
```



### `INSERT`

```sql
INSERT   
{  
        [ TOP ( expression ) [ PERCENT ] ]   
        [ INTO ]   
        { <object> | rowset_function_limited   
          [ WITH ( <Table_Hint_Limited> [ ...n ] ) ]  
        }  
    {  
        [ ( column_list ) ]   
        [ <OUTPUT Clause> ]  
        { VALUES ( { DEFAULT | NULL | expression } [ ,...n ] ) [ ,...n     ]   
        | derived_table   
        | execute_statement  
        | <dml_table_source>  
        | DEFAULT VALUES   
        }  
    }  
}  
[;]  
  
<object> ::=  
{   
    [ server_name . database_name . schema_name .   
      | database_name .[ schema_name ] .   
      | schema_name .   
    ]  
  table_or_view_name  
}  
```

