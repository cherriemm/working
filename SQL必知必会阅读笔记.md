

# 关系代数与关系演算



可以将关系代数描述为一种( 高级的 ) 过程式语言， 即可用它告诉 DBMS 如何从数据库的一个或多个关系中构建新关系 ； 而将关系演算看成一种非过程式语言 ， 它用公式给出由数据库的一个或多个关系中构建新关系的定义。关系代数和关系演算形式上是相互等价的 。

演算和代数都是形式语言， 对用户不太友好。 它们通常用作其他高级关系数据库数据操作语言( DML )



关系演算用来衡量关系语言的选择能力 。如果一种语言可以生成所有由关系演算推导出来的关系，就称它具有关系完备性



## 关系代数

关系代数是一种纯理论语言， 它定义了一些操作， 运用这些操作可以从一个或多个关系中得到另一个关系，而不改变原关系。 因此它的操作数和操作结果都是关系， 而且一个操作的输出可以作为另一个操作的输入。故而关系代数的一个表达式中可以嵌套另一个表达式， 这种性质称为闭包 ( closure ) : 关系在关系代数下是封闭的 ， 正如数在算数运算下是封闭的一样。



关系代数中有 五个基本运算 ：选择、投影、笛卡尔乘积、集合并、集合差 ， 还有连接 、集合交、除运算等。

![image-20240422204512140](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422204512140.png)



### 一元运算



#### 选择

![image-20240422204612602](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422204612602.png)



![image-20240422204633382](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422204633382.png)



#### 投影

![image-20240422204656657](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422204656657.png)





### 二元运算



#### 集合并

![image-20240422204756296](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422204756296.png)

可以先用投影运算使得两个关系具有并相容性。



#### 集合差

![image-20240422204922618](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422204922618.png)



#### 集合交

![image-20240422204947217](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422204947217.png)





#### 笛卡尔积

![image-20240422205024961](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422205024961.png)

若一个关系有 I 个元组， N 个属性； 而另一个关系有 J 个元组，M 个属性， 则它们的笛卡尔乘积将会有 ( I * J ) 个元组， ( N + M ) 个属性。



![image-20240422205227421](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422205227421.png)





#### 除法运算

![image-20240423143528067](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423143528067.png)

![image-20240423143545483](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423143545483.png)





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

![image-20240422205708214](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422205708214.png)

![image-20240422205719781](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422205719781.png)



#### 等接

在谓词 F 仅包含 = 的情况下， θ连接就变成了等接(` Equijoin` )

![image-20240422205840946](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422205840946.png)





#### 自然连接

![image-20240422205940573](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422205940573.png)





#### 外连接

连接两个关系时，常会出现一个关系中的某些元组无法在另一个关系中找到匹配元组的情况。 即这些元组在连接属性上不存在匹配值， 但仍希望这些元组出现在结果中。

![image-20240422210114146](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422210114146.png)



![image-20240422210327634](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422210327634.png)

严格的说， 上图是左( 自然 ) 外连接， 因为它在结果中保留了左边关系的所有元组 。

类似的，右外连接，全外连接( 保留左右两个关系中的所有元组 ， 凡没有找到匹配元组的就在相应的属性中填入空 )



#### 半连接

![image-20240423143242497](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423143242497.png)

![image-20240423143400232](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423143400232.png)

![image-20240423143420605](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423143420605.png)



### 聚集运算和分组运算

![image-20240423143713254](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423143713254.png)





## 关系演算

在关系代数表达式中，一般都显式指定一个计值顺序，它隐含着执行查询的策略。在关系演算中， 不描述查询执行策略，即关系演算表达查询只说明要什么，不说明如何得到它 。

在一阶逻辑或谓词演算中， **谓词**是一个带参数的真值函数。如果将参数代入， 这个函数就会变成一个表达式， 称为**命题**， 它非真即假

如果某个谓词包含一个变量，例如 "x是一个员工"， 那么就一定有一个与 x 相关联的 **论域** ，将论域的某些值赋给x时， 命题可能为真， 而对于另一些值， 命题可能为假 。



### 元组关系演算

在元组关系演算中，我们感兴趣的是找出所有使谓词为真的元组。 这种演算是基于**元组变量**的， 元组变量是"定义于" 某个命名关系上的变量， 即该变量的论域仅局限于这个关系中的元组。



![image-20240423145017067](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423145017067.png)



![image-20240423145224148](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423145224148.png)

![image-20240423152232812](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423152232812.png)



### 域关系演算

在元组关系演算中， 使用了定义在关系上的元组变量。在域关系演算中， 同样也要用到变量， 但它的论域不再是关系中的元组， 而是属性的域 。

![image-20240423153536915](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423153536915.png)



![image-20240423153557604](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423153557604.png)

![image-20240423153624064](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240423153624064.png)







SQL 必知必会

https://forta.com/books/0135182794/

#  SQL



**数据库 vs 数据库软件**

确切地说，数据库软件应称为数据库管理系统 ( DBMS : database management system ) 数据库是通过 DBMS 创建和操纵的容器。



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





- **SQL语句** ： 由简单的英语单词组成，称为**关键字** ： 关键字不能用作表或列的名字



**注释**

```sql
SELECT 	-- This is a 注释
# This is another 注释，但有些DBMS 不支持

/*
多行注释
*/
```



用扩展的巴克斯范式( Backus Naur Form, BNF ) 定义SQL语句 ：

- 大写字母用于保留字
- 小写字母用于表示用户自定义字
- `|` 表示从选项中进行选择 ， 如 `a|b|c`
- 大括号表示所需元素， 如 `{a}`
- 中括号表示可选择元素  如`[a]`
- `...` 表示某一项可选择重复零到多次。

example : `{a|b (,c...)}` 意思是a或b后紧跟着用逗号分开的零个或多个 c





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
  - 字段 ( field ) , 基本上于列 ( column ) 的意思相同，经常互换使用
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







![image-20240310224539355](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240310224539355.png)

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

![image-20240310224607021](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240310224607021.png)







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
    -  **COUNT(column**) :  对指定列中非 NULL值的行进行计数

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



## 易犯的错误

错误提示：

消息 8120，级别 16，状态 1，第 2 行
选择列表中的列 'Qiu.dbo.students.name' 无效，因为该列没有包含在聚合函数或 GROUP BY 子句中。

解决方案：

如果 SELECT 子句 <select list> 中包含聚合函数，则 GROUP BY 将计算每个组的汇总值。指定 GROUP BY 时，选择列表中任何非聚合表达式内的每个属性名都应包含在GROUP BY列表中，或者GROUP BY表达式必须与选择列表表达式完全匹配。

