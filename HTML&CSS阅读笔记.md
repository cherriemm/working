# chapter1 web语言

## 1.html语言

- 首部包含< head >  和 < /head > 标记及它们之间的所有内容。主体包含 < body > < /body > 标记及它们之间的所有内容。**编写html要把首部和页面主体分开**
  - < head >  和 < /head > head首部包含web页面的有关信息 ，head标记中放入title标记，title总出现在浏览器窗口的顶部
  - < body > < /body > 页面主体

- 元素由包围内容的标记和标记之间的内容组成

- **一定要以 `<!DOCTYPE html>`开头**，告诉浏览器你使用的html版本，**HTML标准现在是一个活的标准，这说明这个标准会不断改变，加入新的特性和更新**
  - `<html>`元素：**`<html>`元素必须是web页面的最顶层元素或根元素**。在doctype以 `<html>`元素开始你的页面
  - 在`<head>`中包含`<meta charset="utf-8">`标记，指定正确的字符编码 (**`<meta>`标记告诉浏览器关于web页面的额外信息，如内容类型和类型)**
  - 一定要在`<head>`中包含一个`<title>`元素
  - `<img>`的 alt标签是必要的

- 元素的属性 ？   通过属性，可以提供一个元素的附加信息



## 2.CSS语言

HTML提供了一种方法来描述文件中内容的结构。浏览器显示HTML时，它会使用自己内置的默认样式来表现这个结构  ===>   CSS ，层叠样式表 ，cascading style sheets .

### 认识style元素

需要在页面增加一个新的element ，即 < style > 元素 

- < style> 元素 放在HTML的首部里 

- < style >标记还有一个可选的属性 type ，它可以告诉浏览器你正在使用什么类型的样式，由于要使用css ，可以制定 "text/css" 属性

  ```html
  <html>
      <head>
          <title>Starbuzz Coffee</title>
          <style type="text/css">
          <!-- 此处定义页面的样式 -->
              body{
                  background-color: #d2b48c ;
                  margin-left: 20% ;
                  margin-right: 20% ;
                  border: 2px dotted black ;
                  padding: 10px 10px 10px 10px ;
                  font-family:sans-serif ;
              }
           <!-- 此处css中的body是什么意思 ？ 表示css应用于body标签中的内容-->
              
          </style>
      </head>
      
      
      <body>
          <h1>Starbuzz Coffee Beverages </h1>
  		<h2>House Blend,$1.49</h2>
          <p>A smooth,mild blend of coffees from Mexico,Bolivia, and Guatemala</p>
      </body>
  </html>
  ```

  





# chapter 3 web页面建设

- **< q > < /q > 短引用标签**

  < blockquote > < /blockquote> 用于较长的引用，需要单独显示 。

  **< q >  与 < blockquote >的本质区别**

    	< q >是一个内联元素 (inline) , 而< blockquote > 是一个块元素(block) ,块元素显示时就好像前后各有一个换行符 ，而内联元素在页面文本流中总在行内出现

  **< h1 >< h2 >...< h6 >< p >< blockquote >	都是块元素 ， < q > < a > 是内联元素**

  ​	**块元素通常用作web页面中的主要构建模块 ，而内联元素往往用来标记小段内容。设计一个页面时，通常先从较大的块开始 ，再在完善页面时加入内联元素**

- **void元素没有结束标记**

​			**< br >** 

​			浏览器不会显示空白和换行，除非把每一行放在一个块元素里，比如<p>，否则如何显示行呢？ 

​			< br >标签

​			< br >是一个 void元素 ，类似的还有 < img > 元素 



- **列表** **< li >**

  创建一个列表需要两个元素 ：

  1. 标记每个列表项
  2. 确定你创建的是哪种类型的列表 ：有序or无序

  STEP 1 将每个列表项放在一个 < li >元素中

  STEP 2 用 < ol >或 < ul > 元素包围列表项 。

  ```html
  <p>
      ...
  </p>
  <ol>
      <li>a</li>
  	<li>b</li>
  	<li>c</li>
  </ol>
  <p>
      ...
  </p>
  ```

  ​	ol : ordered list 

  ​	ul :unordered list

  ​	li : list item 

  ​	**< ol > 和 < li > 都是块元素** ，< ol > 和 < li > 总是要一起用才有意义，这些元素离开彼此没有意义 ，列表实际上就是一组列表项， < li >用来标识每个元素 ， < ol >用于把它们归为一组 。



- 对应特殊字符的字符实体

  <字符的缩写是  `&lt;`  ,     > 字符的缩写是 `&gt;`

  输入`&lt;html&gt; element rocks`

  

# chapter 4 < a >元素

- < a >元素用于创建**指向另一个页面的链接**，< a >元素的内容就是链接文本。在浏览器中链接文本会显示有下划线，指示这是可单击的
  - 通过**href属性**来制定链接的目标文件(  **属性 Attributes的写法**：属性名 =" 属性值 " )

- 将< img >元素放在 < a >标记之间，这样图像就会像文本一样可单击 。

## 链接页面的两种方式

**相对路径和URL**

相对路径只用来链接同一网站内的页面 ，而 URL 通常用来连接其它网站 。

**思考** ：**为什么不全部使用URL**？

如果需要更改web服务器名，使用相对链接来链接同一网站内的页面的方便 。

```
## file协议

file:///D:/study/js/Head-First-HTML-master/chapter4/starbuzz-complete/index.html

浏览器从你的计算机本地读取文件时会使用file协议 ，
```

### (1) 相对路径

相对路径是**相对于源web页面**到**网站中其它文件**的路径 

- **相对路径** ：可能要下行或上行一两个文件夹，最后得到一个可以放在href中的相对路径 。

  - **下行** ：进入子文件夹 href = " 子文件夹名/文件名 "
  - **上行** ：**..**   移至上一级文件夹 ，若向上移动两级  ../.. 注意需要用 / 分隔每一部分 。 href = " ../文件名 "
  - 若只有文件名则表示在同一文件夹下 

- 对于网页 ，只能使用 /作为分隔符 (windows操作系统使用 \ 作为文件分隔符 )

  

### (2) 绝对路径

#### URL 

**统一资源定位符 Uniform Resource Locator** 

一个全局地址，可以用来定位web上的任意资源，包括html页面、音频、视频和很多其他形式的web内容

![image-20231213201254364](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231213201254364.png)





![image-20231213203623928](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231213203623928.png)



![full URL](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL/mdn-url-all.png)

scheme (方案) 协议

 Domain Name :域名表示所请求的网络服务器。通常是域名，但也可以使用 IP 地址（但这种情况很少见，因为不太方便)

 Path to the file : 在网络发展初期，这样的路径代表网络服务器上的物理文件位置。如今，它主要是网络服务器处理的一个抽象概念，没有任何实际意义。

#### 绝对路径

绝对路径就是在协议和网站名之后的最后一部分，绝对路径告诉服务器如何从你的根文件夹到达某个特定的页面或页面。

**用 / 表示根** 

![image-20231214090909148](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231214090909148.png)

- ​	可以在< a > 元素的href属性中放入相对路径，既然它们不是绝对路径 ，服务器是怎么找到的呢 ？
  - 单击一个相对链接时，在后台浏览器会根据这个相对路径和所单击页面的路径创建一个绝对路径

**当浏览器web服务器请求一个目录而不是一个文件**

```
如浏览器请求  http://www.starbuzzcoffee.com/images/  根目录中的images目录 
或 
http://www.starbuzzcoffee.com/ 根目录本身
```

web浏览器接收到一个类似这样的请求时，它会尝试查找这个目录中的一个默认文件。 通常默认文件名为 index.html 或default.htm ,如果服务器找到这样一个文件 ，就会把它返回给浏览器显示 。

**要从根目录(或其他任何目录)默认地返回一个文件 ，只需要把这个文件命名为 index.html 或 default.htm**

ps ：if请求 http://www.starbuzzcoffee.com 末尾没有 / 

**若服务器接收到一个末尾没有 / 的请求 ，且这个目录确实存在 ，服务器就会帮你加上末尾的斜线**

![image-20231214102056175](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231214102056175.png)



​    默认文件名取决于你的托管公司使用哪种web服务器 (index.html , default.htm , index.php )







## < a > 的title属性

可以为< a > 增加title属性以便访问 ,标题会显示为一个**工具提示**

```html
<p>
    Read the <a href="http://wickedlysmart.com/buzz" title="Read all about caffeine on the Buzz">Caffeine Buzz</a>
</p>
```





## < a > 的id属性

**允许访问页面中的一个特定点**

只要链接到另一个页面 ，浏览器就会加载整个页面，并从头开始显示 ，若希望能直接链接到页面的某个特定位置  则需要 < a > 的id属性



**使用id属性为 < a > 创建锚点** 

1.找到页面中你希望创建锚点的位置 ，这可以是页面上的任何文本 ， 不过通常是标题

2.为目标选择一个标识符名(id名) ，在元素的开始标记中插入id属性

```html
<h2 id="chai">
    Chai Tea , $1.85
</h2>
<!--
为标题的开始标记增加id ，id必须是唯一的
-->
```



### 如何使用id链接到元素

不论是相对链接还是URL , 要**链接到页面中的一个特定目标**，只需要在链接最后加上一个 **#** ,再加上id名。

**interesting questions**

- **能不能链接到一个链接，也就是在目标中为一个 < a > 元素增加id属性 ？**

  yes ， `<a href = "  " id = "  "> ... </a >`

-  **可以在文档中放置一个指向相同文档中某个目标的链接吗？**

  yes , 此时**URL为空**即可 。实际上，通常会在页面最上面定义一个目标 top ，并在页面最下面定义一个目标back to top 。在长文档中，往往会有**整个页面的一个目录** 。例如 ，要链接到同一个页面上的 top 目标 ，`<a href = "#top">Back to top </a>`

- **为什么需要为URL 增加 /index/html 来创建指向目标标题的链接呢？为什么不能直接写为 http://wickedlysmart.com/buzz#Coffee ?**

  No ，这不一定能正常工作 。因为浏览器会帮你在URL 末尾加斜线 ，这样可能取代id引用 ，不过你可以这样写：

  `http://wickedlysmart.com.buzz/#Coffee`如果你不知道默认文件是否是 index.html ，这就会很方便

- **如果一个web页面没有提供一个目标 ，但我还需要链接到页面的某个特定部分，该怎么做呢 ？**

  这是办不到的，如果没有目标 (没有带id的元素) 就无法指示浏览器前往web页面中的一个特定位置 ，你可能需要联系页面作者，让他们增加这样一个目标 。

