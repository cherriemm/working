## 1.数据类型和变量

### 数据类型

#### Number  

- **JavaScript不区分整数和浮点数** 

```javascript
//特殊
NaN ; //NaN 表示 Not a Number ， 当无法计算结果时用NaN表示
Infinity ; // Infinity 表示无限大 ，当数值超过了 JavaScript 的Number
```

- JavaScript的Number不区分整数和浮点数，也就是说，`12.00 === 12`。（在大多数其他语言中，整数和浮点数不能直接比较）并且，JavaScript的整数最大范围不是±263，而是±253，因此，超过253的整数就可能无法精确表示

```javascript
console.log(Number.MAX_SAFE_INTEGER) ;
//9007199254740991
```



#### 字符串  

- **以单引号或双引号括起来的任意文本**

#### 布尔值

 true , false



**(1)   JavaScript的比较运算符** 

1.  == 比较 

   会自动转换数据类型再比较，很多时候会的到非常诡异的结果

2.  === 比较

   不会自动转换数据类型，如果数据类型不一致，返回 false , 如果一致再比较

   **!!!!! 始终使用 === 比较**

  **(2)  NaN**

​	NaN这个特殊的Number与所有其他值都不相等 ，包括它自己

```javascript
NaN === NaN // false

// 唯一能判断 NaN的办法是通过 isNaN
isNaN(NaN) // true 
```

  **(3) 浮点数的相等比较**

 	`1/3 === (1-2/3);    // false`

- ​	浮点数再运算过程会产生误差，因为计算机无法精    确表示无限循环小数 ，要比较两  个浮点数是否相等，   智能计算它们之差的绝对值 ，看是否小于某个阈值

```javascript
Math.abs(1/3 - (1-2/3))<0.0000001 ; // true 
```



#### null和undefined

- `null`表示一个“空”的值，它和`0`以及空字符串`''`不同，`0`是一个数值，`''`表示长度为0的字符串，而`null`表示“空”。

#### 数组

- 数组是一组按顺序排列的集合，集合的每个值称为元素。JavaScript的数组可以包括任意数据类型

```javascript
[1,2,3,'hello',null,true] ;
```

- 另一种创建数组的方式是通过 Array() 函数实现

```javascript
 new Array(1,2,3) ;
```



#### 对象

```javascript
var person = {
    name : 'Bob' ,
    age : 20 ,
    tags : ['js','web','mobile'] ,
    city : 'Beijing' ,
    hasCar : true ,
    zipcode : null 
} ;
```

- **JavaScript对象的键都是字符串类型，值可以是任意数据类型**

- **要获取一个对象的属性，我们用`对象变量.属性名`的方式：**



### 变量

-  申明一个变量用 var 语句 ，变量名是大小写英文，数字 ，$ 和 _的组合，不能用数字开头

- **JavaScript是动态语言** ：在JavaScript中，使用 = 对变量进行赋值 ，可以把任意数据类型赋值给变量 ，**同一个变量可以反复赋值，且可以是不同数据类型**



### JavaScript 对象

- JavaScript对象是一种无序的集合数据类型，它由若干键值对组成，以名称和值对的形式 (name : value) 

```javascript
var xiaoming = {
    name : '小明' ,
    birth : 1990 ,
    school : 'No.1 Middle School' ,
    height : 1.70 ,
    weight ；65 ,
    score : null 
} ;
```

- 对象由花括号分隔。属性由逗号分隔.注意，最后一个键值对不需要在末尾加`,`，如果加了，有的浏览器（如低版本的IE）将报错。



## 2.函数定义和调用

### 1.定义函数

```javascript
function abs(x){
	if(x>=0){
        return x ;
	} else {
        return  -x ;
    }
}

```

- function 指出这是一个函数定义
- abs是函数名称
- (x) 括号内列出函数的参数，多个参数以 ， 分隔

- 函数体内部的语句在执行时，一旦执行到`return`时，函数就执行完毕，并将结果返回

**如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`undefined`。**

**！！！！！**

由于JavaScript的函数也是一个对象，上述定义的abs()函数本质上是一个函数对象，而函数名abs可以视为指向该函数的变量。

因此 ，第二种定义函数的方式

```javascript
var abs = function(x) {
    //函数体
} ;
```

 此时 function(x) 是一个匿名函数，它没有函数名，但是这个匿名函数赋值给了变量abs ，故通过变量abs 就可以调用该函数 

注意第二种方式按照完整语法需要在函数体末尾加一个 ； 表示赋值语句结束

### 2.调用函数



调用函数时，按顺序传入参数即可：

```
abs(10); // 返回10
abs(-9); // 返回9
```

由于JavaScript允许传入任意个参数而不影响调用，因此传入的参数比定义的参数多也没有问题，虽然函数内部并不需要这些参数：

```
abs(10, 'blablabla'); // 返回10
abs(-9, 'haha', 'hehe', null); // 返回9
```

传入的参数比定义的少也没有问题：

```
abs(); // 返回NaN
```

此时`abs(x)`函数的参数`x`将收到`undefined`，计算结果为`NaN`。

要避免收到`undefined`，可以对参数进行检查：

```
function abs(x) {
    if (typeof x !== 'number') {
        throw 'Not a number';
    }
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```





## 



# JavaScript 函数

------

函数是由事件驱动的或者当它被调用时执行的可重复使用的代码块。



```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>测试实例</title>
<script>
function myFunction()
{
    alert("Hello World!");
}
</script>
</head>
 
<body>
<button onclick="myFunction()">点我</button>
</body>
</html>
```





------

## JavaScript 函数语法

函数就是包裹在花括号中的代码块，前面使用了关键词 function：

function functionname()
{
  *// 执行代码*
}

当调用该函数时，会执行函数内的代码。

可以在某事件发生时直接调用函数（比如当用户点击按钮时），并且可由 JavaScript 在任何位置进行调用。

| ![lamp](https://www.runoob.com/images/lamp.jpg) | JavaScript 对大小写敏感。关键词 function 必须是小写的，并且必须以与函数名称相同的大小写来调用函数。 |
| ----------------------------------------------- | ------------------------------------------------------------ |
|                                                 |                                                              |





## 局部 JavaScript 变量

在 JavaScript 函数内部声明的变量（使用 var）是*局部*变量，所以只能在函数内部访问它。（该变量的作用域是局部的）。

您可以在不同的函数中使用名称相同的局部变量，因为只有声明过该变量的函数才能识别出该变量。

只要函数运行完毕，本地变量就会被删除。

------

## 全局 JavaScript 变量

在函数外声明的变量是*全局*变量，网页上的所有脚本和函数都能访问它。

------

## JavaScript 变量的生存期

JavaScript 变量的生命期从它们被声明的时间开始。

局部变量会在函数运行以后被删除。

全局变量会在页面关闭后被删除。

------

## 向未声明的 JavaScript 变量分配值

如果您把值赋给尚未声明的变量，该变量将被自动作为 window 的一个属性。

这条语句：

carname="Volvo";

将声明 window 的一个属性 carname。



## 浏览器对象



### 1.window对象

`window`对象不但充当全局作用域，而且表示浏览器窗口。

### 2.document 

`document`对象表示当前页面。由于HTML在浏览器中以DOM形式表示为树形结构，`document`对象就是整个DOM树的根节点。

`document`的`title`属性是从HTML文档中的`<title>xxx</title>`读取的，但是可以动态改变：