错误用法：

```
SELECT name,sex,SUM(age)
  FROM [Qiu].[dbo].[students]
  group by sex
```

更正后用法：

```
SELECT name,sex,SUM(age)
  FROM [Qiu].[dbo].[students]
  group by sex,name
```

使用Group By子句的时候，一定要记住下面的一些规则：
（1）不能Group By非标量基元类型的列，如不能Group By text，image或bit类型的列
（2）Select指定的每一列都应该出现在Group By子句中，除非对这一列使用了聚合函数；
（3）进行分组前可以使用Where子句消除不满足条件的行；
（4）使用Group By子句返回的组没有特定的顺序，可以使用Order By子句指定次序。

```
use Qiu
select sex,avg(age)
from students
group by sex
```







## 挑战题

![image-20240314185845520](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240314185845520.png)

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







## SQL 数据类型

数据类型是定义列中可以存储什么数据以及该数据实际怎样存储的基本规则

- 限制可存储在列中的数据
- 更有效地存储数据，可用一种比文本字符串更简洁的格式存储数值和日期时间值。
- 数据类型允许变换排序顺序，若所有数据都作为字符串处理，则 1 位于 10 之前， 而 10 又位于 2 之前 ( 字符串以字典顺序排序， 从左侧开始比较，一次一个字符 ) 。作为数值数据类型，数值才能正确排序 。

- 即便具有相同名称的数据类型也可能代表不同的东西

### 字符串

```sql
CHAR 	# 1-255 个字符的定长字符串。它的长度必须在创建时规定
NCHAR 	# CHAR 的特殊形式用来支持多字节或 Unicode字符( 此类型的不同实现变化很大 )
NVARCHAR 	#TEXT 的特殊形式，用来支持多字节或 Unicode字符 ( 此类型的不同实现变化很大 )
TEXT ( 也称为LONG, MEMO 或VARCHAR )		#变长文本
```

- **定长列不允许多于指定的字符数目。它们的存储空间与指定的一样多 。**

  若字符串Ben存储到30个字符的字段，则存储的是 30 个字符，缺少的字符用空格填充，或根据需要补为 NULL

- 变长字符串存储任意长度的文本( 其最大长度随不同的数据类型和 DBMS 而变化) 。有些变长数据类型具有最小的定长，而有些则是完全变长的。不管是哪种，只有指定的数据得以保存( 额外的数据不保存 )

  

## 后续使用的table

![image-20240307110039367](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240307110039367.png)





###  Orders 表

orders表存储顾客订单( 不是订单细节 ) ， 每个订单唯一编号 ( order_num 列)

- 每个表都应该有主键 ，这个表应该用 order_num 作为其主键
- 为实施引用完整性，应该在 cust_id 上定义一个外键 ，关联到 Customers 的 cust_id 列



### OrderItems 表

OrderItems 表存储每个订单中的物品，每个订单的每个物品一行。对于 Orders表的每一行，在 OrderItems 表中有一行或多行。每个订单物品由**订单号**加**订单物品号**( 订单内的顺序 ,即 order_item  ) 唯一标识 。







## 表 table

某种**特定类型数据**的结构化清单( Attention: 存储在表中的数据是同一种类型的数据或清单)



**表名**

数据库名和表名等的组合，使表名成为唯一的。( 同一个数据库中不能两次使用相同表名，但不同的数据库中可以使用相同表名 )



**模式 schema**

表具有一些特性，这些特性定义了数据在表中如何存储，包括存储什么样的数据，数据如何分解，各部分信息如何命名等信息。描述表的这组信息就是**模式**

模式既可以描述数据库中特定的表，也可以描述整个数据库 ( 和其中表的关系)



**列 column**

表中的一个字段。

- **理解**： 
  - 将数据库想象成一个网格，网格中的每一列都存储着某种特定的信息。例如，在顾客表中，一列存储顾客标号，另一列存储顾客姓名 ......

- **tips : 数据分解** ： 
  - 正确地将数据分解成多个列极为重要。例如，城市、州、邮政编码总是彼此独立的列。通过分解这些数据，才有可能利用特定的列对数据进行分类和过滤。

- **数据类型 datetype**
  - 数据类型定义了列可以存储哪些数据种类。每个表列都有相应的数据类型，它限制该列中存储的数据
  - 数据类型及其名称是SQL不兼容的一个主要原因。虽然大多数基本数据类型得到了一致的支持，但许多高级的数据类型却没有。更糟的是，偶尔会有相同的数据类型在不同的DBMS 中具有不同的名称。对此用户毫无办法，重要的是在创建表结构时记住这些差异



**行 row**

表中的数据按行存储的，所保存的每个记录存储在自己的行内。例如，顾客表可以每行存储一个顾客。表中的行编号为记录的编号



**主键 primary key**

- **主键**： 一列或几列，其值能够唯一标识表中每一行。顾客表可以使用顾客标号， 其中订单表可以使用订单 ID 。

- **tips** ：虽然并不总是需要主键，但多数数据库设计者都会保证他们创建的每一个表具有一个主键，以便于以后得数据操作和管理

- **表中的任何列都可以作为主键**，只要它满足：
  - 任意两行主键值不同
  - 每一行必须具有一个主键值( 不允许为 NULL )
  - **主键列中的值不允许修改**（但并不代表某行不允许修改如删除本行）
  - 主键列值不可**重用**( 若某行从表中删除，它的主键不能赋给以后的新行)
- 在使用多列作为 primary key时 ，要求所有列值的组合必须唯一( 但其中单个列的值可以不唯一 )









# 拓展 ：ER 图 

**entity relationship diagrams** 实体关系图

摘自 https://drawio-app.com/blog/entity-relationship-diagrams-with-draw-io/

![](D:\study\database\shortcuts\1.png)



![](D:\study\database\shortcuts\2.png)

## REDs的三个组成部分



### 1.属性

**Attributes** : 组成实体的各个数据。 

- In the first style of diagram, they are drawn as circles floating around their entity. In the second style, similar to UML class diagrams, they are listed within the rectangle.

- 如果一个属性用于标识实体，则它是主键并带有下划线。如果它指的是另一个实体的标识属性，则它是外键，并用斜体表示。

- 如果不是实际存储属性，而是根据其他属性计算属性，则该属性是派生属性，并且具有虚线轮廓。

![](D:\study\database\shortcuts\3.png)



### 2.关系