- < a > 元素能够由文字和图像(内联内容) 创建链接 ，还可以从块元素(如 < p > 和 < blockquote >) 创建链接 



## < a > 的target属性

可以为< a > 元素增加一个target属性 ，告诉浏览器使用一个不同的窗口 。target属性值会告诉浏览器页面的目标窗口 。

`<a target="_blank" href="http://wickedlysmart.com/buzz" title="Read all about caffeine on the Buzz"> Caffeine Buzz </a>`

**Q : 我得到了一个新的标签页 ，而不是新窗口 ？**

A ：大多数浏览器现在都有一个默认设置 ，会在一个标签页中打开新窗口 ，不过新的标签页和新窗口实际上是一样的，只是标签页可以共享原窗口的窗口边框 。



- 不一定要把target指定为 _ blank , 如果指定另外一个名字 (任意设定) ，那么**有相同目标名的所有链接都会在同一个窗口中打开** ，因为**为target指定一个特定的名字时实际上就是在对链接页面的新窗口命名** 。**_ blank则是一种特殊情况，告诉浏览器总是使用一个新窗口**



## < a >元素的样式

- 未访问过的链接默认是蓝色的
- 访问过的链接默认为紫色
- 当把鼠标悬停在一个链接上方，会得到工具提示，显示title属性的值 



### 如何对链接指定样式

```css
a:link{
    color : green ;
}/*应用于未访问状态的链接*/
a:visited{
    color : red ;
}/*应用于已访问状态的链接*/
a:hover{
    color :yellow ;
}/*应用于悬停状态的链接*/
```

**另外两种状态：focus 和active**

- **focus** ：浏览器将焦点放在你的链接上时就是焦点(focus状态) 。

有些浏览器允许按下tab键来轮流访问页面上的所有链接。浏览器访问到某个链接时，这个链接就拥有 "焦点" 。

设置一个**焦点伪类值**对于提高可访问性很有帮助，因为需要使用键盘(而不是鼠标) 来访问链接的人会知道他们何时选择到正确的链接 。



- **active** ：用户第一次单击一个链接时，就处于活动(active状态)



ps ：链接可能同时处于多种状态，需要按规则的顺序来确定应用那个样式，所以一般认为适当的顺序是 link , visited ,hover ,focus ,active 。





# chapter 5 为你的页面增加图像 



## 浏览器如何处理图像

- 浏览器对 < img >元素的处理与其他元素稍由不同 ，以 < h1 > 或 < p >元素为例，浏览器在页面上看到这些标记时，只需要把它们显示出来就可以了，不过对 < img > ,浏览器在显示图像之前 ，必须先获取这个图像

获取和现实页面的过程

1. 浏览器从服务器获取文件 elixir.html
2. 浏览器读取 elixir.html文件 ，显示这个文件，发现其中有4个图像需要获取，所以它需要从web服务器逐个得到这些图像
3. 获取到 green.jpg后 ，浏览器显示这个图像，然后转向下一个图像
4. 重复

## jpeg , png ,gif 的区别 ？

### 1.JPEG ：照片和复杂图像使用JPEG

- 最适合连续色调图像，如照片 
- 这是一种有损格式，因为缩小文件大小时会丢掉图像的一些信息
- 不支持透明度
- 文件比较小 ，以便web页面更高效的显示
- 不支持动画

### 2.PNG ：单色图像和线条构成的图像 

如 logo ，剪贴画和图像中的小文本

- PNG可以包含上百万中不同颜色的图像 ，PNG有三种 ，PNG-8 , PNG-24 ,PNG-32 
- PNG会压缩文件来缩小文件大小，不过不会丢掉信息 ，这是一种无损格式 
- 允许将颜色设置为透明 ，使图像下面的东西可以显示出来 
- 与相应的JPEG文件相比 ，PNG文件更大一些



### 3.GIF  

- GIF最大可以表示256中不同颜色的图像
- GIF也是一种无损格式
- GIF也支持透明度，不过只允许一种颜色设置为透明
- 支持动画



## < img >



` img src="imags/drinks.gif"> `

- `<img>` 元素是一个内联元素，它不会再前面和后面插入换行
- `<src>` 属性指定了在web页面上显示的文本文件的位置
- `<img>`是一个void元素

!!!!!!!!!!!!!

< img >元素只是指向图像，图像并不是HTML页面本身的一部分，实际上，浏览器显示页面时，图像会取代 < img > 元素 。HTML页面是纯文本，所以图像绝对无法直接作为页面的一部分 ，它是单独存在的 。

### alt属性 ：提供候选格式 alternative 

`<img>` 元素的alt属性为访问者提供一些指示 ，告诉他们图像里有什么信息。

`<img src="http://wickedlysmart.com/hfhtmlcss/trivia/pencil.png"  alt="The typical new pencil can draw a line 35 miles long.">`

alt 属性需要指定描述这个图像的一些文本 ，**如果图像未能显示 ，就会用这个文本来取代它 。**



### width 和 height ：调整图像大小

很多浏览器上，如果在HTML中提供了width 和height ，浏览器在显示图像之前就可以开始建立页面布局，如果没有指定，则浏览器在知道了图像的大小之后，通常需要重新调整页面布局 。要记住 ，**浏览器是在下载了HTML文件并开始显示页面之后才下载图像 ，浏览器下载图像之前，除非你告诉它，否则它无法知道图像的大小 。**

需要按与原尺寸不同的大小显示一个现有图像时 ，很多人都会这么做，不过最好不要使用width和height来达到这个目的

### 使用缩略图

将每个照片替换为一个更小的缩略图，然后创建从这个缩略图到各个更大照片的链接

1.图片可能会并排显示

 由于 `<img>`是内联元素 ，所以显示元素时不会在元素前后插入换行 。因此HTML有多个图像，浏览器窗口足够宽时，浏览器会把它们并排摆放 。

2.链接到图像

```html
<a href="html/applestore.html" target="_blank" alt="An ipod at the Birmingham Apple store">
     <img src="thumbnails/applestore.jpg"><br>
</a>
```



### 使用logo

**.psd** 格式？

.psd 表示这个文件是以Photoshop格式保存的 ，

柔化文本边缘 ，背景色蒙版(反锯齿处理)











# chapter 7 css入门

css (cascading style sheets )：层叠样式表

## 层叠的含义 ？

**样式表的类型 ：** 

**1.**作者为页面写的所有样式表 	

**2.**有些浏览器允许用户为HTML元素创建自己的样式(如果读者在一个属性声明的最后加上 !important , 就能覆盖作者的样式) ，	

```css
h1{
    font-size:200% 
    !important ;
}
```

 

**3.**浏览器本身会维护一组默认样式，如果作者没有为一个元素定义样式，就会使用默认样式 ，如果根本没有任何作者和读者样式表，也会使用这些样式 。

优先级 ：作者 > 读者 > 默认



### 确定属性值的过程



假设页面有一个 <h1>元素，想知道这个元素的font-size 属性

**Step1 : 收集所有样式表**



**Step2 : 找到所有匹配的声明**

查看所有可能选择<h1>元素的选择器的font-size 声明。检查所有样式表，找出所有匹配<h1>而且有font-size 属性的规则



**Step3 : 对所有匹配的规则排序**

按作者、读者、浏览器默认样式的顺序对这些规则排序(读者可能在他的css属性上加上 !important，此时读者属性最优先 )



**Step4 : 按特定性对所有声明排序**

**完成特定性排序时，不会对所有规则重排，只会在各个类别中按特定性排序。对于特定性相同的元素，则根据样式表中的顺序再次进行排序**

如果一个规则能更准确地选择一个元素，那么这个规则就更特定

example : 子孙选择器 " blockquote h1" 就比"h1" 选择器更为特定，因为前者只选择<blockquote>中的<h1>



**Step5 : 对于冲突的规则，按照它们在各自样式表中出现的顺序进行排序。**

现在只需要对冲突的规则排序，各个样式表中后出现的规则更重要。因此，如果在样式表中增加一个新规则，它会覆盖在它之前的所有规则 。



- 计算特定性

  ![image-20231228110546523](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228110546523.png)





example

![image-20231228110919033](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228110919033.png)



**如果经过这些步骤还是没有找到包含特定属性声明的规则 ？**

- 如果在层叠的所有规则中都没有找到匹配的属性，就要使用**继承**了。并不是所有属性都能继承(比如border属性) ，对于能继承的属性(color，font-family , line-height ...) ，浏览器会查看这个元素的祖先，先从它的父元素开始，尝试找到这个属性的值。





![image-20231215185300203](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215185300203.png)

```css
p{
	background-color : red ;
	border : 1px solid gray ; 粗细为一像素的边框，灰色，实线
}
```

`color` 与 `background-color` 区分 ：color是字体颜色，background-color是背景颜色 。

## 将css放入html中

1. `<style>`元素
2. 建立单独的css文件



合并：要为多个元素编写一个规则，只需要在选择器之间加上逗号

```css
h1{
    font-family :sans-serif ;
    color :gray ;
}
h1{
    font-family :sans-serif ;
    color :gray ;
}

等价于
h1,h2{
    font-family :sans-serif ;
    color :gray ;
}
```



合并项中的特殊属性

```css
h1,h2{
    font-family: sans-serif ;
    color: gray ;
}
h1{
    border-bottom :1px solid black ;
}
```

增加一个规则，只为`<h1>`增加另一个属性 。

**把元素所有的共同样式归组在一起，然后把一个元素特定的样式写在另一个规则中 。**(好处？ 若把共同的样式合并在一起，倘若它们有改变，只需要在一个规则中修改，若分开则必须修改多个规则)



## css选择器

![image-20231215191716478](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215191716478.png)

![image-20231215191725121](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215191725121.png)

![image-20231215191734390](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215191734390.png)





**1.元素选择器 ( Element Selector)** ：通过元素名称选择HTML元素 

​		`p{color:blue} `  p选择器将选择所有的<p>元素 ，



**2.类选择器 (Class Selector)** ：**.class** 选择器用于选择具有指定类别(class) 属性的HTML元素，通过在css规则中使用 .class , 可以将样式应用于具有相同类别的多个元素 。

HTML

```html
<p class="highlight">
    this is a paragraph with class highlight
</p>
<p>
    this is a normal paragraph .
</p>
<p class="highlight">
    this is another paragraph with class highlight .
</p>
```

