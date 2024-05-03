

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

![image-20240418192727258](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240418192727258.png)



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

![image-20240418193649848](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240418193649848.png)

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

Character strings data types allow you to store either fixed-length (char) or variable-length data (varchar). The text data type can store non-Unicode data in the code page of the server.



#### Character strings

##### `char[(n)]`

Fixed-size string data. *n* defines the string size in bytes and must be a value from 1 through 8,000. 

For single-byte encoding character sets such as `Latin`, the storage size is *n* bytes and the number of characters that can be stored is also *n*. For multibyte encoding character sets, the storage size is still *n* bytes but the number of characters that can be stored may be smaller than *n*. 

The ISO synonym for **char** is **character**. For more information on character sets, see [Single-Byte and Multibyte Character Sets](https://learn.microsoft.com/en-us/cpp/c-runtime-library/single-byte-and-multibyte-character-sets).



##### `varchar[(n|max)]`

Variable-size string data. Use *n* to define the string size in bytes and can be a value from 1 through 8,000, or use **max** to indicate a column constraint size up to a maximum storage of 2^31-1 bytes (2 GB)

he ISO synonyms for **varchar** are **char varying** or **character varying**.



##### Remarks

- A common misconception is to think that with **char(n)** and **varchar(n)**, the *n* defines the number of characters. 

  However, in char(n) and varchar(n), the *n* defines the string length in **bytes** (0 to 8,000). 

  *n* never defines numbers of characters that can be stored. This is similar to the definition of **nchar(n)** and **nvarchar(n)**

  The misconception happens because when using single-byte encoding, the storage size of char and varchar is *n* bytes and the number of characters is also *n*. However, for multibyte encoding such as [UTF-8](https://www.wikipedia.org/wiki/UTF-8), higher Unicode ranges (128 to 1,114,111) result in one character using two or more bytes.



- When *n* isn't specified in a data definition or variable declaration statement, the default length is 1. If *n* isn't specified when using the `CAST` and `CONVERT` functions, the default length is 30.



- If you use **char** or **varchar**, we recommend that you:
  - Use **char** when the sizes of the column data entries are consistent.
  - Use **varchar** when the sizes of the column data entries vary considerably.
  - Use **varchar(max)** when the sizes of the column data entries vary considerably, and the string length might exceed 8,000 bytes.





#### binary and varbinary



##### `binary[(n)]`

Fixed-length binary data with a length of *n* bytes, where *n* is a value from 1 through 8,000. The storage size is *n* bytes.



##### `varbinary [ ( n | max ) ]`

Variable-length binary data. *n* can be a value from 1 through 8,000. max indicates that the maximum storage size is 2^31^-1 bytes. The storage size is the actual length of the data entered + 2 bytes. The data that is entered can be 0 bytes in length.

![image-20240422194951448](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422194951448.png)



##### truncation

```sql
DECLARE @BinaryVariable2 BINARY(2);
  
SET @BinaryVariable2 = 123456;
SET @BinaryVariable2 = @BinaryVariable2 + 1;
  
SELECT CAST( @BinaryVariable2 AS INT);
GO
```









## Manage



### Create database

https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-transact-sql?view=sql-server-ver16&tabs=sqlpool

```sql
USE master;
GO

CREATE DATABASE Sales ON
(NAME = Sales_dat,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\saledat.mdf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5)
LOG ON
(NAME = Sales_log,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\salelog.ldf',
    SIZE = 5 MB,
    MAXSIZE = 25 MB,
    FILEGROWTH = 5 MB);
GO
```



#### Files and Filegroups

At a minimum, every SQL Server database has two operating system files: a data file and a log file

Data files contain data and objects such as tables, indexes, stored procedures, and views.

Log files contain the information that is required to recover all transactions in the database

Data files can be grouped together in filegroups for allocation and administration purposes.





## Operators



### UNION

Concatenates the results of two queries into a single result set. You control whether the result set includes duplicate rows:

**UNION ALL** - Includes duplicates.

**UNION** - Excludes duplicates.

```sql
{ <query_specification> | ( <query_expression> ) }   
{ UNION [ ALL ]   
  { <query_specification> | ( <query_expression> ) } 
  [ ...n ] }
```





- basic rules using **UNION**:

  - The number and the order of the columns must be the same in all queries.

  -  The definitions of the columns that are part of a UNION operation don't have to be the same, but they must be compatible through implicit conversion. 

Columns of the **xml** data type must be equal. All columns must be either typed to an XML schema or untyped. If typed, they must be typed to the same XML schema collection.