- 可以用菱形表示，也可以在两个实体之间的连接器上写成文本。
- In the first style of diagram, you can see that both User and Coach write comments, and the User can perform a habit Checkin, these two ‘actions’ aren’t represented at all in the second style of diagram, which purely represents the data, not any interactions.
- Relationship connectors use Crow’s foot notation to show how many of each entity is related to another entity. For example, in the Habit Tracker app – A Coach can have 0 to many Users, but a User can only have 0 or 1 Coach. Users may have many Habits, and each Habit may belong to many users.
- 将鼠标悬停在实体关系库中的每个形状上，以查看其类型。

![4](D:\study\database\shortcuts\4.png)



### 3.实体

- These represent a collection of data, using a rectangle with attributes ‘hanging’ off it, or box containing a list of its attributes.

- 一个弱实体（显示为双矩形），因为它没有自己的主键——它只存在于它所属的实体中。
- 关联实体（在第二种类型的图中更容易看到）以虚线轮廓和连接器显示——无论在哪里有多对多关系，都需要这种类型的实体。要在第一种图表样式中创建关联实体，请添加实体形状和关系形状，并将这两个形状组合在一起。



## draw.io 使用技巧

### 连接线

- 滑动连接：绘制关系的连接线时，请确保将鼠标悬停实例上直到轮廓变为蓝色——不要将其连接到其中一个连接点。这样，当您拖动某个实例以腾出空间时，连接线将滑动到正确的位置(自动避免交叉)。
- 如果不希望连接线在实例周边滑动，可以将它们附着到固定连接点（小十字，悬停在形状上时以绿色突出显示）。



### 编辑某行

- 选择属性行，然后按Enter键编辑该行。完成后，按CTRL+Enter退出文本编辑。使用箭头键移动到下一个实体，或按CTRL+Enter（或在MacOS上按CMD+Enter）复制该实体。

   

- **Inserting entities from a text file:** You can insert entities directly from SQL code – click on **Arrange**, then **Insert**, then **Advanced**, then **From Text**. In the dialog, select **Table** from the drop down list. You’ll see example code – paste in your SQL, then click **Insert**.

















# 用函数处理数据





## 函数类型

与所有的 DBMS 都等同地支持SQL语句不同，每一个DBMS 都有特定的函数 , SQL函数不是可移植的。

![image-20240311152828277](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240311152828277.png)



大多数SQL实现支持以下类型的函数：

- 文本函数( 如删除或填充值，转换大小写 ) 
- 算数操作函数
- 日期和时间函数( 如返回两个日期之差，检查日期有效性 ) 
- 格式化函数
- 返回 DBMS 正使用的特殊信息 ( 如用户登录信息 ) 的系统函数。



## 文本处理函数

```sql
LEFT() ， RIGHT()	#返回字符串左/右边的字符
LENGTH() , DATALENGTH() ,LEN() # 返回字符串长度
LOWER() UPPER() #字符串转换小大写
LTRIM() , RTRIM() , TRIM() #去掉字符串左/右/两边的空格
SUBSTR() , SUBSTRING() # 提取字符串组成部分
SOUNDEX()  #返回字符串的 SOUNDEX 值
```



**UPPER()**

```sql
SELECT vend_name, UPPER(vend_name) AS vend_name_upcase
FROM Vendors
RODER BY vend_name;
```



**SOUNDEX()**

SOUNDEX() 是一个将任何文本串转换为描述其语音表示的字母数字模式的算法。

类似的发音字符和音节，使得能对字符串进行发音比较而不是字母比较。



**` substr`**

**` substr`** 用于提取字符串子串。

在大多数DBMS中，`SUBSTR` 函数的语法：

```sql
SUBSTR(string_expression, start, length)
```

- `string_expression` 是要提取子串的字符串表达式。
- `start` 是子串的起始位置，从 1 开始计数。
- `length` 是要提取的子串的长度。

```sql
SELECT cust_id, 
	   cust_name, 			
	   UPPER( SUBSTRING(cust_contact, 1, 2) + SUBSTRING(cust_city, 1, 3) ) 
	   AS user_login
FROM Customers;
```





## 日期和时间处理函数

日期和时间值以特殊的格式存储，以便能快速和有效地排序或过滤 ，并且节省物理存储空间。

应用程序一般不使用日期和时间的存储格式，因此日期和时间函数总是用来读取、统计和处理这些值。但日期和时间函数可移植性最差 。



SQL Server:

```sql
SELECT order_num
FROM Orders
WHERE DATEPART(yy, order_date) = 2020;
```

DATEPART() 函数有两个参数：返回的成分和从中返回成分的日期



PostgreSQL :

```sql
SELECT order_num
FROM Orders
WHERE DATE_PART('year', order_date) = 2020;
```



Oracle:

```sql
SELECT order_num
FROM Orders
WHERE EXTRACT(year FROM order_date) = 2020;
```

或使用 BETWEEN 操作符：

```sql
SELECT order_num
FROM Orders
WHERE order_date BETWEEN to_date('2020-01-01', 'yyyy-mm-dd') AND to_date('2020-12-31', 'yyyy-mm-dd');
```

Oracle 的 to_date() 函数用来将两个字符串转换为日期。

SQL Server不支持 to_date() 函数



DB2, MySQL, MariaDB , 具有各种日期处理函数，但没有 DATEPART() , 可用 YEAR() 从日期中提取year

```sql
SELECT order_num
FROM Orders
WHERE YEAR(order_date) = 2020;
```



在 SQLite 中有个技巧：

```sql
SELECT order_num
FROM Orders
WHERE strftime('%Y', order_date) = '2020';
```





## 数值处理函数

```sql
ABS()	# 返回绝对值
COS()	# 角度的余弦值
EXP()	# 返回一个数的指数值
PI()	# 返回圆周率的值
SIN()	# 正弦
SORT()	# 平方根
TAN()	# 正切
```













# 子查询

 **子查询** ( **subquery** ) ：嵌套在其他查询中的查询。

子查询常用于 WHERE 子句的 IN 操作符中，以及用来填充计算列。