css

```css
.highlight{
    color : red ;
    font-weight : bold ;
}
```

.highlight 类别被应用于两个<p>元素 ，通过使用 .highlight 选择器 ，可以选择所有带有该类别的元素，并将样式应用于它们 。

(意义：可以单独选中一个或几个段落)

more : element.class 选择器  ：结合元素选择器和类选择器 



**3.ID选择器(ID Selector)** :通过元素的唯一标识符ID选择HTML元素 ，ID选择器以#开头，后面跟着ID名称

`#footer{color:red }` 选择id为footer的任意元素



**id属性**

- **类和id 命名规则**

​	类名要以字母开头，id名可以以数字或字母开头 ，id名和类名都可以包含数字、字母、下划线 ，但不能有空格 。

- 在一组复杂的页面中，可能出现：有些页面将这个id指定给一个段落，而在另外一些页面上可能会把这个id分配给一个 <li>或<blockquote> ，所以可能需要为这个id制定多个规则，根据页面上不同类型的元素应用不同的规则，如 p#someid 和 blockquote#someid (why ？一个网站可能有多个页面，而多个页面链接到同一个css文件)

- **类 or id**

多个元素重用某些样式才能真正发挥类的作用，如果只有一个元素需要指定样式，这种情况下使用类就有些大材小用了 。



example：

所有页面都只有一个页脚，所以可以为包含页脚文本的<p>增加id footer 

```html
<p id="footer"> Please steal this page , it isn't copyrighted in any way </p>
```





**4.属性选择器 (Attribute Selector)** 通过属性值来选择元素

```css
img[width]{
    border: black thin soli;
} /* 该选择器选择HTML中所有包含一个width属性的图像 */
img[height ="300"]{
    border: red thin solid;
}  /* 该选择器选择HTML中所有height属性值为300的图像 */
image[alt~="flowers"]{
    border :#ccc thin solid;
}/* 该选择器选择alt属性包含单词flowers的图像 */
```



**5.后代选择器 (Descendant Selector)** :通过指定元素的后代关系选择HTML元素 。

```css
div p{
    font-weight :bold ;
}
```

div p 选择器将选择所有在 < div > 元素内的 < p > 元素。



6.兄弟选择器 ：

假设你希望只选择前面有一个 <h1> 元素的段落 ，可以使用下面这个选择器

```css
h1+p{
	font-style:			italic;
}
/* 选择所有紧跟在一个<h1>元素后面的段落 */
```





## 创建css文件

**在HTML文件中创建外部链接链接到css文件**



**`<link>`元素**

不再需要`<style> </style>`

```html
<link type="text/css" rel="stylesheet" href="lounge.css">

<!--
1.使用link元素链入外部信息
2.这个信息的类型是 text/css ,即这是一个css样式表，在HTML5中，不再需要这个属性 ，不过你可能在比较老的页面上看到它 。
3.rel属性 ：rel属性指定了HTML文件与所链接的文件之间的关系，我们要链接到一个样式表，所以这里使用值 stylesheet
4.样式表放在href中，相对链接和完整的URL都可以
5.<link>是一个void元素 ，它没有结束标记
-->
```

![image-20231215193308997](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215193308997.png)



## 继承

为`<p>`选择器增加 font-family 属性时，也会影响到`<p>`元素中内部元素的字体

![image-20231215194746449](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215194746449.png)



![image-20231215194855040](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215194855040.png)



**覆盖继承**

要覆盖从body继承的 font-family 属性，可以增加一个新规则选择 em 将font-family 属性值设置为 serif

```html
em{
	font-family :serif 
}
```



css注释 ： /*  ....  */

html 注释 <!--     -->

## 创建类 class属性

如何单独的选择段落？

1.为**HTML中的元素**增加一个**class属性**，这样就会**把这个元素增加到这个类中**

2.在css中选择这个类

![image-20231215200940383](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215200940383.png)



**在css中创建一个类选择器**

![image-20231215200856532](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215200856532.png)

![image-20231215201249803](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215201249803.png)







**！！！！！！！！！！！**

![image-20231215201325576](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215201325576.png)

一个元素可以属于多个类 ，把各个类名放在class属性中 ，各个类名之间用一个空格分隔 ，类名的顺序并不重要

**若你希望一个元素拥有不同类中定义的不同样式，就要使用多个类**

![image-20231215201930818](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215201930818.png)

- 通过为你想改变的元素创建一个更特定的规则，能覆盖该元素继承的属性
- 使用class属性将元素增加到一个类
- 通过在元素名和类名之间加一个 .  可以选择该类中的一个特定元素
- 使用 .classname 可以选择属性这个类的所有元素
- 通过在class属性中放入多个类名，可以指定一个元素属于多个类，类名之间用空格分隔





# chatper8 more css

## 字体的相关属性 

**font-family , font-style , font-weight , font-size ,font-variant , line-weight ;**

**字体的简写**

![image-20231227211555809](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227211555809.png)

![image-20231227211717288](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227211717288.png)











### 1.font-family：页面中的字体

**每个font-family 包含一组有共同特征的字体**，一共有5个字体**系列**：sans-serif , serif , monospace , cursive , fantasy .**每个字体系列都包括大量字体**

![image-20231215205622904](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215205622904.png)

serif 字体系列包括有衬线的字体 。衬线是字母末端的装饰性小细线



![image-20231215205809639](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215205809639.png)



![image-20231215205848380](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215205848380.png)



![image-20231215205908802](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215205908802.png)





![image-20231215210059247](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215210059247.png)

#### web字体 ：web font

**css 的 @font-face 规则** 

该规则允许你定义一种字体的名字和位置，然后可以在你的页面中使用 。

![image-20231215212025411](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215212025411.png)

1.浏览器首先获取一个引用这些字体的HTML页面

2.浏览器再获取这个页面所需的web字体文件

3.浏览器显示这个页面使用该字体



**woff : web open font format    web开放字体格式**



**如何为页面增加web字体**

1. 找到一个字体

2. 确保有所需字体的所有格式

   (1)  @font-face css规则基本上已经成为所有现代浏览器的一个标准。

   (2)   存储字体使用的具体格式还不是一个标准

   ![image-20231215212734310](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215212734310.png)

3. 把你的字体文件放在web上

```html
http://wickedlysmart.com/hfhtmlcss/chapter8/jounal/EmablemaOne-Regular.woff
http://wickedlysmart.com/hfhtmlcss/chapter8/jounal/EmblemaOne-Regular.ttf
```

​	4.在css中增加@font-face属性

```css
/*
注意把该规则放在文件的最上面。放在body规则之上
*/
@font-face{
    font-family:"Emblema One" ;
    src : url("http://wickedlysmart.com/hfhtmlcss/chapter8/jounal/EmablemaOne-Regular.woff"),
    	  url("http://wickedlysmart.com/hfhtmlcss/chapter8/jounal/EmblemaOne-Regular.ttf") ;
}
```

![image-20231215213612226](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231215213612226.png)

​	5.在css中使用font-family名

​	可以用font-family 属性引用你指定的字体名

​	`h1{ font-family : "Emblema One" , sans-serif ; } `





### 2.font-size :字体大小

#### font-size 的值

​	**(1).	按 px 指定大小 (px ：像素)**

```css
body{
    font-size : 14px ;
}
```

- px必须紧跟在像素值后面，不能有空格 。
- 含义：设置一个字体高度为14像素 



​	**(2).	用一个百分数指定字体大小**

```css
body{
    font-size : 14px ;
}
h1{
    font-size : 150% ;
}
```

- 相对于另一个字体指出这个字体有多大

- 是另外哪一个字体大小呢？

  ​	由于font-size 是从父元素继承的一个属性，指定一个百分数字体大小时，就是相对于父元素的字体大小 。



​	**(3).	用 em 指定字体大小，类似百分数 ，这也是一个相对度量单位 。**(注意与<em>元素区分)

`font-size : 1.2em ;` 表示字体大小的比例因子是1.2 ,<h2>元素的大小是父元素的1.2倍 。

```css
body{
    font-size :14px ;
}

h1{
    font-size : 150% ;
}

h2{
    font-size : 1.2em ;
}
```

​	**(4).	使用关键字指定字体大小 。**

```css
xx-small
x-small
small
medium
large
x-large
xx-large
```



#### 指定字体大小的方法 

- **选择一个关键字(推荐samll或medium) ，指定它作为body规则中的字体大小 。这相当于页面的默认字体大小 。**
- **使用em或百分数 ，相对于body字体大小指定的其他元素的字体大小 。**

好处 ？如果相对于body字体大小定义其他元素的字体大小，那么改变web页面中的字体大小就会很容易 ，只需要改变body字体大小就可以了，其他元素会自动按比例变化 ，

若用户想调整页面上字体的大小 ，利用该方法，页面上所有字体都会自动调整大小 。

```css
body{
    font-size:small ;
    font-family: Verdana, Helvetica,Arial, sans-serif ;
}

h1,h2{
    color: #007e7e ;
}

h1{
    font-size: 150% ;
}

h2{
    font-size : 130% ;
}

/*
1.段落文本与body字体一致，<p>会继承来自<body>的font-family 属性
2.<h1><h2><h3> 均未单独指定字体格式，故会从<body>处继承font-family 属性 。
*/
```

### 3.**line-height : 文本的行高 **

line-height: 文本的行高，使得各行之间有更大的行距。

`body{	line-height: 1.6em  ; } ` ,  将各行之间的间距改为 1.6em ,就是字体大小的1.6倍 。



#### **line-height 属性可以继承**

`<div id="elixirs> </div>"`

`#elixirs{ line-height: 1em }` 如果设置整个<div>的line-height 属性，那么<div>中的所有元素都会继承这个属性，包括标题 ，导致标题行高太小了。这是因为 elixirs <div> 中的每一个元素都会继承它的行高设置，即elixirs 元素字体大小的一倍，而 **elixirs <div>的字体大小是从<body>元素继承的**  ，而<body>元素的字体大小设置为small ，

而我们真正希望的是：**elixirs <div>中的所有元素的行高不要基于elixirs <div>的字体大小**，**而是要基于各个元素本身的字体的大小** 。

![image-20231227194600972](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227194600972.png)

利用line-height的属性 ： 可以对它直接使用一个数，而不是一个相对度量(如em ,% ) 如果使用数1 ，就表示elixirs<div>中的各个元素行高是其自己字体大小的1倍，而不是elixirs<div>字体大小的1倍 。



