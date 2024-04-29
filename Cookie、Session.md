# JavaWeb - Cookie、Session、SessionId 详解(上)

## Cookie属性

name字段：一个cookie的名称

value字段：一个cookie的值

domain字段：可以访问此cookie的域名

path字段：可以访问此cookie的页面路径

Size字段：此cookie大小

http字段：cookie的httponly属性，若此属性为True，则只有在http请求头中会有此cookie信息，而不能通过document.cookie来访问此cookie。

secure字段：设置是否只能通过https来传递此条cookie。

expires/Max-Age字段：设置cookie超时时间。如果设置的值为一个时间，则当到达该时间时此cookie失效。不设置的话默认是session，意思是cookie会和session一起失效，当浏览器关闭（并不是浏览器标签关闭，而是整个浏览器关闭）后，cookie失效。

## 一、概述

会话（[Session](https://so.csdn.net/so/search?q=Session&spm=1001.2101.3001.7020)）跟踪是Web程序中常用的技术，用来**跟踪用户的整个会话**。常用的会话跟踪技术是Cookie与Session。**Cookie通过在客户端记录信息确定用户身份，Session通过在服务器端记录信息确定用户身份。**

本章将系统地讲述Cookie与Session机制，并比较说明什么时候不能用Cookie，什么时候不能用Session。

## 

## 二、Cookie

**1.1  Cookie机制**

在程序中，会话跟踪是很重要的事情。理论上，**一个用户的所有请求操作都应该属于同一个会话**，而另一个用户的所有请求操作则应该属于另一个会话，二者不能混淆。例如，用户A在超市购买的任何商品都应该放在A的购物车内，不论是用户A什么时间购买的，这都是属于同一个会话的，不能放入用户B或用户C的购物车内，这不属于同一个会话。

而Web应用程序是使用HTTP协议传输数据的。**HTTP协议是无状态的协议。一旦数据交换完毕，客户端与服务器端的连接就会关闭，再次交换数据需要建立新的连接。这就意味着服务器无法从连接上跟踪会话。**即用户A购买了一件商品放入购物车内，当再次购买商品时服务器已经无法判断该购买行为是属于用户A的会话还是用户B的会话了。要跟踪该会话，必须引入一种机制。

Cookie就是这样的一种机制。它可以弥补HTTP协议无状态的不足。在Session出现之前，基本上所有的网站都采用Cookie来跟踪会话。

**1.1.1  什么是Cookie**

Cookie意为“甜饼”，是**由W3C组织提出**，最早由Netscape社区发展的一种机制。目前Cookie已经成为标准，所有的主流浏览器如IE、Netscape、Firefox、Opera等都支持Cookie。

​     由于HTTP是一种无状态的协议，服务器单从网络连接上无从知道客户身份。怎么办呢？**就给客户端们颁发一个通行证吧，每人一个，无论谁访问都必须携带自己通行证。这样服务器就能从通行证上确认客户身份了。这就是Cookie的工作原理。**

​     Cookie实际上是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用response向客户端浏览器颁发一个Cookie。客户端浏览器会把Cookie保存起来。当浏览器再请求该网站时，浏览器把请求的网址连同该Cookie一同提交给服务器。服务器检查该Cookie，以此来辨认用户状态。服务器还可以根据需要修改Cookie的内容。

![image.png](https://ucc.alicdn.com/pic/developer-ecology/32f70f453725450a8da49e0426a9bac1.png)

查看某个网站颁发的Cookie很简单。在浏览器地址栏输入**javascript:alert (document. cookie)**就可以了（需要有网才能查看）。JavaScript脚本会弹出一个对话框显示本网站颁发的所有Cookie的内容，如图1.1所示。

![image.png](https://ucc.alicdn.com/pic/developer-ecology/d2a949b0c1e34dd6be08baba63edd562.png)

图1.1  Baidu网站颁发的Cookie

图1.1中弹出的对话框中显示的为Baidu网站的Cookie。其中第一行BAIDUID记录的就是笔者的身份helloweenvsfei，只是Baidu使用特殊的方法将Cookie信息加密了。

注意：Cookie功能需要浏览器的支持。

如果浏览器不支持Cookie（如大部分手机中的浏览器）或者把Cookie禁用了，Cookie功能就会失效。

不同的浏览器采用不同的方式保存Cookie。

IE浏览器会在“C:\Documents and Settings\你的用户名\Cookies”文件夹下以文本文件形式保存，一个文本文件保存一个Cookie。

**1.1.2  记录用户访问次数**

Java中把Cookie封装成了javax.servlet.http.Cookie类。每个Cookie都是该Cookie类的对象。服务器通过操作Cookie类对象对客户端Cookie进行操作。通过**request.getCookie()获取客户端提交的所有Cookie**（以Cookie[]数组形式返回），**通过response.addCookie(Cookiecookie)向客户端设置Cookie。**

Cookie对象使用key-value属性对的形式保存用户状态，一个Cookie对象保存一个属性对，一个request或者response同时使用多个Cookie。因为Cookie类位于包javax.servlet.http.*下面，所以JSP中不需要import该类。

**1.1.3  Cookie的不可跨域名性**

很多网站都会使用Cookie。例如，Google会向客户端颁发Cookie，Baidu也会向客户端颁发Cookie。那浏览器访问Google会不会也携带上Baidu颁发的Cookie呢？或者Google能不能修改Baidu颁发的Cookie呢？

答案是否定的。**Cookie具有不可跨域名性。**根据Cookie规范，浏览器访问Google只会携带Google的Cookie，而不会携带Baidu的Cookie。Google也只能操作Google的Cookie，而不能操作Baidu的Cookie。

Cookie在客户端是由浏览器来管理的。浏览器能够保证Google只会操作Google的Cookie而不会操作Baidu的Cookie，从而保证用户的隐私安全。浏览器判断一个网站是否能操作另一个网站Cookie的依据是域名。Google与Baidu的域名不一样，因此Google不能操作Baidu的Cookie。

需要注意的是，虽然网站images.google.com与网站www.google.com同属于Google，但是域名不一样，二者同样不能互相操作彼此的Cookie。

注意：用户登录网站www.google.com之后会发现访问images.google.com时登录信息仍然有效，而普通的Cookie是做不到的。这是因为Google做了特殊处理。本章后面也会对Cookie做类似的处理。

**1.1.4  Unicode编码：保存中文**

中文与英文字符不同，**中文属于Unicode字符，在内存中占4个字符，而英文属于ASCII字符，内存中只占2个字节。**Cookie中使用Unicode字符时需要对Unicode字符进行编码，否则会乱码。

提示：Cookie中保存中文只能编码。一般使用UTF-8编码即可。不推荐使用GBK等中文编码，因为浏览器不一定支持，而且JavaScript也不支持GBK编码。

**1.1.5  BASE64编码：保存二进制图片**

Cookie不仅可以使用ASCII字符与Unicode字符，还可以使用二进制数据。例如在Cookie中使用数字证书，提供安全度。使用二进制数据时也需要进行编码。

%注意：本程序仅用于展示Cookie中可以存储二进制内容，并不实用。由于浏览器每次请求服务器都会携带Cookie，因此Cookie内容不宜过多，否则影响速度。Cookie的内容应该少而精。

**1.1.6  设置Cookie的所有属性**

除了name与value之外，Cookie还具有其他几个常用的属性。每个属性对应一个getter方法与一个setter方法。Cookie类的所有属性如表1.1所示。

表1.1  Cookie常用属性![image.png](https://ucc.alicdn.com/pic/developer-ecology/1c9e662a82f545cbae2a8133ecc7fabc.png)

**1.1.7  Cookie的有效期**

Cookie的maxAge决定着Cookie的有效期，单位为秒（Second）。Cookie中通过getMaxAge()方法与setMaxAge(int maxAge)方法来读写maxAge属性。

如果maxAge属性为正数，则表示该Cookie会在maxAge秒之后自动失效。浏览器会将maxAge为正数的Cookie持久化，即写到对应的Cookie文件中。无论客户关闭了浏览器还是电脑，只要还在maxAge秒之前，登录网站时该Cookie仍然有效。下面代码中的Cookie信息将永远有效。

```
Cookie cookie = new Cookie("username","helloweenvsfei");   // 新建Cookie
 
cookie.setMaxAge(Integer.MAX_VALUE);           // 设置生命周期为MAX_VALUE
 
response.addCookie(cookie);                    // 输出到客户端
```

如果maxAge为负数，则表示该Cookie仅在本浏览器窗口以及本窗口打开的子窗口内有效，关闭窗口后该Cookie即失效。maxAge为负数的Cookie，为临时性Cookie，不会被持久化，不会被写到Cookie文件中。Cookie信息保存在浏览器内存中，因此关闭浏览器该Cookie就消失了。Cookie默认的maxAge值为–1。

如果maxAge为0，则表示删除该Cookie。Cookie机制没有提供删除Cookie的方法，因此通过设置该Cookie即时失效实现删除Cookie的效果。失效的Cookie会被浏览器从Cookie文件或者内存中删除，

例如：

```
Cookie cookie = new Cookie("username","helloweenvsfei");   // 新建Cookie
 
cookie.setMaxAge(0);                          // 设置生命周期为0，不能为负数
 
response.addCookie(cookie);                    // 必须执行这一句
```

response对象提供的Cookie操作方法只有一个添加操作add(Cookie cookie)。

要想修改Cookie只能使用一个同名的Cookie来覆盖原来的Cookie，达到修改的目的。删除时只需要把maxAge修改为0即可。

注意：从客户端读取Cookie时，包括maxAge在内的其他属性都是不可读的，也不会被提交。浏览器提交Cookie时只会提交name与value属性。maxAge属性只被浏览器用来判断Cookie是否过期。

**1.1.8  Cookie的修改、删除**

Cookie并不提供修改、删除操作。如果要修改某个Cookie，只需要新建一个同名的Cookie，添加到response中覆盖原来的Cookie。

如果要删除某个Cookie，只需要新建一个同名的Cookie，并将maxAge设置为0，并添加到response中覆盖原来的Cookie。注意是0而不是负数。负数代表其他的意义。读者可以通过上例的程序进行验证，设置不同的属性。

注意：修改、删除Cookie时，新建的Cookie除value、maxAge之外的所有属性，例如name、path、domain等，都要与原Cookie完全一样。否则，浏览器将视为两个不同的Cookie不予覆盖，导致修改、删除失败。

**1.1.9  Cookie的域名**

Cookie是不可跨域名的。域名www.google.com颁发的Cookie不会被提交到域名www.baidu.com去。这是由Cookie的隐私安全机制决定的。隐私安全机制能够禁止网站非法获取其他网站的Cookie。

正常情况下，同一个一级域名下的两个二级域名如www.helloweenvsfei.com和images.helloweenvsfei.com也不能交互使用Cookie，因为二者的域名并不严格相同。如果想所有helloweenvsfei.com名下的二级域名都可以使用该Cookie，需要设置Cookie的domain参数，例如：

```
Cookie cookie = new Cookie("time","20080808"); // 新建Cookie
 
cookie.setDomain(".helloweenvsfei.com");           // 设置域名
 
cookie.setPath("/");                              // 设置路径
 
cookie.setMaxAge(Integer.MAX_VALUE);               // 设置有效期
 
response.addCookie(cookie);                       // 输出到客户端
```

读者可以修改本机C:\WINDOWS\system32\drivers\etc下的hosts文件来配置多个临时域名，然后使用setCookie.jsp程序来设置跨域名Cookie验证domain属性。

注意：domain参数必须以点(".")开始。另外，name相同但domain不同的两个Cookie是两个不同的Cookie。如果想要两个域名完全不同的网站共有Cookie，可以生成两个Cookie，domain属性分别为两个域名，输出到客户端。

**1.1.10  Cookie的路径**

domain属性决定运行访问Cookie的域名，而path属性决定允许访问Cookie的路径（ContextPath）。例如，如果只允许/sessionWeb/下的程序使用Cookie，可以这么写：

```
Cookie cookie = new Cookie("time","20080808");     // 新建Cookie
 
cookie.setPath("/session/");                          // 设置路径
 
response.addCookie(cookie);                           // 输出到客户端
```

设置为“/”时允许所有路径使用Cookie。path属性需要使用符号“/”结尾。name相同但domain相同的两个Cookie也是两个不同的Cookie。

注意：页面只能获取它属于的Path的Cookie。例如/session/test/a.jsp不能获取到路径为/session/abc/的Cookie。使用时一定要注意。

**1.1.11  Cookie的安全属性**

HTTP协议不仅是无状态的，而且是不安全的。使用HTTP协议的数据不经过任何加密就直接在网络上传播，有被截获的可能。使用HTTP协议传输很机密的内容是一种隐患。如果不希望Cookie在HTTP等非安全协议中传输，可以设置Cookie的secure属性为true。浏览器只会在HTTPS和SSL等安全协议中传输此类Cookie。下面的代码设置secure属性为true：

```
Cookie cookie = new Cookie("time", "20080808"); // 新建Cookie
 
cookie.setSecure(true);                           // 设置安全属性
 
response.addCookie(cookie);                        // 输出到客户端
```

​     提示：secure属性并不能对Cookie内容加密，因而不能保证绝对的安全性。**如果需要高安全性，需要在程序中对Cookie内容加密、解密，以防泄密。**

**1.1.12  JavaScript操作Cookie**

Cookie是保存在浏览器端的，因此浏览器具有操作Cookie的先决条件。浏览器可以使用脚本程序如JavaScript或者VBScript等操作Cookie。这里以JavaScript为例介绍常用的Cookie操作。例如下面的代码会输出本页面所有的Cookie。

<script>document.write(document.cookie);</script>

由于JavaScript能够任意地读写Cookie，有些好事者便想使用JavaScript程序去窥探用户在其他网站的Cookie。不过这是徒劳的，W3C组织早就意识到JavaScript对Cookie的读写所带来的安全隐患并加以防备了，W3C标准的浏览器会阻止JavaScript读写任何不属于自己网站的Cookie。换句话说，A网站的JavaScript程序读写B网站的Cookie不会有任何结果。

**1.1.13  setPath()、setDomain()**

正常的cookie只能在一个应用中共享，即一个cookie只能由创建它的应用获得。 

**i、可在同一应用服务器内共享方法：设置cookie.setPath(“/”);**

```
本机tomcat/webapp下面有两个应用：cas和webapp_b，
 
    1）原来在cas下面设置的cookie，在webapp_b下面获取不到，path默认是产生cookie的应用的路径。
 
    2）若在cas下面设置cookie的时候，增加一条cookie.setPath("/");或者cookie.setPath("/webapp_b/");就可以在webapp_b下面获取到cas设置的cookie了。
 
    3）此处的参数，是相对于应用服务器存放应用的文件夹的根目录而言的(比如tomcat下面的webapp)，因此cookie.setPath("/");之后，可以在webapp文件夹下的所有应用共享cookie，而cookie.setPath("/webapp_b/");是指cas应用设置的cookie只能在webapp_b应用下的获得，即便是产生这个cookie的cas应用也不可以。
 
    4）设置cookie.setPath("/webapp_b/jsp")或者cookie.setPath("/webapp_b/jsp/")的时候，只有在webapp_b/jsp下面可以获得cookie，在webapp_b下面但是在jsp文件夹外的都不能获得cookie。
 
    5）设置cookie.setPath("/webapp_b");，是指在webapp_b下面才可以使用cookie，这样就不可以在产生cookie的应用cas下面获取cookie了。
 
    6）有多条cookie.setPath("XXX");语句的时候，起作用的以最后一条为准。
```

**ii、跨域共享cookie的方法：设置cookie.setDomain(“.jszx.com”);**

```
A机所在的域：home.langchao.com,A应用：cas
B机所在的域：jszx.com，B应用：webapp_b
 
    1）在cas下面设置cookie的时候，增加cookie.setDomain(".jszx.com");，这样在webapp_b下面就可以取到cookie。
 
    2）这个参数必须以“.”开始。
 
    3）输入url访问webapp_b的时候，必须输入域名才能解析。比如说在A机器输入：http://lc-bsp.jszx.com:8080/webapp_b,可以获取cas在客户端设置的cookie，而B机器访问本机的应用，输入：http://localhost:8080/webapp_b则不可以获得cookie。
 
    4）设置了cookie.setDomain(".jszx.com");，还可以在默认的home.langchao.com下面共享。
```

通常，cookie却不能跨越域传递，只有那些创建它的域才能访问，同一根域名下的二级域名，三级域名可以直接共享。但你可以利用重定向来间接的获取cookies。

**1.1.14  案例：永久登录**

如果用户是在自己家的电脑上上网，登录时就可以记住他的登录信息，下次访问时不需要再次登录，直接访问即可。**实现方法是把登录信息如账号、密码等保存在Cookie中，并控制Cookie的有效期，下次访问时再验证Cookie中的登录信息即可。**

保存登录信息有多种方案。最直接的是把用户名与密码都保持到Cookie中，下次访问时检查Cookie中的用户名与密码，与数据库比较。**这是一种比较危险的选择，一般不把密码等重要信息保存到Cookie中。**

**还有一种方案是把密码加密后保存到Cookie中，下次访问时解密并与数据库比较。**这种方案略微安全一些。如果不希望保存密码，还可以把登录的时间戳保存到Cookie与数据库中，到时只验证用户名与登录时间戳就可以了。

这几种方案验证账号时都要查询数据库。

**本例将采用另一种方案，只在登录时查询一次数据库，以后访问验证登录信息时不再查询数据库。实现方式是把账号按照一定的规则加密后，连同账号一块保存到Cookie中。下次访问时只需要判断账号的加密规则是否正确即可。**本例把账号保存到名为account的Cookie中，把账号连同密钥用MD1算法加密后保存到名为ssid的Cookie中。验证时验证Cookie中的账号与密钥加密后是否与Cookie中的ssid相等。

```
代码1.8 loginCookie.jsp
 
<%@ page language="java"pageEncoding="UTF-8" isErrorPage="false" %>
 
<%!                                                  // JSP方法
 
    private static final String KEY =":cookie@helloweenvsfei.com";
                                                     // 密钥 
 
    public final static String calcMD1(Stringss) { // MD1 加密算法
 
       String s = ss==null ?"" : ss;                  // 若为null返回空
 
       char hexDigits[] = { '0','1', '2', '3', '4', '1', '6', '7', '8', '9',
       'a', 'b', 'c', 'd', 'e', 'f' };                        // 字典
 
       try {
 
        byte[] strTemp =s.getBytes();                          // 获取字节
 
        MessageDigestmdTemp = MessageDigest.getInstance("MD1"); // 获取MD1
 
       mdTemp.update(strTemp);                                // 更新数据
 
        byte[] md =mdTemp.digest();                        // 加密
 
        int j =md.length;                                 // 加密后的长度
 
        char str[] = newchar[j * 2];                       // 新字符串数组
 
        int k =0;                                         // 计数器k
 
        for (int i = 0; i< j; i++) {                       // 循环输出
 
         byte byte0 =md[i];
 
         str[k++] =hexDigits[byte0 >>> 4 & 0xf];
 
         str[k++] =hexDigits[byte0 & 0xf];
 
        }
 
        return newString(str);                             // 加密后字符串
 
       } catch (Exception e){return null; }
 
    }
 
%>
 
<%
 
   request.setCharacterEncoding("UTF-8");             // 设置request编码
 
    response.setCharacterEncoding("UTF-8");        // 设置response编码
 
   
 
    String action =request.getParameter("action"); // 获取action参数
 
   
 
    if("login".equals(action)){                       // 如果为login动作
 
        String account =request.getParameter("account");
                                                     // 获取account参数
 
        String password =request.getParameter("password");
                                                     // 获取password参数
 
        int timeout = newInteger(request.getParameter("timeout"));
                                                     // 获取timeout参数
 
              
 
        String ssid =calcMD1(account + KEY); // 把账号、密钥使用MD1加密后保存
 
       
 
        CookieaccountCookie = new Cookie("account", account);
                                                     // 新建Cookie
 
       accountCookie.setMaxAge(timeout);              // 设置有效期
 
       
 
        Cookie ssidCookie =new Cookie("ssid", ssid);   // 新建Cookie
 
       ssidCookie.setMaxAge(timeout);                 // 设置有效期
 
       
 
       response.addCookie(accountCookie);             // 输出到客户端
 
       response.addCookie(ssidCookie);            // 输出到客户端
 
       
 
        // 重新请求本页面，参数中带有时间戳，禁止浏览器缓存页面内容
 
       response.sendRedirect(request.getRequestURI() + "?" + System.
        currentTimeMillis());
 
        return;
 
    }
 
    elseif("logout".equals(action)){                  // 如果为logout动作
 
       
 
        CookieaccountCookie = new Cookie("account", "");
                                                 // 新建Cookie，内容为空
 
       accountCookie.setMaxAge(0);                // 设置有效期为0，删除
 
              
 
        Cookie ssidCookie =new Cookie("ssid", ""); // 新建Cookie，内容为空
 
       ssidCookie.setMaxAge(0);                   // 设置有效期为0，删除
 
       response.addCookie(accountCookie);         // 输出到客户端
 
       response.addCookie(ssidCookie);         // 输出到客户端
 
        //重新请求本页面，参数中带有时间戳，禁止浏览器缓存页面内容
 
       response.sendRedirect(request.getRequestURI() + "?" + System.
        currentTimeMillis());
 
        return;
 
    }
 
    boolean login = false;                        // 是否登录
 
    String account = null;                        // 账号
 
    String ssid = null;                           // SSID标识
 
   
 
    if(request.getCookies() !=null){               // 如果Cookie不为空
 
        for(Cookie cookie :request.getCookies()){  // 遍历Cookie
 
           if(cookie.getName().equals("account"))  // 如果Cookie名为
                                                    account
 
               account = cookie.getValue();       // 保存account内容
 
           if(cookie.getName().equals("ssid")) // 如果为SSID
 
               ssid = cookie.getValue();          // 保存SSID内容
 
        }
 
    }
 
    if(account != null && ssid !=null){    // 如果account、SSID都不为空
 
        login =ssid.equals(calcMD1(account + KEY));
                                      // 如果加密规则正确, 则视为已经登录
 
    }
 
%>
 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01Transitional//EN">
 
       <legend><%= login ? "欢迎您回来" : "请先登录"%></legend>
 
        <% if(login){%>
 
            欢迎您, ${ cookie.account.value }. &nbsp;&nbsp;
 
           <a href="${ pageContext.request.requestURI }?action=logout">
            注销</a>
 
        <% } else {%>
 
        <formaction="${ pageContext.request.requestURI }?action=login"
        method="post">
 
           <table>
 
               <tr><td>账号： </td>
 
                   <td><input type="text"name="account" style="width:
                   200px; "></td>
 
               </tr>
 
               <tr><td>密码： </td>
 
                   <td><inputtype="password" name="password"></td>
 
               </tr>
 
               <tr>
 
                   <td>有效期： </td>
 
                   <td><inputtype="radio" name="timeout" value="-1"
                   checked> 关闭浏览器即失效 <br/> <input type="radio" 
                   name="timeout" value="<%= 30 *24 * 60 * 60 %>"> 30天
                   内有效 <br/><input type="radio" name="timeout" value= 
                   "<%= Integer.MAX_VALUE %>"> 永久有效 <br/> </td> </tr>
 
               <tr><td></td>
 
                   <td><input type="submit"value=" 登  录 " class= 
                   "button"></td>
 
               </tr>
 
           </table>
 
        </form>
 
        <% } %>
```

​     登录时可以选择登录信息的有效期：关闭浏览器即失效、30天内有效与永久有效。通过设置Cookie的age属性来实现，注意观察代码。运行效果如图1.7所示。

![image.png](https://ucc.alicdn.com/pic/developer-ecology/f1288ff8f7264793b99d0b6d2b2abc76.png)

图1.7  永久登录

**提示：该加密机制中最重要的部分为算法与密钥。由于MD1算法的不可逆性，即使用户知道了账号与加密后的字符串，也不可能解密得到密钥。因此，只要保管好密钥与算法，该机制就是安全的。**







我们都知道银行的柜台每天要接待客户存款/取款业务，可以有几种方案：

凭借柜台职员的记忆，由柜台职员来为每位顾客办理存款/取款业务，单凭职员的记忆力，要记住每位顾客的相貌，并记录这个顾客当前的存款以及存取的次数，每次存取的金额是多少。

**-----------这种方式表示协议本身支持状态。**

使用存折的方式。柜台职员把每位顾客的存款/取款的信息保存在这张折子里，交给顾客保管，当顾客来存款/取款时，只要拿出存折，职员进行查看就对这位顾客的存款/取款信息一目了然。

当然，你马上会想到，顾客修改这个信息怎么办？我们也有措施对每次存款/取款记录后面盖章。无盖章的就是假冒信息。但如果顾客是真的要伪造，当然印章也是可以伪造的。

**-------------这种方式就是在客户端端保持状态。**

使用银行卡的方式，发给每位银行用户一张银行卡，银行卡上有一个唯一的卡号，没有其它任何信息，当顾客来存款/取款时，拿出银行卡，银行把卡号输入的电脑，很快就显示当前用户的存/取款记录。这种方式的安全性就会有很大的提高。用户想要做手脚，只有攻破银行的[服务器](https://cloud.tencent.com/act/pro/promotion-cvm?from=20067&from_column=20067)来修改自己的存/取款信息，这样做难度会很大。

**---------这种方式就是服务器端保持状态。**

Cookie与Session的产生过程

HTTP协议本身是无状态的，客户只需要简单的向服务器来发送请求下载某些文件，客户端向服务器端发送的每次请求都是独立的。对于当前的web应用，HTTP的“无状态”，导致许多应用都不得不花费大量的精力来记录用户的操作步骤。就像我们上面介绍的第一种情况，银行职员要花费大量的精力来记忆每一位用户的存/取款记录。

程序员很快发现，如果能够提供一些按需生成的动态信息，会使web的交互能力大大增强。程序员一方面在HTML中添加表单、脚本、DOM等客户端行为，来增加web应用与客户端的交互性。另一方面在服务器端则出现了CGI规范以响应客户端的动态请求，作为传输载体的HTTP协议添加了文件上载、cookie 等特性。那cookie的原理与我们上面介绍的使用存折记录用户行为的方式是一样的。

通过前面的例子我们已经发现，通过cookie的方式存储信息，可能会存在不安全性，因为所有的信息都是写在客户端的，客户可能会对这些信息进行修改或清除。然后就又出现session的方式用于保存用户信息的行为，这种方式的原理与前面介绍银行卡的方式是一样的。

具体来说，cookie机制采用的是在客户端保持状态的方案，而session机制采用的是在服务器端保持状态的方案。同时我们也看到，由于采用服务器端保持状态的方案在客户端也需要保存一个标识，所以session机制可能需要借助于cookie机制来达到保存标识的目的，但实际上它还有其他选择。

Cookie与Session的机制与原理

cookie机制

正统的cookie分发是通过扩展HTTP协议来实现的，服务器通过在HTTP的响应中加上一行特殊的指示以提示浏览器按照指示生成相应的cookie。然而纯粹的客户端脚本如JavaScript或者VBScript也可以生成cookie。而cookie的使用是由浏览器按照一定的原则在后台自动发送给服务器的。

浏览器检查所有存储的cookie，如果某个cookie所声明的作用范围大于等于将要请求的资源所在的位置，则把该cookie附在请求资源的HTTP请求头上发送给服务器。

cookie的内容主要包括：名字，值，过期时间，路径和域。路径与域一起构成cookie的作用范围。若不设置过期时间，则表示这个cookie的生命期为浏览器会话期间，关闭浏览器窗口，cookie就消失。这种生命期为浏览器会话期的cookie被称为会话cookie。

会话cookie一般不存储在硬盘上而是保存在内存里，当然这种行为并不是规范规定的。若设置了过期时间，浏览器就会把cookie保存到硬盘上，关闭后再次打开浏览器，这些cookie仍然有效直到超过设定的过期时间。存储在硬盘上的cookie可以在不同的浏览器进程间共享，比如两个IE窗口。而对于保存在内存里的cookie，不同的浏览器有不同的处理方式。

session机制

session机制是一种服务器端的机制，服务器使用一种类似于散列表的结构（也可能就是使用散列表）来保存信息。

当程序需要为某个客户端的请求创建一个session时，服务器首先检查这个客户端的请求里是否已包含了一个session标识------------称为session id，如果已包含则说明以前已经为此客户端创建过session，服务器就按照session id把这个session检索出来使用（检索不到，会新建一个），如果客户端请求不包含session id，则为此客户端创建一个session并且生成一个与此session相关联的session id，session id的值应该是一个既不会重复，又不容易被找到规律以仿造的字符串，这个session id将被在本次响应中返回给客户端保存。

保存这个session id的方式可以采用cookie，这样在交互过程中浏览器可以自动的按照规则把这个标识发给服务器。一般这个cookie的名字都是类似于SEEESIONID。但cookie可以被人为的禁止，则必须有其他机制以便在cookie被禁止时仍然能够把session id传递回服务器。

经常被使用的一种技术叫做URL重写，就是把session id直接附加在URL路径的后面。还有一种技术叫做表单隐藏字段。就是服务器会自动修改表单，添加一个隐藏字段，以便在表单提交时能够把session id传递回服务器。