## 用于IN操作符

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
```



输出：

```sql
order_num
--------
20007
20008
```



下一步查询与订单 20007 和 20008 相关的顾客 ID

```sql
SELECT cust_id
FROM Orders
WHERE order_num IN (20007, 20008);
```

 ![image-20240314214817688](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240314214817688.png)



结合这两个查询，将第一个查询( 返回订单号的那个 )变为子查询

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

- 在 SELECT 语句中 ，子查询总是从内向外处理 。
- 作为子查询的SELECT 语句只能查询单个列 ，企图检索多个列将返回错误。

- 格式化SQL：包含子查询的 SELECT 的语句难以阅读和调试，它们在较为复杂时更是如此 。把子查询分解为多行并进行适当的缩进，能极大地简化子查询的使用。



## 作为计算字段使用子查询

使用子查询的另一方法是创建计算字段

例如需要显示 Customers 表中每个顾客的订单总数 。订单与相应的顾客 ID 存储在 Orders表中。

1. 从 Customers表中检索顾客列表
2. 对于检索出的每个顾客，统计其在 Orders 表中的订单数目。



可使用SELECT COUNT(*) 对表中的行进行计数，并通过提供一条 WHERE 子句来过滤某个特定的顾客 ID, 仅对该顾客的订单进行计数。

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

- **完全限定列名**
  - 子查询中的 WHERE 子句与前面使用的 WHERE 子句稍有不同 ，因为它使用了**完全限定列名**，而不只是 列名 ( cust_id ) , 它指定 表名和 列名 ( Orders.cust_id, Customers.cust_id )
  - 用句点分隔表名和列名 ，在SELECT 语句中操作多个表，有可能混淆列名时必须使用这种语法。
- ` WHERE Orders.cust_id = Customers.cust_id` 告诉 SQL ， 比较 Orders 表中的 cust_id 和当前正从 Customers 表中检索的 cust_id



## 挑战题

![image-20240315183036922](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240315183036922.png)

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



## Problem Record

![image-20240321185426136](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240321185426136.png)

报错原因 ：一个 cust_id 可能对应多个 order_num , 因此报错 ：子查询返回的值不止一个 。

改正：

![image-20240321185849326](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240321185849326.png)

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





# 联结表

SQL最强大的功能之一就是能在数据查询的执行中 联结( join) 表。

![image-20240315224739590](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240315224739590.png)

- 同一供应商生产的每个产品 ，其供应商信息都是相同的 ，对每个产品重复此信息既浪费时间又浪费存储空间；
- 若供应商信息发生变化，只需修改一次
- 若有重复，则很难保证每次输入该数据的方式都相同。不一致的数据在报表中就很难利用。
- 关键是 ，相同的数据出现多次绝不是一件好事，这是关系数据库设计的基础 。关系表的设计就是要把信息分解成多个表，一类数据一个表 。各表通过某些共同的值互相关联( 所以才叫 关系数据库 )

- **可伸缩** ：能够适应不断增加的工作量而不失败 ，设计良好的数据库或应用程序称为可伸缩性良好( scale well )

本例可建立两个表：一个存储供应商信息，另一个存储产品信息。Vendors 表包含所有供应商信息，每个供应商占一行，具有唯一的表示( primary key) ，Products 表只存储产品信息，除了存储 供应商 ID（ Vendors表的主键） 外 ，它不存储其他有关供应商的信息 。Vendors表的主键将 Vendors 表与 Products表关联 。利用供应商 ID 从 Vendors表中找出相应供应商的详细信息 。



**联结**是一种机制：

**用来在 SELECT 语句中关联表** 。可以联结多个表返回一组输出 ，联结在运行时关联表中正确的行 

![image-20240316095038701](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240316095038701.png)

在一条 SELECT 语句中联结几个表时 ，相应的关系是在运行中构造的 。在数据库表的定义中没有指示 DBMS 如何对表进行联结 ，你必须手动定义 。



## 创建联结

**指定要联结的所有表以及关联它们的方式**

```sql
SELECT vend_name, prod_name, prod_price
FROM Vendors, Products
WHERE Vendors.vend_id = Products.vend_id
```

- FROM 子句列出了该SELECT 语句需要联结的两个表 ：Vendors 和 Products

  

- **联结中使用WHERE 子句**

  - **联结两个表时 ，实际要做的是将表一的每一行与表二的符合联结条件的行配对 。**
  - WHERE 子句作为过滤条件 ，只包含**匹配给定条件 ( 这里是联结条件 ) 的行**

  - 没有 WHERE 子句，表一的每一行与表二的每一行配对，而不管它们逻辑上是否能配在一起

    - **笛卡尔积** CARTESIAN PRODUCT

      由没有联结条件的表 返回的结果为笛卡尔积 

      ```sql
      SELECT vend_name, prod_name, prod_price
      FROM Vendors, Products;
      ```

      


## 内联结

上面使用的联结称为 **等值联结( equijoin ) ，也称为 内联结 ( inner join )**, 它基于两个表之间的相等测试 。

除上述语法外，还可以明确指定联结的类型 。具体选用哪种语法，参阅具体的 DBMS 文档 。

- **ANSI SQL 规范首选 INNER JOIN 语法**

```sql
SELECT vend_name, prod_name, prod_price
FROM Vendors
INNER JOIN Products ON Vendors.vend_id = Products.vend_id;
```



### INNER JOIN 嵌套

```sql
FROM table1 
INNER JOIN (table2 INNER JOIN (table3 INNER JOIN table4 on..) on..)on ..
```



```sql
SELECT cust_email
FROM Customers
INNER JOIN ( Orders INNER JOIN OrderItems 
				ON OrderItems.order_num = Orders.order_num) 
	ON Orders.cust_id = Customers.cust_id;