## 4.font-weight : 字体粗细

`font : bold or  normal `

将 font-weight 属性设置为 bold 来使用粗体文本

也可以反过来 ，若一个元素默认地设置为bold ，或者从父元素继承了粗体可以 `font-weight: normal`  去掉粗体样式 ，



## 5.font-style : italic 斜体

italic : 斜体

oblique : 倾斜

## 6.color属性 ： 字体颜色

### web颜色如何工作

css提供的指定颜色的方法 ：1.指定颜色名(black,white ...)	2.按红绿蓝相对百分比指定颜色 (	rgb(255,255,255)	)	3.使用一个十六进制码指定颜色 (#ee0033 ,两个十六进制数表示一个通道)



**用红绿蓝值指定颜色**

```css
body{
    background-color :rgb(80%,40%,0%)
}
```

以rgb开头(red green blue) , 然后指定红绿蓝的百分比 

还可以将红绿蓝指定为0到255之间的一个数值 。



**使用十六进制码指定颜色**

一个十六进制码中，每组两位数字分别代表颜色的红绿蓝分量 

十六进制码总以# 开头 

```css
@fonr-face{
    font-family ："Emblema One" ;
    src :url("...") ;
}
body{
    font-family : Verdana ,Geneva,Arial,sans-serif ;
    font-size : small ;
}

h1,h2{
    color: #cc6600 ;
    text-decoration : underline ;
}

h1{
    font-family: "Emblema One" ,sans-serif ;
    font-size : 220% ;
}

h2{
    font-weight : normal ;
    font-size : 130% ;
}

blockquote {
    font-style : italic ;
}
```



# chapter 9 盒模型 ：与元素亲密接触



**盒模型： box model** ，这是css看待元素的一种方式，css将每个元素看做由一个盒子表示 。

![image-20231226143414590](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226143414590.png)



- **内容区** 

![image-20231226143626578](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226143626578.png)

内容区中内容与盒子边缘没有空间



- **内边距**

![image-20231226143724263](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226143724263.png)



- **边框**

![image-20231226143822433](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226143822433.png)



- **外边距**

![image-20231226143900752](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226143900752.png)





![image-20231226144005680](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226144005680.png)



## 如何设置段落的盒子

将段落增加到一个类中，然后就可以只为段落创建一些定制样式  。



### **1. 内边距 ：padding属性** 

对内容四周设置相同的内边距 。可以设置为一个像素数，也可以设置为一个百分数 。

- 如何只在某个方向上增加内边距 ？

  - **padding-left 属性** 

    ```css
    .guarantee{
        padding : 25px ;
        padding-left : 80px ;
        /*顺序很重要*/
    }
    ```

    ```css
    .guarantee{
        padding-top : 0px ;
        padding-right : 20px ;
        padding-bottom : 30px ;
        padding-left : 10px ;
    }
    ```

- **简写 padding : 0px , 20px , 30px , 10px ;**

​			对应 top , right , bottom , left (即顺时针顺序)

- **当上下 、左右是一样的时候**

  ```css
  .guarantee{
      padding-top : 0px ;
      padding-right : 20px ;
      padding-bottom : 0px ;
      padding-left : 20px ;
  }
  ```

  **简写为 padding : 0px , 20px  ;** (上和下，左和右)

​		

外边距简写类似	

### **2.外边距 ：margin属性** 

可以设置为一个像素数，也可以设置为一个百分数 。

- 什么时候使用内边距/外边距 ？

  - 如果需要再内容区本身周围有更大的可见空间，就要使用内边距，另一方面，如果希望元素与页面边缘之间有更大空间，这种情况下就要使用外边距 。

  

### **3.背景：background-image 属性**

为任何元素增加一个背景图像, 类似于背景颜色，这些背景图片只会出现在内容区和内边距下面，不会出现在边框以外及外边距中出现 。

另外两个会影响背景图像的属性 : **background-position**  **background-repeat**



#### (1).background-position 属性

 **background-position**  会设置图像的位置，可以按像素指定，也可以指定为一个百分数，或使用关键字指定：top，left ，right , bottom , center 

#### (2).background-repeat 属性

- 默认地，背景图像会平铺，也就是反复重复来填满整个背景空间，background-repeat 属性可以控制这种平铺行为。
- 默认地，背景图像会重复，好在background-repeat 属性有一个 no-repeat值，另外，浏览器会默认地把背景图像放在元素的左上角 。



- **background-repeat 的值**

  ```css
  repeat	设置图像在水平和垂直方向上重复，这是默认行为
  no-repeat  图像显示一次，根本不重复 
  repeat-x	图像只在水平方向重复
  repeat-y
  inherit		按父元素的设置来处理
  ```

  

```css
.guarantee{
    border-color : black ;
    border-width : 1px ;
    border-style : solid ;
    background-color : #a7cece ;
    padding : 25px ;/* 在内容的四周增加25像素的内边距*/
    margin :30px ;
    background-image: url(images/background.gif) ;/*注意url两边不需要加引号*/
    background-repeat : no-repeat ;
    background-position : top left ;
}
```



```css
.guarantee{
    border-color : black ;
    border-width : 1px ;
    border-style : solid ;
    background-color : #a7cece ;
    padding: 25px ;
    margin : 30px ;
    font-style :italic ;
    line-height : 1.9em ;
    color: #444444 ;
    font-family:Georgia, 'Times New Roman', Times, serif ;
    background-image : url(images/background.gif) ;
    background-repeat : no-repeat ;
    background-position : top left ;
    padding-left: 80px ;
    margin-right: 250px ;
}
```



- #### 对背景也可以使用简写

```css
#elixirs{
    background-color :white ;
    background-image: url(images/cocktail.gif) ;
    background-repeat : repeat-x ;
}
```

简写： 同样没有顺序限制

```css
#elixirs{
    background :white url(images/cocktail.gif) repeat-x ;
}
```





### **4.边框** ：border 属性

控制元素边框的各种不同方法：

- #### 边框样式： border-style 属性，

  border-style 属性可以控制边框的视觉样式，共有 8 种可用的边框样式，包括实线、虚线、脊线、槽线

![image-20231226180710859](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226180710859.png)



- #### 边框宽度 border-width

![image-20231226180800624](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226180800624.png)



- #### 边框颜色 border-color

![image-20231226180820891](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226180820891.png)



- #### 指定某一边的边框 border-left-color

![image-20231226180918301](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226180918301.png)



- #### 边框圆角 border-radius

![image-20231226181014173](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226181014173.png)



- #### 边框属性也可以使用简写**,可以采用任何顺序**

  ```css
  #elixirs{
      border-width : thin ;
      border-style: solid ;
      border-color : #007e7e ;
  }
  ```

  重写为

  ```css
  #elixirs{
      border : thin solid #007e7e ;
  }
  ```

  

  









## 混合样式表

**使用多个样式表** 

![image-20231226200246683](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231226200246683.png)

**1.允许覆盖和修改原样式表 ，如何做到 ？**

在HTML中，可以指定多个样式表 。需要注意顺序，一个样式表会覆盖在它上面链接的样式表中的样式 。若两个样式表包含冲突的属性定义，HTML文件中最后链接的样式表最为优先

- 有时会有一个样式表作为页面的基础样式，要修改样式，并不是直接修改这个样式表，而是链接这个样式表，然后在它下面提供自己的样式表，指定你想修改的样式 。





之所以希望有多个样式文件，实际上还有一个原因：

**2.可能想针对将要显示页面的设备类型来调整页面的样式**，要做到这一点，可以利用一个 media 属性，在 <link>元素中增加这个属性，只使用适用于指定设备的样式文件

```html
<link href="lounge-mobile.css" rel="stylesheet" media="screen and (max-device-width : 480px )" >
```

media属性允许你指定应用这个样式表的设备类型 ，通过创建一个媒体查询来制定设备类型，媒体查询要与设备匹配 ，这个查询指定了有屏幕的设备

创建一个查询来匹配打印机设备

```html
<link href="lounge-print.css" rel="stylesheet" media="print">
```

lounge-print.css 文件只有当媒体类型为 print时才会使用



**直接在css中增加媒体查询**

要为css指定有特定属性的设备，还有一种方法：不是在link标记中使用媒体查询，还可以直接写在css中 

```css
@media screen and (min-device-width : 481px ){
    #guarantee{
        margin-right : 250px ;
    }
}
@media screen and (max-device-width: 480px ){
    #guarantee{
        margin-right: 30px ;
    }
}
@media print{
    body{
        font-family: Times ,"Times New Roman" ,serif ;
    }
}
p.specials{
    color: red ; /*所有其它规则会应用于所有页面*/
}
```





# chapter 10  div 与 span

**逻辑区**( logical section)

逻辑区就是页面上彼此相关的一组元素 

![image-20231227103502675](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227103502675.png)

## < div >块元素

### id属性在 < div >中应用

使用一个id属性为 <div>提供一个唯一的标签 

接下来就可以对<div>中包含的一组元素指定样式了

```html
<html>
    <head>
        <meta charset="utf-8">
        <title>...</title>
        <link rel="stylesheet" href="...">
    </head>
    <body>
        <div id="cats">
            <h1>cat</h1>
            <p>...</p>
            <img src="...">
        </div>
        <div id="dogs">
            <h1>cat</h1>
            <p>...</p>
            <img src="...">
        </div>
    </body>
</html>
```



```css
#cats{
    background-image: url(leopard.jpg) ;
}
#dogs{
    background-image: url(mutt.jpg) ;
}
```

- 这里有两个规则，分别对应一个 <div> ，每个<div>由一个id选择器来选择 ，

- 就像所有子元素一样，<div> 中的元素也会从 <div>继承一些属性 ，如 font-size ,color 等



![image-20231227104306826](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227104306826.png)

```html
<html>
    <head>
        <meta charset="utf-8">
        <title>...</title>
        <link rel="stylesheet" href="...">
    </head>
    <body>
        <div id="pets">
            <div id="cats">
            	<h1>cat</h1>
            	<p>...</p>
            	<img src="...">
        	</div>
            
        	<div id="dogs">
            	<h1>cat</h1>
            	<p>...</p>
            	<img src="...">
        	</div>
        </div>
    </body>
</html>
```



### < div > 可用的一些属性

#### width 属性

- width 属性 ：允许你指定元素**内容区**的宽度 ，

  - 能不能调整浏览器窗口大小使窗口宽度小于 elixirs <div>的宽度 ？ 有些浏览器不允许把窗口调到那么窄 。不论将窗口调整到多宽或多窄 ，其他段落会自行调整大小 ，而 elixirs <div>的宽度永远是200px 

  - **整个元素的宽度 ？**
    - 指定**内容区、内边距、边框和外边距的宽度** ，所有加在一起就是**整个元素的宽度** 。

  - **一个块元素的默认宽度是 auto ，这说明它会延伸占满可用的空间 。**

  - **高度？**
    - **一般来说一个元素的高度是默认的，也就是 auto ,** 浏览器在垂直方向会延伸内容区，使所有内容都可见，可以显式地设置一个高度，不过这会有风险，如果你指定的高度不够大，不足以放下内容，内容底部有可能溢出到其他元素中。

- < div >的默认内边距为0px

  

#### text-align属性

- text-align 会对**块元素**中的**所有内联内容**对齐。所以对<div>块元素设置了这个属性后，它的所有内联内容都会居中 。 text-align 属性只能在块元素上设置 ，如果直接在内联元素(如 <img> )上使用，则不起作用。
  - < div >中的文本都在其他的块元素中，如 < h2 > < h3 > 和 < p > ，既然text-align 是针对 < div >块元素中的内联元素对齐，那么这些嵌套块元素中的文本怎么也对齐了呢 ？ 
  - < div >元素中的所有文本都在嵌套块元素中，这些块元素**继承了 < div > 的text-align 属性**.并不是 < div > 本身将标题和段落中的文本对齐(标题和段落是块元素) , 实际上是**段落和标题继承了 text-align 值 "center" ，然后是他们自己将内容居中 。**
  - 这样就可以**用< div > 包围一些内容，然后对 < div > 应用样式，而不是对单个元素分别应用样式**。但**并不是所有属性都能继承** ，



### css的子孙选择器

- ![image-20231227171927702](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227171927702.png)

![image-20231227171938482](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227171938482.png)

- 我们需要一种选择子孙的方法 ：**只想选择某些元素的子孙元素 ,例如某个特定部分的 h2, 而不是本页面所有的h2 .**

#### 子孙选择器会选择所有子孙

-  **子孙选择器会选择一个元素中嵌套的所有<h2> ，而不论它嵌套得有多深 .   <h2>可以是<div>的直接孩子，也可以是一个嵌套在<blockquote>或另一个嵌套的<div>d的<h2>(成为孙子) .

![image-20231227172134859](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227172134859.png)

div 是父元素 ， h2 是它的子孙元素 ，这个规则指出要**选择作为一个 < div > 子孙的所有 < h2 > ，**





![image-20231227180720819](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227180720819.png)

**应用于特定的子孙元素 ，可以结合 <div>元素的id属性使用**





#### 选择直接的孩子

```css
#elixirs>h2{
    
}
```

这样仅当<h2>是一个id为elixirs的元素的直接孩子时，才会选择这个<h2>

more complicated version :

选择一个<h2>,要求它是一个<blockquote>的孩子，且<blockquote>在elixirs中

```css
#elixirs blockquote h2{
    
}
/*这会选择<blockquote>的下一级的<h2>元素，而且这个<blockquote>是一个id为elixirs 的元素的子元素 */
```



## 内联元素< span >





![image-20231227212657663](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231227212657663.png)

如何达到该效果？

-  前后是同一个列表项中的文本，好像没有办法分别指定样式 ？

- 只能对元素指定样式，这里只有一些文本，我们需要一个元素来包围每一部分文本，才能对他们分别指定不同的样式 ，`<div class ="cd"> Music for Airports </div>      <div class="artist> Brian Eno </div>"` ,但这是一个块元素，所以会带来换行 。



使用< span >元素 

**<span>元素是针对内联元素的，可以利用<span> 创建内联字符和元素的逻辑分组 ，**

```html
<ul>
    <li>Buddha Bar, Claude Challe</li>
    <li>When It Falls, Zero 7</li>
    <li>Earth 7, L.T.J. Bukem</li>
    <li>Le Roi Est Mort, Vive Le Roi!, Enigma</li>
    <li>Music for Airports, Brian Eno</li>
</ul>
```



### 使用< span >的方法

1**.增加<span>标签 并设置其属于不同的class**

```html
<ul>
    <li><span class="cd">Buddha Bar</span>, <span class="artist">Claude Challe</span></li>
    <li>When It Falls, Zero 7</li>
    <li>Earth 7, L.T.J. Bukem</li>
    <li>Le Roi Est Mort, Vive Le Roi!, Enigma</li>
    <li>Music for Airports, Brian Eno</li>
</ul>
```



**2.在css中指定<span>的样式**

```css
.cd{
    font-style : italic ;
}
.artist{
    font-weight :bold ;
}
```



**能不能对<span>元素设置类似width之类的属性 ？一般的元素能不能设置这些属性 ？**

可以设置内联元素的宽度，不过在对这些元素定位之前，你可能注意不到宽度改变的效果 ，另外还可以对这些元素增加外边距、内边距以及边框。

内联元素上的外边距和内边距和块元素稍有不同 。如果一个内联元素四周都增加外边距，只能看到左边和右边会增加空间。你也可以对内联元素的上边和下边增加内边距 ，不过这个内边距不会影响包围它的其他内联元素的间距，所以内边距会与其他内联元素重叠 。

图像与其他内联元素稍有些不同。图像的宽度、内边距和外边距属性都表现得更像是块元素的相应属性。如果使用<img> 元素的width属性或者css中的width属性来设置图像的宽度，浏览器会缩放图像，使它适合你指定的宽度。

有时如果你不能自己编辑图像来改变大小，但又希望页面上图像能调整大小，浏览器的这种做法就很方便。不过如果依赖于浏览器来缩放你的图像，可能会不必要地下载过多的数据(如果图像大于你需要的尺寸)





## 伪类 pesudo class

```css
a:link{
    color : green ;
}/*应用于未访问状态的链接*/
a:visited{
    color : red ;
}/*应用于已访问状态的链接*/
a:hover{
    color :yellow ;
}/*应用于悬停状态的链接*/


/* a:link , a:visited ... 都允许你指定样式，就好像它们是类一样,但它们实际上并不是类。你可以对伪类指定样式，但没人在HTML中真正输入这些伪类 。*/
```



**工作原理** ：**浏览器会在后台向这些类增加和删除元素 **

浏览器会仔细检查所有< a > 元素 ，把它们增加到正确的伪类中 。如果一个链接已经访问过，它会放在 :visited 伪类中 。用户把鼠标悬停在一个连接上时，浏览器会把这个链接放在 :hover 伪类中 。当用户不再悬停时，浏览器又会把它从hover伪类中取出来 。

现代浏览器已经对其他类型的元素提供了类似 :hover 等伪类支持 ，另外还有一些一些其他的伪类 ，如 伪类 **first-child 对应元素的第一个子元素** ，如< blockquote >中的第一个段落 ，甚至还可以用  :lastchild 伪类选择< blockquote >的最后一个段落



**运用伪类**

```css
#elixirs a:link{
    color :#007e7e ;
}
#elixirs a:visited{
    color :#333333 ;
}
#elixirs a:hover{
    background: #f88396 ;
    color : #0d5353 ;
}
```

第一个选择器要选择 嵌套在一个id为 "elixirs" 的元素中的所有未访问过的<a>元素 。







# chapter11 布局与定位 ：摆放元素

## 流 Flow

流实际上就是浏览器在页面上摆放HTML元素所用的方法 。浏览器从HTML文件最上面开始，**从上到下沿着元素流逐个显示所遇到的各个元素 。**

### 块元素：

它会在每个块元素之间加一个换行。所以首先会显示文档中的第一个元素，然后一个换行，然后第二个元素，如此类推。

![image-20231228115740116](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228115740116.png)

### 内联元素：

内联元素在水平方向上会相互挨着，总体上会从左上方流向右下方 。

![image-20231228120147451](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228120147451.png)

- 文本时内联元素的一种特殊情况。浏览器会把它分解为适当大小的内联元素，以适应给定的空间 。
  - 既然文本(text)的内容不是元素，为什么文本会作为内联元素工作 ？
    - 即便是文本内容，浏览器也要让它流入页面。所以浏览器会确定一行能流入多少文本，然后把这行文本当做一个内联元素 。



### 如何集成

![image-20231228120508387](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228120508387.png)



### 浏览器对外边距的处理



- 浏览器并排放置两个内联元素

  如果这些元素都有外边距，浏览器会在这些元素之间创建足够的空间 ，考虑到它们的外边距 。

  ![image-20231228121238272](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228121238272.png)

- 浏览器上下放置两个块元素

  把两个块元素共同的外边距折叠在一起 ，折叠后共同的外边距高度就是较大的外边距高度 。

  ![image-20231228121510719](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228121510719.png)

​	

## float属性

float属性首先尽可能远地向左或向右(根据float的值) 浮动一个元素 ，然后它下面的所有内容都会绕流这个元素(所谓绕流，就是像流体一样绕着这个元素流动)

### 如何浮动元素

1.指定想要浮动的段落的id

![image-20231228143454681](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228143454681.png)

2.对于所有浮动元素都有一个要求：它必须有一个宽度

![image-20231228143511399](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228143511399.png)

- 其中包含的内联内容必须调整以适应宽度
- 段落是一个块元素，所以不会有元素上移到它旁边。



3.增加 float 属性

![image-20231228143937969](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228143937969.png)

![image-20231228143957941](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228143957941.png)

- 由于这个浮动段落已经从正常的流中删除，所以其他块元素会填在这里，(即在浮动元素的下面) 
- 但是，对内联元素定位时，它们会考虑浮动元素的边界，因此会围绕浮动元素 。





![image-20231228144345749](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228144345749.png)



- 边栏浮在页面上，主内容区在它下面扩展 。
- **如果为主内容区指定适当的外边距，让外边距至少与边栏宽度相同**，这样主内容区的内容就会扩展到边栏附近的位置，而不会一直扩展下去 。
  - 这样主内容区和边栏就会分开。因为外边距是透明的，不会显示背景图像，所以页面本身的背景颜色会透过来 。

- **浮动元素的外边距不会折叠！！！！**
  - 与流入页面的块元素不同，浮动元素只是浮在页面上。即浮动元素的外边距并不会碰到正常流中元素的外边距，故它们不会折叠 。
  - 如果有一个主内容区和一个边栏，通常会对它们分别设置一个上外边距 ，然后如果浮动边栏，它仍然有一个外边距 ，但这个外边距不会再与它上面的空间折叠，这样一来，如果你不记得浮动元素不会折叠外边距，最后边栏和主内容可能会有不同的外边距 。







### 解决重叠问题



**clear属性**

![image-20231228151122103](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228151122103.png)

- 可用使用元素的 **clear 属性**来提出请求 ： **当元素流入页面时，在这个元素的左边、右边、或两边不允许有浮动内容 。**

![image-20231228151312410](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228151312410.png)

### 另一种设计方法 ：对主内容使用 float "left" 

采用 边栏float方式 设计页面的缺点之一 ：由于我们需要把边栏放在页眉下面，而且要在主内容之前，如果有人使用功能受限的浏览器 (PDA , 小的移动设备 ，屏幕阅读器等) ，他们看到的页面就会采用我们写页面时使用的元素顺序 。

- 此时<div>的顺序正确，不过边栏过于扩展 。

此时 <div>摆放顺序是正确的 ，即此时主页面在页眉之下，而不是边栏在页面之下(若将边栏放在主页面之下且边栏悬浮， 会优先流入主页面的内容，直到主页面的内容放置完毕才处理浮动的边栏) 。





### 流体与冻结设计

目前为止，我们采用的所有设计都称为**流体布局 ( liquid layouts )** ：**扩展浏览器窗口时，页面中的内容会扩展以适应页面。**

不过，有时让布局锁定可能更重要，这样当用户调整屏幕大小时，你的设计仍能保持原样。这称为**冻结布局(frozen layouts)** ：内容宽度固定，不会随着浏览器窗口扩展或收缩，代价是不能使用有效使用浏览器宽度 。



#### **冻结布局的操作**

![image-20231228161110514](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228161110514.png)



#### **凝胶布局**  : 



- **凝胶布局：内容宽度固定，但是外边距会随着浏览器窗口扩展或收缩。**



![image-20231228162249724](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228162249724.png)



- **外边距为auto**时，浏览器会确定正确的外边距是多少 。另外还会**确保左右外边距相同，所以内容全居中** 。



## position属性



### position 属性的值 

- **position 属性有4个值** ： static ，absolute ，fixed 和relative 。
  - **static(静态)** : **position的默认值** ，如果是静态定位，元素就会放在正常的文档流中，而不是由你来指定位置 ，要由浏览器决定这些静态定位元素放在哪里 。你**可以使用float属性将一个元素从流中取出，并向左或向右浮动，但最终仍然由浏览器来确定它放在哪里 。**
  - **absolute** : 绝对定位。绝对定位的绝对位置是相对于离它最近的父元素指定的，(一般是<html>,除非你自行指定了另外一个父元素)
    - 绝对定位元素不必须指定宽度，不过，若没有指定宽度，默认地，块元素会扩展浏览器的整个宽度(减去指定的距左边或右边的偏移量)  。(float必须指定width)
  - **fixed (固定**）:固定定位时为元素指定的位置是距离**浏览器窗口边界**的一个偏移量，而不是距**页面边界**的距离 。(视窗：页面的可见区域) 页面中的其他内容会在这些固定定位元素下面正常滚动。
  - **relative** ：相对定位元素相对于其外围包含元素来定位。相对定位元素首先正常流入页面，然后按指定的量偏移，从而留出它们原先所在的空间 。(此时left,right,top,bottom 是指相对正常流中该元素位置的偏移量)
- 综合使用这些定位方式：可以将一个<div>放在另一个<div>中，对外围<div>使用相对定位，这样它仍在页面流中，然后用绝对定位指定内部<div>的位置，这样就能相对于父<div>对他定位了
- 指定位置时不必须使用像素 。还可以使用百分数 。如果使用百分数，改变浏览器宽度时，元素的位置可能会改变。(如果浏览器设置为800像素宽，元素的left位置设置为 10% , 那么元素就会放在距浏览器窗口左边80像素的位置 )

### 绝对定位 absolute positioning

另一种创建两栏布局的常用技术，它能让内容保持正确的顺序，同时避免流体布局存在的一些问题 。



**绝对定位如何工作**

```css
#sidebar{
    position: 	absolute;
    top:		100px ;
    right:		200px ;
    width:		280px ;
}
/*
首先使用position属性指定这个元素要绝对定位
接下来设置top和right属性 ，也可以用 left和bottom指定
另外为<div>指定一个宽度
*/
```

- 一个元素绝对定位时，浏览器首先将它从流中完全删除 ，然后将这个元素放置在 指定的位置上



![image-20231228175515219](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228175515219.png)

![image-20231228175608511](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228175608511.png)

**绝对定位时使用 z-index 属性来控制哪个元素在上面**(可以认为这个z轴从屏幕指向你)

```css
#div1{
    position: 	absolute;
    top: 		30px;
    left: 		30px;
    z-index: 	0;
}
#div2{
    position: 	absolute;
    top:		30px;
    left: 		30px;
    z-index: 	1;
}
```



- 浮动元素 vs 绝对定位
  - 流中的元素会调整它们的内容来适应浮动元素的边界。而绝对定位元素对其他元素没有任何影响



![image-20231228180815604](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228180815604.png)



![image-20231228184555978](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228184555978.png)















## css表格显示

**css表格显示在一个有行和列的表格中显示块元素 。通过将内容放在一个css表格中，可以创建多栏设计**

对于css表格显示，每个单元格会包含一个HTML块元素 。

![image-20231228185923319](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228185923319.png)



### **实现表格显示**



#### 增加HTML结构

![image-20231228190253539](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228190253539.png)



![image-20231228190439901](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228190439901.png)

```html
<div id="tableContainer">
    <div id="tableRow">
        <div id="main">
            ...
        </div>
        <div id="sidebar">
            ...
        </div>
    </div>
</div>
```



#### css创建表格显示

![image-20231228192543793](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228192543793.png)

![image-20231228192555278](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231228192555278.png)

```css
#tableContainer{
    display: 	table; /** display:table 表明tableContainer <div>要像表格一样摆放*/
    border-spacing:	10px ;
}
#tableRow{
    display: 	table-row ;
}
#main{
    display: 	table-cell ;
    background:	#efe5d0 url(images/background.gif) top left ;/*top left 是属性background-position 的值*/
    font-size:	150% ;
    padding: 	15px ;
    vertical-align: top ;
}
```



- **border-spacing 属性**为表格中的单元格增加10像素的边框间距 。**可以把border-spacing 看做是常规元素的外边距** 。由于我们要使用单元格上的border-spacing, 所以不再需要 <div>上的外边距 。

​		**border-spacing 和外边距创建的空间不会折叠**

- **vertical-align 属性** 确保表格**单元格中的内容相对于单元格顶部对齐** ，垂直对齐可以设置为top ，middle 或 bottom(默认方式为中间对齐)

- 如何控制列的宽度 ？

  - **用 width 属性就能控制列的宽度** ，可以用**百分数**设置各个列的宽度 ( 最好确保所有列的宽度加在一起是100% ) 。通过使用百分数，你的表格仍能随着浏览器窗口大小的调整扩展和收缩。

  

- css display:table vs HTML表格
  - 它们都是在HTML中创建一种结构，能够映射到表格的行和列。不过与HTML表格不同，css表格显示只是使用一种**类似表格的布局**来表现这个结构中的内容。
  - **HTML表格面向的是表格数据**，也就是应当有表格结构的数据。
  - 所以使用css表格显示只是创建某种**表现布局**的一种方法，而HTML表格则是建立**数据的结构**。





# chapter12 HTML5新特性



## HTML5新元素

将原来的<div>更换为一些更特定的元素，能够更明确地指示其中包含什么类型的内容。

```html
<article>	页面中一个独立的组成部分，如一个博客帖子、用户论坛或新闻报道
<nav>	所包含的内容将作为页面的导航链接
<header>	放在页面顶部或页面某个区块的顶部
<footer>	放在页面底部或页面某个区块的底部
<time>		可能包含一个日期或时间
<aside>		包含的内容是对页面内容的补充，如插图或边栏
<section>	一个主题性内容分组，通常包含一个header，可能还有一个footer
<video>		为页面增加视频媒体
```



HTML内容

```html
<div id="header">
    <img id="headerLogo" src="images/headerLogo.gif" alt="Starbuzz Coffee logo image">
    <img id="headerSlogan" src="images/headerSlogan.gif" alt="Providing all the...">
</div>
```

改为

```html
<header>
    <img id="headerLogo" src="images/headerLogo.gif" alt="Starbuzz Coffee logo image">
    <img id="headerSlogan" src="images/headerSlogan.gif" alt="Providing all the...">
</header>
```



css

```css
header{
    ...
}
header img#headerSlogan{
    /*子孙选择器 。表明选择 父元素是header 的id 为"#headerSlogan" 的<img>标签元素 */
}
footer{
    ...
}
```



![image-20231229115605359](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231229115605359.png)

把各个博客帖子放在各自的<article>元素中，每个帖子都是一个独立的元素，因此你可以取出这些文章而不会影响其余文章的可读性。



- < section > vs < article > 
  - < section> 元素比< article>元素通用，不过它又不及< div>通用 。例如，如果只是要增加一个元素以便为页面指定样式，那么可以使用< div> ,如果要增加一个元素来标记一些内容，指示这是由相关内容构成的一个结构明确的区块，那就可以使用< section> ,如果有些内容可以独立于页面上的其余内容进行重用和分发，那就使用< article>

- < header >

​		<header>元素能提供额外的语义含义，可以将页面、区		块或文章的首部与其余的内容区分开。



### Navigator

- if不使用 <nav>元素

```html
<ul>
	<li><a href="index.html">HOME</a></li>
	<li class="sekected"><a href="blog.html">BLOG</a> </li>
	<li><a href="...">INVENTIONS</a> </li>
</ul>
```



```css
ul{
    background-color:	#efe5d0;
    margin:			  	10px 10px 0px 10px ;
    list-style-type:	none;
    padding: 			5px 0px 5px 0px;
}
ul li{
    display:			inline;/* 将各个列表项的显示从 block 改为inline ，所以现在列表项的前后不再有回车，它们会像常规的内联元素一样在页面上流入一行 。*/
    padding:			5px 10px 5px 10px ;
}
ul li a:link, ul li a:visited{
    color:				#954b4b;
    border-bottom:		none;
    font-weight:		bold;
}
ul li.selected{
    background-color:	#c8b99c;
}/*为selected 类的<li> 元素设置背景，这样如果某个导航项正好对应我们所在的页面，它看起来会与其他导航项有所不同*/
```



- 使用 <nav> 元素

  ```html
  <nav>
  	<ul>
  		<li><a href="index.html">HOME</a></li>
  		<li class="sekected"><a href="blog.html">BLOG</a> </li>
  		<li><a href="...">INVENTIONS</a> </li>
  	</ul>
  </nav>
  ```

  ```css
  nav{
      background-color:	#efe5d0;
      margin:				10px 10px 0px 10px;
  }/*由于继承，<nav>中所有的内容都会按这些属性指定样式*/
  nav ul{
      margin:			  	0px;
      list-style-type:	none;
      padding: 			5px 0px 5px 0px;
  }
  nav ul li{
      display:			inline;
      padding:			5px 10px 5px 10px ;
  }
  nav ul li a:link, nav ul li a:visited{
      color:				#954b4b;
      border-bottom:		none;
      font-weight:		bold;
  }
  nav ul li.selected{
      background-color:	#c8b99c;
  }
  ```





### video

```html
<article>
	<header>
    	<h1>
            Starbuzz launches.....Tweet Sip</h1>
        <time datatime="2012-05-03">5/3/2012</time>
    </header>
    
    <p>
        As promised,today ......
    </p>
    
    <video controls autoplay width="512" height="288" src="video/tweetsip.mp4"></video>

</article>
```



```css
<video controls autoplay width="512" height="288" src="video/tweetsip.mp4" poster="images/poster.png" id="video"></video>
```

- controls 和 autoplay 属性
  - controls 和 autoplay 属性是布尔属性 ，没有值 。所以如果有controls属性则视频控件就会出现，否则不出现 。同理如果有autoplay属性一旦页面加载视频就会自动播放
- poster属性
  - 可以提供一个可选的海报图像，视频未播放时就会显示这个图像

- preload属性
  - preload属性通常用于细粒度地控制视频如何加载来实现优化。通常浏览器会根据是否设置autoplay以及用户的带宽来选择加载多少视频。可以覆盖这种设置，将preload 设置为 none (在用户真正播放视频之前不下载视频) ，也可以设置为 metadata (下载视频元数据，但不下载视频内容)

**视频格式**

![image-20231229225426934](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231229225426934.png)

- 每种格式分别使用一个 <source>元素 。

```html
<video controls autoplay width="512" height="288">
<source src="video/tweetsip.mp4">
<source src="video/tweetsip.webm">
<source src="video/tweetsip.ogv">
<p>
    Sorry, your browser doesn't support the video element</p>
</video>
```

![image-20231229225846118](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231229225846118.png)

![image-20231229225931790](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231229225931790.png)





# chapter13 表格与更多列表

## 表格的元素



### < th > < tr > < td >

- 使用 <table>标记开始表格 。
- 每个<th>元素分别是某一列的表头。 table header
- 每个<tr>元素工程表格中的一行 。table row
- 每个<td>元素包含表格中的一个单元格 (<td>元素分别包含一个表格数据) table data

```html
<table>
    <tr>
    	<th>City</th>
        <th>Data</th>
        <th>Temperature</th>
        <th>Altitude</th>
        <th>Population</th>
        <th>Diner Rating</th>
    </tr>
    <tr>
    	<td>Walla Walla,WA</td>
        <td>June 15th</td>
        <td>75</td>
        <td>1024 ft</td>
        <td>19686</td>
        <td>4/5</td>
    </tr>
    <tr>
    	<td>Magic City ID</td>
        <td>June 25th</td>
        <td>74</td>
        <td>5312 ft</td>
        <td>50</td>
        <td>3/5</td>
    </tr>
</table>
```

![image-20231229232832371](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231229232832371.png)



### < caption >

为表格增加一个标题 ,提供额外信息。默认地，大多数浏览器会把标题显示在表格上方 。

- 注意HTML中 <caption> 要放在表格元素上方，如需调整标题位置使用css指定。

```html
<table>
    <caption>the cities I visited</caption>
    <tr>
    	<th>City</th>
        <th>Data</th>
        <th>Temperature</th>
        <th>Altitude</th>
        <th>Population</th>
        <th>Diner Rating</th>
    </tr>
    <tr>
    	<td>Walla Walla,WA</td>
        <td>June 15th</td>
        <td>75</td>
        <td>1024 ft</td>
        <td>19686</td>
        <td>4/5</td>
    </tr>
    <tr>
    	<td>Magic City ID</td>
        <td>June 25th</td>
        <td>74</td>
        <td>5312 ft</td>
        <td>50</td>
        <td>3/5</td>
    </tr>
</table>
```



## css规则

version 1.0

```css
table{
  margin-left:      20px;
  margin-right:     20px;
  border:           thin solid black;
  caption-side:     bottom;/*把标题移到表格的下方*/
}
td,th{
  border:           thin dotted gray ;
  padding:          5px;
}
caption{
  font-style:       italic;
  padding-top:      8px ;
}
```



### border-spacing 

![image-20231230113056543](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230113056543.png)

- border-spacing 属性针对整个表格定义

我们不能单独地设置各个表格单元格外边距，而是要为所有单元格设置一个共同的间距。 

```css
border-spacing : 10px 30px ;
/* 这会设置10px的水平边框间距 ，30px的垂直边框间距 */
```

( 将border-spacing 值设置为0 ，可以将两条线重合为1条 )



### border-collapse 

border-collapse 属性折叠边框使单元格之间没有边框间距 。

```css
border-collapse: 	collapse;
```



### 颜色



**background-color**

```css
th{
    background-color:	#cc6600;
}
```



**对各行着色**

对表格着色的常用方法是为各行指定交替的颜色 ，这样就能更容易地区分各行。

可以定义一个类 " cellcolor " ，然后把这个类属性加到希望着色的行上

```css
.cellcolor{
    background-color: #fcba7a;
}
```



**更高级的方法为表格隔行增加颜色** ：**nth-child 伪类**

伪类会根据元素的状态来指定元素的样式 。对于nth-child 伪类，状态则是一个元素相对于他的兄弟元素的数字顺序 。

![image-20231230123030694](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230123030694.png)



```css
p:nth-child(even){
    background-color: 	red;
}
p:nth-child(odd){
    background-color:	green;
}
```

还可以更加灵活，用数字n指定简单的表达式 



### text-align  vertical-align

指定单元格内数据对齐方式

```css
.right{
    text-align: right;
}
.center{
    text-align: center;
}
```

 `<td class="right">...</td>`



## 跨多行的单元格

rowspan 属性指定一个表格数据单元格占多少行，然后从这个单元格所跨越的其他行中删除相应的表格数据元素 。

```html
<tr>
	<td rowspan="2">Truth or Consequences,NM</td>
    <td class="center">August 9th</td>
    <td class="center">93</td>
    <td rowspan="2" class="right">4242 ft</td>
    <td rowspan="2" class="right">7289</td>
    <td class="center">5/5</td>
</tr>

<tr>
	
    <td class="center">August 27th</td>
    <td class="center">98</td>
    
    <td class="center">4/5</td>
</tr>
```

在第二行中，只指定我们需要的列 。



同理，可以跨多列，只需要为 <td> 增加一个 colspan 属性 ，跨多列时，需要删除同一行中的表格数据元素 。





## 表格嵌套

将另一个 <table> 元素放在一个 <td> 中

```html
<tr>
	<td rowspan="2">Truth or Consequences,NM</td>
    <td class="center">August 9th</td>
    <td class="center">93</td>
    <td rowspan="2" class="right">4242 ft</td>
    <td rowspan="2" class="right">7289</td>
    <td class="center">5/5</td>
</tr>

<tr>
	
    <td class="center">August 27th</td>
    <td class="center">98</td>
    
    <td>
		<table>
			<tr>
            	<th>rose</th>
                <td>5/5</td>
            </tr>
			<tr>
            	<th>tom</th>
                <td>4/5</td>
            </tr>
		</table>
	</td>
</tr>
<!-- 用表格表头表示名字，用数据单元格表示评分 --!>
```

- 如何选中嵌套表格的表头?

  -  ```css
     table table th{
         background-color :white ;
     }
     ```

    



## 列表样式

- **list-style-type 属性** ，可以控制列表中使用的项目符号(也叫列表标记)

list-style-type 属性的值 ： disc , circle , square , none （无序列表 ul ）



![image-20231230132321252](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230132321252.png)



- 定制标记

  **list-style-image 属性** ，为列表设置标记图像

  ```css
  li{
      list-style-image:	url(images/backpack.gif) ;
      padding-top:	5px;
      margin-left:	20px;
         
  }
  ```










# chapter14 HTML表单 ：实现交互



## 表单如何工作

![image-20231230154714481](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230154714481.png)



### 表单在浏览器中如何工作

1.浏览器加载页面

- 遇到表单元素时，它在页面上创建控件，允许输入各种各样的数据
  - 控件就是类似按钮、文本输入框或下拉菜单之类的工具。

2.用户输入数据并提交表单

3.服务器响应



#### 浏览器发送数据的方法

POST 和 GET 

![image-20231230213421933](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230213421933.png)

- 既然再向服务器发送数据，为什么这种方法叫 GET ?
  - 浏览器的主要任务是什么 ？ 就是从服务器得到web页面 。使用GET 时，浏览器像往常一样用正常的方式得到web页面 ，只不过，由于有一个表单，它会在URL 的最后追加另外一些数据 。除此以外 ，浏览器会把它当做一个普通请求来处理 。
  - 另一方面，利用POST ， 浏览器实际上会创建一个小数据包 ，并把它发送到服务器 。
- 何时使用GET ? 何时使用 POST ?
  - 如果你希望用户能够对提交表单后的结果页面加书签，就必须使用GET 。
  - 何时想要加书签？
    - 假设你有一个服务器脚本 ，它会返回一个搜索结果列表 ，你可能希望用户能够对这些结果加书签，这样他们就能直接查看这些结果 ，而不用再填写表单 。
  - 另一方面，如果你有一个处理订单的服务器脚本，可能不希望用户对这个页面加书签 ，否则每次他们返回到这个书签时，都会重新提交这个订单 。
  - 还有一种情况你肯定不想使用GET, 比如你的订单中的数据是私有的，因为URL是明文可以看到，别人只要查看你的浏览器历史，就能看到这些数据 。
  - 如果你使用 <textarea> ,就应该使用POST ,因为可能发送大量数据 。 



**HTML代码**

```html
<form action="http://wickedlysmart.com/hfhtmlcss/contest.php" method="post">
    <p>
        Just type in your name and click submit to enter the contest:<br>
        First name:<input type="text" name="firstname" value=""><br>
        Last name:<input type="text" name="lastname" value=""><br>
        <input type="submit">
    </p>
</form>

<!-- 用 <input> 元素创建这些控件 --!>
```





## < form >

**< form >元素**不仅**包含构成表单的所有元素**，还会告诉浏览器当你提交表单时**要把表单数据发送到哪里** 以及**浏览器要用什么方法发送数据 。**


```html
<form action="http://wickedlysmart.com/hfhtmlcss/contest.php" method="post">
    
</form>
```

- action 属性包含web服务器的 URL ，contest.php 是要**处理表单数据**的**服务器脚本**的文件名 。
- method 属性确定表单数据如何发送到服务器 。



### 表单元素的属性



#### name属性

name属性相当于表单和处理表单的服务器脚本之间的一个粘合剂 。

- < form >中的每个表单元素都有**唯一的name属性** 。浏览器以 **name:value的格式** 打包数据发给服务器脚本

  ![image-20231230202327259](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230202327259.png)



- 服务器脚本怎么知道我要在表单中使用哪些名字 ？ 换句话说，我怎么为表单元素选择名字 ？

  实际上应该反过来，你必须知道**服务器脚本希望有哪些表单元素名** ，并**相应地编写表单**。服务器脚本的编写者必须在脚本文档中提供信息 。



#### value属性

**value的值**是要**发送到服务器脚本**的内容 。



#### 标签

标签就是会显示在控件上的提示性信息 。需要注意标签和name的区别 。

对单选钮元素来说，标签一般放在<input>元素的右边 。

<p>
    Type:<br>
    <input type="radio" name="beantype" value="whole">Whole bean <br>
    <input type="radio" name="beantype" value="ground">Ground 
</p

```html
<p>
    Type:<br>
    <input type="radio" name="beantype" value="whole">Whole bean <br>
    <input type="radio" name="beantype" value="ground">Ground 
</p>
```





**< label >** 

**用 < label >元素来标记这些标签** 。 < label > 元素可以提供页面结构的更多信息，使你能更容易地使用css对标签设置样式。

默认地，标签与普通的文本看上去并没有两样，不过在**可访问性**方面他们确实有很大不同。任何表单控件都可以使用<label>元素 

```html
<input type="radio" name="hotornot" value="hot" id="hot">
<label for="hot">hot</label>

<input type="radio" name="hotornot" value="not" id="not">
<label for="not">not</label>
```

- 首先为表单元素增加一个id属性 。
- 然后增加一个 <label>, 设置 **for 属性为相应的 id** 



- 为单选钮或复选框增加标签时，虽然name相同，但每个控件的id必须唯一

- 标签可以放在与它关联的控件的任意位置，只要for属性的值与id匹配，标签放在哪里并不重要 。







### 表单元素的类型



#### textarea元素

< textarea >元素会创建一个多行的文本区，可以在其中输入多行文本，如果输入的文本在文本区中放不下，右边还会出现一个滚动条 。

```html
<textarea name="comments" rows="10" cols="48"></textarea>
```

- rows 和 cols 分别告诉浏览器文本区高度和宽度分别为多少个字符

- 开始和结束标记之间的所有文本会成为浏览器**文本区空间中的初始文本**



#### select & option元素

**< option > 元素用来表示各个菜单项** ，**< select >元素在web页面中创建一个菜单控件**。 < select >与< option >结合使用可以创建一个菜单 ，  菜单提供了一种从一组选项中做出选择的方法 。 

![image-20231230164746499](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230164746499.png)

```html
<select name="characters">
    <option value="Jersery">New Jersery</option>
    <option value="Tommy">Perfect Tommy</option>
</select>
```

- option 元素的**内容**用作**菜单项的描述标签**，每个菜单选项有value 属性。浏览器打包表单元素的name和value时会使用**select的name**和**option的value**  。option元素没有name属性 。因为所有option元素实际上是菜单的一部分 ，而菜单由select元素创建 
- 如果为 select 元素增加**布尔属性 multiple** ，就会把你的单选菜单变成一个**多选菜单** ，不再显示下拉式菜单



#### < input > 表单元素



**1.void元素，没有结束标记**

**2.内联元素，如需换行，需要 < br >**



**< input >表单元素的< type > 属性**



**type = "text"** ![image-20231230162337637](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230162337637.png)

-  text <input>元素会在浏览器页面中创建一个单行文本输入控件

- text <input>元素的value属性的内容为用户在文本输入框中输入的内容 ，也就是要发送到服务器脚本的内容 。

  

  



**type = "submit"**

![image-20231230162523071](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230162523071.png)

submit <input> 会创建一个按钮允许你提交表单。点击这个按钮时浏览器会把表单发送到服务器脚本进行处理

提交按钮上默认显示submit ，为元素指定一个**value 属性**从而按钮上会显示value属性指定的值





**type="radio"**

radio <input> 元素会创建**包含多个按钮的空间**，但是一次只能选择其中一个按钮 。

![image-20231230163139493](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230163139493.png)



- **每一组单选按钮必须有相同的name**

****

```html
<form>
    <p>
    Type:<br>
    <input type="radio" name="beantype" value="whole">Whole bean <br>
    <input type="radio" name="beantype" value="ground" checked >Ground 
</p>
</form>
```

- 为单选钮输入元素增加一个 **bool属性值 checked** ，浏览器显示表单就会默认地选中这个元素 。**注意布尔属性不需要值，只要有属性checked ，这个输入控件就会选中。**





**type="checkbox"**

**与单选钮一样，我们把标签放在复选框右边**

![image-20231230163721008](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230163721008.png)



**文件输入**			

```html
<input type="file" name="doc">
```

这样这个 <input>元素会创建一个文件输入控件 ，允许你选择一个文件 ，表单提交时，文件的内容会随其余的表单数据一同发送给服务器

![image-20231231144251353](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231231144251353.png)



**HTML5 新的type属性值**



![image-20231230171931903](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230171931903.png)

![image-20231230172029498](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230172029498.png)

```html
<p>
	Number os bags:<input type="number" name="bags" min="1" max="10">
</p>
<p>
    Must arrve by data: <input type="data" name="date">
</p>
```







#### others



**fieldset 和 legend**

表单变得越来越大时，在视觉上对元素进行分组会很有帮助 。HTML提供了一个 <fieldset>元素 ，可以用来将公共元素组织在一起 。<fieldset>又使用了<legend> .

```html
<fieldset>
    <legend>
        Condiments
    </legend>
    <input type="checkbox" name="spice" value="salt">Salt <br>
    <input type="checkbox" name="spice" value="pepper">Pepper<br>
    <input type="checkbox" name="spice" value="garlic">Garlic<br>
</fieldset>
```

<form>
    <fieldset>
    <legend>
        Condiments
    </legend>
    <input type="checkbox" name="spice" value="salt">Salt <br>
    <input type="checkbox" name="spice" value="pepper">Pepper<br>
    <input type="checkbox" name="spice" value="garlic">Garlic<br>
</fieldset>
</form>





**placeholder**

![image-20231231144717898](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231231144717898.png)





**required**

![image-20231231144802634](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231231144802634.png)









## 为表单增加样式

![image-20231230215400368](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20231230215400368.png)



**将表单元素放入HTML结构实现表格显示布局**

结构： 一个 tableRow <div> 对应表行，另外每个单元格放在 <p>中。

```html
<form action="http://starbuzzcoffee.com/processorder.php" method="post">
    
    <div class="tableRow">
        <p>Choose your beans:</p>
        <p>
            <select name="beans">
                <option value="House Blend">House Blend</option>
                <option value="Bolivia">Shade Grown Bolivia Supremo</option>
                <option value="Guatemala">Organic Guatemala</option>
            </select>
        </p>
    </div>
    
    <div class="tableRow">
        
        <p>Type:</p>
        <p>
            <input type="radio" name="beantype" value="whole">Whole beans <br>
            <input type="radio" name="beantype" value="ground" checked> Ground 
        </p>
    </div>
    
    <div class="tableRow">
        
        <p>Numbers of bags:</p>
        <p> <input type="number" name="bags" min="1" max="10"> </p>   
    </div>
 
    <div class="tableRow">
        <p>Must arrive by data:</p>
        <p> <input type="time" name="date"> </p>
    </div>
    
    <div class="tableRow">
        <p>Extras:</p>
        <p>
            <input type="checkbox" name="extras[]" value="giftwrap">Gift wrap<br>
            <input type="checkbox" name="extras[] " value="catalog" checked>Include catalog with order
        </p>
    </div>
    
    <div class="tableRow">
        <p class="heading">Ship to</p>
        <p></p> <!-- 右列中还有一个空单元格，所以在这里直接放一个空的<p>元素 -->
    </div>
    <!-- 对于只包含标签ship to 的行，为 <p> 只增加了一个类heading ，以便对这个文本加粗 。-->
    
    <div class ="tableRow">
        <p>Name:</p>
        <p> <input type="text" name="name" value=""> </p>
    </div>
    
    <div class="tableRow">
        <p>Address:</p>
        <p><input type="text" name="address" value=""></p>
    </div>
    
    <div class="tableRow">
        <p>Address:</p>
        <p><input type="text" name="address" value=""></p>
    </div>
    
    <div class="tableRow">
        <p>Customer Comments:</p>
        <p>
            <textarea name="comments" rows="10" cols="48"></textarea>
        </p>
    </div> 
    
    <div class="tableRow">
        <p></p>
        <p> <input type="submit" value="Order Now"> </p>
    </div>

</form>
```



```css
body{
    background:		#efe5d0 url(images/background.gif) top left ;
    margin:			20px;
}
form{
    display:		table;
    padding:		10px;
    border:			thin dotted #7e7e7e;
    background-color:#e1ceb8;
}
form textarea{
    width:			500px;
    height:			200px;
}
div.tableRow p{
    display:		table-cell;
    vertical-align:	top;
    padding:		3px ;
}
div.tableRow p:first-child{
    text-align:		right;
}
p.heading{
    font-weight:	bold;
}
```