```





## 联结多个表

SQL不限制一条 SELECT 语句中可以联结的表的数目 。创建联结的基本规则也相同 。

首先列出所有表 ，然后定义表间的关系

```sql
SELECT prod_name, vend_name, prod_price, quantity
FROM OrderItems, Products, Vendors
WHERE Products.vend_id = Vendors.vend_id
AND OrderItems.prod_id = Products.prod_id
AND order_num = 20007;
```



![image-20240317222137412](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240317222137412.png)

虽然SQL本身不限制每个联结约束中表的数目，但实际上许多 DBMS 都有限制 。





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



## 挑战题

![image-20240321130325069](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240321130325069.png)

![image-20240321130340805](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240321130340805.png)

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





## 创建高级联结



### 使用表别名

why ？

- 缩短SQL语句
- 允许在一条SELECT 语句中多次使用相同的表 。

example：

```sql
SELECT cust_name, cust_contact
FROM Customers AS C, Orders AS 0, OrderItems AS OI
WHERE C.cust_id = O.cust_id
AND OI.order_num = O.order_num
AND prod_id = 'RGAN01'
```

ATTENTION : **与列别名不同，表别名不会返回到客户端，只在查询执行中使用**



### 不同类型的联结

Another three join ： 

自联结( self-join ) , 自然联结( natural join ) , 外联结( outer join )



#### self-join

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
因为名为cust_id、cust_name、cust_contact 的列各有两个。DBMS
不知道想要的是哪一列（即使它们其实是同一列）。WHERE 首先联结两个
表，然后按第二个表中的cust_contact 过滤数据，返回所需的数据。



**Tips : 用自联结而不用子查询**

自联结通常作为外部语句，用来代替从相同表中检索数据的子查询语句 。虽然最终结果相同，但许多DBMS 处理联结远比处理子查询快得多。



#### natural-join

无论何时对表进行联结，应该至少有一列不止出现在一个表中（被联结的列）。标准的联结（内联结）返回所有数据，相同的列甚至多次出现。

自然联结排除多次出现，使每一列只返回一次。

怎样完成这项工作呢？答案是，系统不完成这项工作，由你自己完成它。

一般通过对一个表使用通配符（SELECT *），而对其他表的列使用明确的子集来完成。

```sql
SELECT C.*, O.order_num, O.order_date,
OI.prod_id, OI.quantity, OI.item_price
FROM Customers AS C, Orders AS O,
OrderItems AS OI
WHERE C.cust_id = O.cust_id
AND OI.order_num = O.order_num
AND prod_id = 'RGAN01';
```

事实上，我们迄今为止建立的每个内联结都是自然联结，很可能永远都不会用到不是自然联结的内联结。



#### outer-join

- 许多联结将一个表中的行与另一个表中的行相关联，但有时候需要包含没有关联行的那些行。例如，可能需要使用联结完成以下工作：

  - 对每个顾客下的订单进行计数，包括那些至今尚未下订单的顾客；

  -  列出所有产品以及订购数量，包括没有人订购的产品；

  - 计算平均销售规模，包括那些至今尚未下订单的顾客。

在上述例子中，联结包含了那些在相关表中没有关联行的行。这种联结称为外联结。

类似内联结 ，SELECT 语句使用了关键字  `OUTER JOIN` 来指定联结类型， 而不是在 `WHERE` 子句中指定 



example

```sql
SELECT Customers.cust_id, Orders.order_num
FROM Customers
LEFT OUTER JOIN Orders ON Customers.cust_id = Orders.cust_id
```

- 在使用 `OUTER JOIN`  语法时 ，必须使用 `RIGHT` 和 `LEFT` 关键字指定包括其所有行的表 。
  - `RIGHT`  ：OUTER JOIN 右边的表
  - `LEFT`  :  OUTER JOIN 左边的表 



### 使用带聚集函数的联结

example ：

```sql
SELECT Customers.cust_id,
		COUNT(Orders.order_num) AS num_ord
FROM Customers
INNER JOIN Orders ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_id


vs
SELECT Customers.cust_id,
		COUNT(Orders.order_num) AS num_ord
FROM Customers
LEFT OUTER JOIN Orders ON Customers.cust_id = Order.cust_id
GROUP BY Customers.cust_id
#使用左外部联结来包含所有顾客，甚至包含那些没有任何订单
```

- 注意执行顺序 
  - FROM 子句获取表数据
  - INNER JOIN 子句将 Customers 和 Orders 表相互关联
  - GROUP BY 子句按顾客分组数据
  - 聚集函数 `COUNT(Orders.order_num) `计算每个顾客的订单数
  - 作为 `num_ord `返回 



# 组合查询

多数SQL 查询只包含从一个或多个表中返回数据的单条SELECT 语句。SQL 也允许执行多个查询（多条SELECT 语句），并将结果作为一个查询结果集返回

这些组合查询通常称为 union 或 复合查询( compound query 

使用组合查询的两种主要情况 ：

- 在一个查询中从不同的表返回结构数据
- 对一个表执行多个查询，按一个查询返回数据

Tips ：多数情况下，组合相同表的两个查询所完成的工作与具有多个 WHERE 子句条件的一个查询所完成的工作相同 。



## 创建组合查询



### UNION

![image-20240408122238895](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240408122238895.png)

![image-20240408122251323](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240408122251323.png)



组合：

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

- UNION 指示DBMS 执行这两条 SELECT 语句，并把输出组合成一个查询结果集 。
- 在这个简单的例子中，使用UNION 可能比使用WHERE 子句更为复杂。但对于较复杂的过滤条件，或者从多个表（而不是一个表）中检索数据的情形，使用UNION 可能会使处理更简单。



### UNION 规则

- 必须由两条及以上SELECT 语句组成 ，语句间用关键字 UNION 分隔
- UNION 中的每个查询必须包含相同的列、表达式或聚集函数( 不过各个列不需要以相同次序列出)
- 列数据类型必须兼容 ： 类型不必完全相同，但必须是 DBMS 可以隐含转换的类型

- **UNION 的列名**
  如果结合UNION 使用的SELECT 语句遇到不同的列名，那么会返回什么名字呢？比如说，如果一条语句是SELECT prod_name，而另一条语句是SELECT productname
  答案是它会返回第一个名字，举的这个例子就会返回prod_name，而不管第二个不同的名字。这也意味着你可以对第一个名字使用别名，因而返回一个你想要的名字。

  - 这种行为带来一个有意思的副作用。由于只使用第一个名字，那么想要排序也只能用这个名字。
  - 以例子说明 ：可以用 `ORDER BY prod_name` 对结果排序，如果写成`ORDER BY productname` 就会出错，
    因为查询结果里没有叫作productname 的列。

  

- **包含或取消重复的行** 

  UNION 从查询结果集中自动去除了重复的行；换句话说，它的行为与一条SELECT 语句中使用多个WHERE 子句条件一样

  这是UNION 的默认行为，如果愿意也可以改变它。

  如果想返回所有的匹配行，可使用 `UNION ALL` 而不是UNION。



- 对组合查询结果排序

  在用UNION 组合查询时，只能使用一条ORDER BY 子句，它必须位于最后一条SELECT 语句之后。

  对于结果集，不存在用一种方式排序一部分，而又用另一种方式排序另一部分的情况，因此不允许使用多条ORDER BY 子句。

  虽然ORDER BY 子句似乎只是最后一条SELECT 语句的组成部分，但实际上DBMS 将用它来排序所有SELECT 语句返回的所有结果。





# 数据插入

INSERT 用来将行插入到数据库表 。

- 插入完整的行
- 插入行的一部分
- 插入某些查询的结果



插入及系统安全 ：

使用 INSERT 语句可能需要客户端/服务器 DBMS 中特定安全权限， 在试图使用INSERT 前，应确保自己有足够的安全权限



## 插入完整的行 INSERT INTO

- 不管使用哪种INSERT 语法，VALUES 的数目都必须正确。如果不提供列名，则必须给每个表列提供一个值；如果提供列名，则必须给列出的每个列一个值。否则，就会产生一条错误消息，相应的行不能成功插入。

  

**不提供列名**

```sql
INSERT INTO Customers
VALUES(1000000006,
		'Toy Land',
		'123 Any Street',
		'New York',
		'NY',
		'11111',
		'USA',
		NULL,
		NULL);
-- 这个例子将一个新顾客插入到Customers 表中。	
```

- 存储到表中每一列的数据在VALUES 子句中给出，必须给每一列提供一个值。如果某列没有值，则应该使用NULL 值（假定表允许对该列指定空值）。

- 各列必须以它们在表定义中出现的次序填充。



**提供列名**

```sql
INSERT INTO Customers(cust_id.
                      cust_name,
                      cust_address,
                      cust_city,
                      cust_state,
                      cust_zip,
                      cust_country,
                      cust_contact,
                      cust_email)
VALUES((1000000006,
		'Toy Land',
		'123 Any Street',
		'New York',
		'NY',
		'11111',
		'USA',
		NULL,
		NULL);
```

- 不能插入同一条记录两次 。主键的值必须有唯一性，而cust_id 是主键，DBMS 不允许插入相同cust_id 值的新行。

  

  

## 插入部分行

使用INSERT 的推荐方法是明确给出表的列名。使用这种语
法，还可以省略列，这表示可以只给某些列提供值，给其他列不提供值。



省略的列需满足条件 ：

- 该列定义为允许NULL 值
- 或 ：表定义中给出默认值

若表中不允许有 NULL 值或默认值 ，这时却省略了表中的值， DBMS 就会报错，相应的行不能成功插入 。



## 插入检索出的数据 INSERT SELECT



**INSERT SELECT 插入多行**

INSERT 通常只插入一行。要插入多行，必须执行多INSERT 语句。
INSERT SELECT 是个例外，它可以用一条INSERT 插入行，不管SELECT语句返回多少行，都将被INSERT 插入。

EXAMPLE :

假如想把另一表中的顾客列合并到Customers 表中，不需要每次读取一行再将它用INSERT 插入 ：

```sql
INSERT INTO Customers(cust_id.
                      cust_name,
                      cust_address,
                      cust_city,
                      cust_state,
                      cust_zip,
                      cust_country,
                      cust_contact,
                      cust_email)

SELECT  cust_id.
        cust_name,
        cust_address,
        cust_city,
        cust_state,
        cust_zip,
        cust_country,
        cust_contact,
        cust_email
FROM CustNew; 
-- 使用INSERT SELECT 从CustNew 中将所有数据导入Customers
```

- **INSERT SELECT 中的列名**

  为简单起见，这个例子在INSERT 和SELECT 语句中使用了相同的列名。但是，不一定要求列名匹配。事实上，DBMS 一点儿也不关心SELECT返回的列名。它使用的是列的位置，因此SELECT 中的第一列（不管其列名）将用来填充表列中指定的第一列，第二列将用来填充表列中指定的第二列

- 任何 SELECT 选项和子句都可以使用， 包括 WHERE 和 GROUP BY, 也可利用联结从多个表插入数据



## 从一个表复制到另一个表

要将一个表的内容复制到一个全新的表（运行中创建的表），可以使用CREATE SELECT 语句（或者在SQL Server 里也可用SELECT INTO 语句）。

与INSERT SELECT 将数据添加到一个已经存在的表不同，CREATE SELECT 将数据复制到一个新表（有的DBMS 可以覆盖已经存在的表，这依赖于所使用的具体DBMS）。

```sql
CREATE TABLE CustCopy AS SELECT * FROM Customers

-- SQL Server :
SELECT * INTO CustCopy FROM Customers
```







# 更新和删除数据



## 更新数据 UPDATE



**三要素**

- 要更新的表；
- 列名和它们的新值；
- WHERE 指定过滤条件



**Update one col**

```sql
UPDATE Customers
SET cust_email = 'kim@thetoystore.com'
WHERE cust_id = 1000000005;
```

- 在使用UPDATE 时一定要细心。因为稍不注意，就会更新表中的所有行 ， 如此例中若不指定 cust_id , 则会修改所有用户的  email



**Update multiple cols**

```sql
UPDATE Customers
SET cust_contact = 'Sam Robers',
	cust_email = '..'
WHERE cust_id = ..
```

- 在更新多个列时，只需要使用一条SET 命令，每个“列=值”对之间用 ， 分隔 。



```sql
UPDATE Vendors
SET vend_state = (SELECT UPPER(vend_state)
					FROM Vendors AS V
					WHERE Vendors.vend_state = V.vend_state)
```

- UPDATE 语句中可以使用子查询，使得能用SELECT 语句检索出的数据更新列数据。





要删除某个列的值，可设置它为NULL（假如表定义允许NULL 值 。这与保存空字符串很不同（空字符串用''表示，是一个值），而NULL 表示没有值



## 删除数据 DELETE



**二要素** ：

列名 + WHERE 指定过滤条件

DELETE 不需要列名或通配符。DELETE 删除整行而不是删除列。要删除指定的列，请使用UPDATE 语句。

```sql
DELETE FROM Customers
WHERE cust_id = ..
```



- **外键**

  简单联结两个表只需要这两个表中的公用字段。
  也可以让DBMS 通过使用外键来严格实施关系。

  存在外键时，DBMS 使用它们实施引用完整性。例如要向Products 表中插入一个新产品，DBMS 不允许通过未知的供应商id插入它，因为vend_id 列是作为外键连接到Vendors 表的。

  那么，这与DELETE 有什么关系呢？使用外键确保引用完整性的一个好处是，DBMS 通常可以防止删除某个关系需要用到的行。例如，要从Products 表中删除一个产品，而这个产品用在OrderItems 的已有订单中，那么DELETE 语句将抛出错误并中止。这是总要定义外键的另一个理由。

  

- 删除表的内容而不是表
  DELETE 语句从表中删除行，甚至是删除表中所有行。但是，DELETE不删除表本身。

  **更快的删除**
  如果想从表中删除所有行，不要使用DELETE。可使用TRUNCATE TABLE
  语句，它完成相同的工作，而速度更快（因为不记录数据的变动）。





# 创建和操纵表



## 创建表 CREATE TABLE

**要素**

- 表定义（所有列）括在圆括号之中，各列之间用逗号分隔
- 每列的定义以列名（它在表中必须是唯一的）开始，后跟列的数据类型
- 整条语句以圆括号后的分号结束。

```sql
CREATE TABLE Products
(
	prod_id		CHAR(10)		NOT NULL,
    vend_id 	CHAR(10)		NOT NULL,
    prod_name	CHAR(254)		NOT NULL,
    prod_price	DECIMAL(8,2)	DEFAULT 1,
    prod_desc	VARCHAR(1000)	NULL
);
```



**SQL 语句中的空格。**

语句可以在一个长行上输入，也可以分成许多行，它们没有差别。前面的CREATE TABLE 语句就是SQL 语句格式化的一个好例子，代码安排在多个行上，列定义进行了恰当的缩进，更易阅读和编辑。以何种格式安排SQL 语句并没有规定，但推荐采用某种缩进格式



- **NULL 值**

  允许NULL 值的列也允许在插入行时不给出该列的值。不允许NULL 值的列不接受没有列值的行，换句话说，在插入或更新行时，该列必须有值。
  每个表列要么是NULL 列，要么是NOT NULL 列，这种状态在创建时由表的定义规定

  **多数DBMS 以 NULL 为默认值** 

  - **主键和NULL 值**

    主键是其值唯一标识表中每一行的列。只有不允许NULL值的列可作为主键，允许NULL 值的列不能作为唯一标识。



- 默认值 DEFAULT value

  默认值经常用于日期或时间戳列。例如，通过指定引用系统日期的函数或变量，将系统日期用作默认日期

![image-20240408163758057](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240408163758057.png)





## 更新表 ALTER TABLE

![image-20240408163950695](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240408163950695.png)





- 在ALTER TABLE 之后给出要更改的表名（该表必须存在，否则将出错）；
- 列出要做哪些更改

```sql
ALTER TABLE Vendors
ADD vend_phone CHAR(20)
```

![image-20240408164528595](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240408164528595.png)



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

视图是虚拟的表。与包含数据的表不一样，视图只包含检索数据的查询。

视图提供了一种封装SELECT 语句的层次，可用来简化数据处理，重新
格式化或保护基础数据。

![image-20240408212705294](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240408212705294.png)

![image-20240408212721897](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240408212721897.png)







- **视图应用** ：

  - 简化复杂的SQL 操作。在编写查询后，可以方便地重用它而不必知道其基本查询细节。

  -  使用表的一部分而不是整个表。保护数据。可以授予用户访问表的特定部分的权限，而不是整个表的访问权限。

  - 更改数据格式和表示。视图可返回与底层表的表示和格式不同的数据。

    

- 创建视图之后，可以用与表基本相同的方式使用它们。可以对视图执行SELECT 操作，过滤和排序数据，将视图联结到其他视图或表，甚至添加和更新数据（添加和更新数据存在某些限制)



- 更改表中的数据后，对应的视图将返回改变过的数据。



## 视图的规则和限制



- 与表一样，视图必须唯一命名

- 创建视图，必须具有足够的访问权限。通常由数据库管理人员授予。

- 视图可以嵌套，即可以利用从其他视图中检索数据的查询来构造视图。
  所允许的嵌套层数在不同的DBMS中有所不同（嵌套视图可能会严重降低查询的性能，因此在产品环境中使用之前，应该对其进行全面测试）。

- 许多DBMS 禁止在视图查询中使用ORDER BY 子句。

  SQL Server 报错 ：`除非另外还指定了 TOP、OFFSET 或 FOR XML，否则，ORDER BY 子句在视图、内联函数、派生表、子查询和公用表表达式中无效`

- 视图不能索引，也不能有关联的触发器或默认值。

- 



## CREATE VIEW

与 `CREATE TABLE` 一样，`CREATE VIEW`只能用于创建不存在的视图。

覆盖（或更新）视图，必须先删除它，然后再重新创建。 删除视图，可以使用DROP 语句 :  `DROP VIEW viewname;`



## 应用

**利用视图简化复杂的联结**

```sql
CREATE VIEW ProductCustomers AS
SELECT cust_name, cust_contact, prod_id
FROM Customers, Orders, OrderItems
WHERE Customers.cust_id = Orders.cust_id
AND OrderItems.order_num = Orders.order_num
```



```sql
SELECT cust_name, cust_contact
FROM ProductCustomers
WHERE prod_id = 'RGAN01';
```

从视图检索数据时如果使用了一条WHERE 子句，则两组子句（一组在视图中，另一组是传递给视图的）将自动组合。

**用视图重新格式化检索出的数据**

```sql
CREATE VIEW VendorLocations AS
SELECT RTRIM(vend_name) || ' (' || RTRIM(vend_country) || ')'
AS vend_title
FROM Vendors;
```



**用视图过滤不想要的数据**

```sql
CREATE VIEW CustomerEMailList AS
SELECT cust_id, cust_name, cust_email
FROM Customers
WHERE cust_email IS NOT NULL;
```



**使用视图与计算字段**

```sql
CREATE VIEW OrderItemsExpanded AS
SELECT order_num,
	prod_id,
	quantity,
	item_price,
	quantity*item_price AS expanded_price
FROM OrderItems
```



```sql
SELECT *
FROM OrderItemsExpanded
WHERE order_num = 20008;
```







# 存储过程

![image-20240409121444135](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409121444135.png)

可以单独编写每条SQL 语句，并根据结果有条件地执行其他语句。在每次需要这个处理时（以及每个需要它的应用中），都必须做这些工作。
也可以创建存储过程。简单来说，存储过程就是为以后使用而保存的一条或多条SQL 语句。可将其视为批文件，虽然它们的作用不仅限于批处理。

- SQLite 不支持存储过程





**意义**

由于不要求反复建立一系列处理步骤，因而保证了数据的一致性。如果所有开发人员和应用程序都使用同一存储过程，则所使用的代码都是相同的。

简化对变动的管理。如果表名、列名或业务逻辑（或别的内容）有变化，那么只需要更改存储过程的代码。使用它的人员甚至不需要知道这些变化。

![image-20240409121908657](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409121908657.png)



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



## 约束

**约束 ( constraint ) : 管理如何插入或处理数据库数据的规则**

**DBMS 通过在数据库表上施加约束来实施引用完整性。大多数约束是在表定义中定义的**

关系数据库存储分解为多个表的数据， 每个表存储相应的数据 。利用键来建立从一个表到另一个表的引用 ， 由此产生术语 ： 引用完整性( referential integrity )

正确地进行关系数据库设计， 需要一种方法保证只在表中插入合法数据 。例， 若 Orders 表中存储订单信息， OrderItems 表存储订单详细内容， 应保证 OrderItems 中引用的任何订单 ID 都存在于 Orders 中。

虽然可以在插入新行时进行检查（在另一个表上执行SELECT，以保证所有值合法并存在），但最好不要这样做，原因如下。

- 若在 客户端层面上实施数据库完整性规则， 则每个客户端都要被迫实施这些规则，一定会有一些客户端不实施这些规则 。
- 在执行UPDATE 和DELETE 操作时，也必须实施这些规则。
- 执行客户端检查是非常耗时的 ，而DBMS 执行这些检查会相对高效 。



### 主键

主键是一种特殊的约束， 用来保证一列( 或一组列 ) 中的值是唯一的， 且永不改动 。

这方便了直接或交互地处理表中的行 ， 没有主键 ， 要安全地 UPDATE 或 DELETE 特定行而不影响其他行会非常困难 。



**作为主键的列需满足的条件** 

- 任意两行的主键值都不相同且该值不允许为 NULL
- 包含主键值的列从不修改或更新。（大多数DBMS 不允许这么做）
- 主键值不能重用。如果从表中删除某一行，其主键值不分配给新行



#### 关键字PRIMARY KEY

在创建表时定义

```sql
CREATE TABLE Vendors
(
vend_id CHAR(10) NOT NULL PRIMARY KEY,
vend_name CHAR(50) NOT NULL,
vend_address CHAR(50) NULL,
vend_city CHAR(50) NULL,
vend_state CHAR(5) NULL,
vend_zip CHAR(10) NULL,
vend_country CHAR(50) NULL
);
```



#### CONSTRAINT 定义

```sql
ALTER TABLE Vendors
ADD CONSTRAINT PROMARY KEY (vend_id);
```

`CONSTRAINT` 语法可用于 `CREATE TABLE` 和 `ALTER TABLE ` 语句

- SQLite 不允许使用 ALTER TABLE 定义键 ， 要求在初始的 CREATE TABLE 语句中定义它们 。





### 外键

**外键是表中的一列 。其值必须列在另一个表的主键中 **



**外键有助防止意外删除**
除帮助保证引用完整性外，外键还可以防止意外删除。
在定义外键后，DBMS 不允许删除在另一个表中具有关联行的行。如，不能删除关联订单的顾客。删除该顾客的唯一方法是首先删除相关的订单（这表示还要删除相关的订单项）。由于需要一系列的删除，因而利用外键可以防止意外删除数据。
有的DBMS 支持称为级联删除（cascading delete）的特性。若启用，该特性在从一个表中删除行时删除所有相关的数据。例如，如果启用级联删除并且从Customers 表中删除某个顾客，则任何关联的订单行
也会被自动删除。



**定义方法 ：**

#### `REFERENCES`

```sql
CREATE TABLE Orders
(
	order_num	INTEGER		NOT NULL PRIMARY KEY,
    order_date	DATETIME	NOT NULL
    cust_id		CHAR(10)	NOT NULL REFERENCES Customers(cust_id)
)
```

`REFERENCES` 关键字表示 `cust_id` 中任何值都必须是 Customers 表的 `cust_id `中的值 。



#### `CONSTRAINT`

```sql
ALTER TABLE Orders
ADD CONSTRAINT
FOREIGN KEY (cust_id) REFERENCES Customers (cust_id)
```





### 唯一约束

唯一约束用来保证一列（或一组列）中的数据是唯一的。它们类似于主键，但存在以下重要区别

 表可包含多个唯一约束，但每个表只允许一个主键。
 唯一约束列可包含NULL 值。
 唯一约束列可修改或更新。
 唯一约束列的值可重复使用。
 与主键不一样，唯一约束不能用来定义外键。



example ：

employees 表是一个使用约束的例子。 每个雇员都有唯一的社会安全号 ，但我们并不想用它做主键 ： 因为它太长 且我们不想使该信息容易利用。

因此每个雇员除了其社会安全号外还有唯一的雇员ID（主键）。

雇员ID 是主键，可以确定它是唯一的。你可能还想使DBMS 保证每个社会安全号也是唯一的（保证输入错误不会导致使用他人号码）。可以通过在社会安全号列上定义 `UNIQUE` 约束做到。

唯一约束的语法类似于其他约束的语法。

```sql
CREATE TABLE employees(
	ID		CHAR(10)	PRIMARY KEY,
    SOCIAL_NUMBER	CHAR(50) 	UNIQUE,
    NAME		CHAR(20),
)
```



### 检查约束

检查约束用来保证一列或一组列中的数据满足指定条件。

检查约束的常见用途 ：

- 检查最小或最大值 ：。例如，防止0 个物品的订单（即使0 是合法的数）。
- 指定范围。例如，保证发货日期大于等于今天的日期，但不超过今天起一年后的日期。
- 只允许特定的值。例如，在性别字段中只允许M 或F。

数据类型限制了列中可保存的数据的类型。检查约束在数据类型内又做了进一步的限制，这些限制极其重要，可以确保插入数据库的数据正是你想要的数据。不需要依赖于客户端应用程序或用户来保证正确获取它，DBMS 本身将会拒绝任何无效的数据。



example ：

```sql
CREATE TABLE OrderItems
(
	order_num		INTEGER		NOT NULL,
    order_item		INTEGER		NOT NULL,
    prod_id			CHAR(10)	NOT NULL,
    quantity		INTEGER		NOT NULL CHECK(quantity > 0),
    item_price		MONEY		NOT NULL
)

ADD CONSTRAINT CHECK(gender LIKE '[MF]');
```



- 用户定义数据类型

  有点 DBMS 允许用户定义自己的数据类型。它们是定义检查约束(  或其他约束 ) 的基本简单数据类型。

  例如，你可以定义自己的名为gender的数据类型，它是单字符的文本数据类型，带限制其值为M 或F（对于未知值或许还允许NULL）的检查约束。。然后，可以将此数据类型用于表的定义。

  定制数据类型的优点是只需施加约束一次（在数据类型定义中），而每当使用该数据类型时，都会自动应用这些约束

  请查阅相应的DBMS 文档，看它是否支持自定义数据类型。





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



## 数据库安全

一般说来，需要保护的操作有：
 对数据库管理功能（创建表、更改或删除已存在的表等）的访问；
 对特定数据库或表的访问；
 访问的类型（只读、对特定列的访问等）；
 仅通过视图或存储过程对表进行访问；
 创建多层次的安全措施，从而允许多种基于登录的访问和控制；
 限制管理用户账号的能力。
