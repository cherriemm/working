# Problems 



## Inspect HTML

查看网页源代码

![image-20240420150805257](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240420150805257.png)





## Search source

打开google 开发者模式 ，选中 top ，右键选择 " 在所有文件中搜索 " ，输入 picoCTF 得到flag 。

![image-20240420151130418](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240420151130418.png)



or 将整个网站的文件下载到本地再用 grep 查询

![image-20240422115208725](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422115208725.png)





![image-20240422120928485](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422120928485.png)



![image-20240422120648121](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422120648121.png)





## login

PicoCTF-Mini真题“login”
https://play.picoctf.org/practice/challenge/200?originalEvent=67&page=1&search=login





```js
(async()=>{
    await new Promise((e=>window.addEventListener("load", e))),
    document.querySelector("form").addEventListener("submit", (e=>{
        e.preventDefault();
        const r = {
            u: "input[name=username]",
            p: "input[name=password]"
        }
          , t = {};
        for (const e in r)
            t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, "");
        return "YWRtaW4" !== t.u ? alert("Incorrect Username") : "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" !== t.p ? alert("Incorrect Password") : void alert(`Correct Password! Your flag is ${atob(t.p)}.`)
    }
    ))
}
)();

```

**explanation**

- `btoa()`  : 对字符串进行base64编码 

- `.replace(/=/g, "")` 

  JavaScript RegExp `g` modifier

  - The `g` modifier specifies a global match. A global match finds all matches( not only the first match)

    Syntax :

    ```js
    new RegExp("regexp", "g")
    
    or simply:
    
    /regexp/g
    ```

  - common regular expression search methods

    - `text.match(pattern)`
    - `text.search(pattern)`
    - `pattern.exec(text)`
    - `pattern.test(text)`



## picobrowser

![image-20240425115652082](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240425115652082.png)



### user-agent

其实简单的说User-Agent就是客户端浏览器等应用程序使用的一种特殊的网络协议，在每次浏览器（邮件客户端/搜索引擎蜘蛛）进行 HTTP 请求时发送到服务器，服务器就知道了用户是使用什么浏览器来访问的。既然是人为规定的协议，那么就是说不管什么浏览器，默认的UA都是可以更改的。

**Change user agent to solve the problem**

- use burpsuite
- write a python script using 内置的`urllib`模块或第三方库`request`











## Cookies

![image-20240428115821718](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428115821718.png)



### burpsuite



- 初始状态， cookie header 还未设置， 可以看到 服务器端的 response header 设置 Set-Cookie `<cookie_name> = <cookie_value>` 

![image-20240428202600050](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428202600050.png)



- browser 收到服务器端的 set-cookie header， 设置自己的 cookie 并发送 GET 请求

![image-20240428202724617](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428202724617.png)



- 输入提示内容，发起 POST 请求 ，服务器端返回新的 cookie值

![image-20240428202517662](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428202517662.png)

And the browser will be redirected to another page PATH /check



- 根据收到的新 cookie值 ， 重新发起  GET 请求

![image-20240428202833477](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428202833477.png)



由上述分析可知，不同的输入值设置 服务器端的不同cookie值， 因此可以构造 GET 请求的 cookie ， 遍历破解( 可利用 intruder)



**设置 Payload type 为 Numbers**

![image-20240428204523055](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428204523055.png)



通过 settings->Grep-Match 过滤输出，( 需要注意的是 {} 需要转义 )

![image-20240428202227275](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428202227275.png)



**result**

![image-20240428204759863](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428204759863.png)





![image-20240428204910387](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428204910387.png)





### python scripts

```python
import requests

for in range(50):
    cookie = 'name={}'.format(i)
    headers = {'Cookie':cookie}
    
    r = requests.get('http://mercury.picoctf.net:<port>/check', headers=headers) # note the path
    
    if(r.status_code==200 and ('picoCTF' in r.text)):
        print(r.text)
```





```
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Cookies</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation"><a href="/reset" class="btn btn-link pull-right">Home</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Cookies</h3>
        </div>

        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}</code></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF</p>
        </footer>

    </div>
</body>

</html>
```









## more cookies

```python
import requests

from base64 import b64decode
from base64 import b64encode

original_cookie = b64decode('aTM5MThRaTMwalAxTGwrcjRlVjZCZnkybGVzWXJtbmxENlVQOFE5ZlZxd3dpU1FWc3lTc0hxWjZjOXhJY1JqSW1GRlZnK0pOTlV3clBSNWx0bmp1T2JDclgvMFZTb1ducHJESzBacURDblUxVTAxYmUyem9TYWJINzd4SWJjNkQ=')
original_cookie = bytearray(original_cookie)

def bitFlip(cookie_char_pos: int, bit_pos: int) -> str:
    altered_cookie = bytearray(original_cookie)

    flipped = altered_cookie[cookie_char_pos] ^ bit_pos

    altered_cookie[cookie_char_pos] = flipped
    altered_cookie_b64 = b64encode(altered_cookie)

    return altered_cookie_b64.decode("utf-8")



for cookie_char_pos in range(len(original_cookie)):
    print(f"checking cookie position {cookie_char_pos}")
    for bit_pos in range(128):
        altered_cookie = bitFlip(cookie_char_pos, bit_pos)
        cookies = {'authname':altered_cookie}
        r = requests.get("http://mercury.picoctf.net:21553/", cookies=cookies)
        if("picoCTF{" in r.text):
            print(r.text)
```





![image-20240501223533656](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240501223533656.png)



### base64 module

This module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data. It provides encoding and decoding functions for the encodings specified in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html), which defines the Base16, Base32, and Base64 algorithms



There are two interfaces provided by this module. The modern interface supports encoding [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) to ASCII [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), and decoding [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) or strings containing ASCII to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)



#### `bytes-like object`

An object that supports the [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects) and can export a C-[contiguous](https://docs.python.org/3/glossary.html#term-contiguous) buffer. This includes all [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray), and [`array.array`](https://docs.python.org/3/library/array.html#array.array) objects, as well as many common [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview) objects. Bytes-like objects can be used for various operations that work with binary data; these include compression, saving to a binary file, and sending over a socket.





#### `base64.base64encode(s, altchars=None)`

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) *s* using Base64 and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes).

Optional *altchars* must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) of length 2 which specifies an alternative alphabet for the `+` and `/` characters. This allows an application to e.g. generate URL or filesystem safe Base64 strings. The default is `None`, for which the standard Base64 alphabet is used.





#### `base64.b64decode(s, altchars=None, validate=False)`

Decode the Base64 encoded bytes-like object or ASCII string *s* and return the decoded bytes







# HTTP



## HTTP Cookies

Cookies are little text-based files that are kept on the user's computer and are accessible only by that user's browser. It is possible for a cookie's size to reach a maximum of 4 KB. 

It remembers stateful information for the [stateless](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#http_is_stateless_but_not_sessionless) HTTP protocol.



**Cookies are mainly used for three purposes:**

- Session management

  Logins, shopping carts, game scores, or anything else the server should remember

- Personalization

  User preferences, themes, and other settings

- Tracking

  Recording and analyzing user behavior



Modern APIs for client storage are the [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) (`localStorage` and `sessionStorage`) and [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).



### The `Set-Cookie` and `Cookie` headers

The [`Set-Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) HTTP response header sends cookies from the server to the user agent. A simple cookie is set like this:

```http
Set-Cookie: <cookie-name>=<cookie-value>
```



example:

```http
HTTP/2.0 200 OK
Content-Type: text/html
Set-Cookie: yummy_cookie=choco
Set-Cookie: tasty_cookie=strawberry

[page content]
```

Then, with every subsequent request to the server, the browser sends all previously stored cookies back to the server using `Cookie` header.

```http
GET /sample_page.html HTTP/2.0
Host: www.example.org
Cookie: yummy_cookie=choco; tasty_cookie=strawberry
```







### lifetime 

Cookies can persist for two different periods, depending on the attributes used with the `Set-Cookie` header 



- *Permanent* cookies are deleted at a date specified by the `Expires`  or  `Max-Age` attribute.

- *Session* cookies – cookies without a `Max-age` or `Expires` attribute – are deleted when the current session ends. The browser defines when the "current session" ends, and some browsers use *session restoring* when restarting. This can cause session cookies to last indefinitely.

  If your site authenticates users, it should regenerate and resend session cookies, even ones that already exist, whenever a user authenticates. This approach helps prevent [session fixation attacks](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#session_fixation), where a third party can reuse a user's session.



### Restrict access to cookies

ensure that cookies are sent securely and aren't accessed by unintended parties or scripts in one of two ways: 

-   `Secure` attribute
-   `HttpOnly` attribute.



**`Secure`**

A cookie with the `Secure` attribute is only sent to the server with an encrypted request over the HTTPS protocol.

It's never sent with unsecured HTTP (except on localhost), which means [man-in-the-middle](https://developer.mozilla.org/en-US/docs/Glossary/MitM) attackers can't access it easily. 

 Insecure sites (with `http:` in the URL) can't set cookies with the `Secure` attribute. However, don't assume that `Secure` prevents all access to sensitive information in cookies. For example, someone with access to the client's hard disk (or JavaScript if the `HttpOnly` attribute isn't set) can read and modify the information.



**`HttpOnly`**

A cookie with the `HttpOnly` attribute is inaccessible to the JavaScript [`Document.cookie`](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie) API; it's only sent to the server. 

 For example, cookies that persist in server-side sessions don't need to be available to JavaScript and should have the `HttpOnly` attribute. This precaution helps mitigate cross-site scripting ([XSS](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#cross-site_scripting_xss)) attacks.





```http
Set-Cookie: id=a3fWa; Expires=Thu, 21 Oct 2021 07:28:00 GMT; Secure; HttpOnly
```





### Define where cookies are sent

The `Domain` and `Path` attributes define the *scope* of a cookie: what URLs the cookies should be sent to.



**`Domain`**

The `Domain` attribute specifies which server can receive a cookie.

If specified, then cookies are available on the server and its subdomains. For example, if you set `Domain=mozilla.org`, cookies are available on mozilla.org and its subdomains like `developer.mozilla.org`.

If the server does not specify a `Domain`, the cookies are available on the server *but not on its subdomains*. 



**`Path`**

The `Path` attribute indicates a URL path that must exist in the requested URL in order to send the `Cookie` header.

- default value

  If the `Path` attribute is not set, its default value is computed from the [path](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#path_to_resource) of the URI that set the cookie

  - If the path is empty, does not start with `"/"`, or contains no more than one `"/"` character, then the default value for `Path` is `"/"`.
  - Otherwise, the default value for `Path` is the path from the start up to but not including the final `"/"` character.

  example, if the cookie was set from `"https://example.org/a/b/c`, then the default value of `Path` would be `"/a/b"`.



### SameSite attribute

The [`SameSite`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#samesitesamesite-value) attribute lets servers specify whether/when cookies are sent with cross-site requests (where [Site](https://developer.mozilla.org/en-US/docs/Glossary/Site) is defined by the registrable domain and the *scheme*: http or https). This provides some protection against cross-site request forgery attacks ([CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)). It takes three possible values: `Strict`, `Lax`, and `None`.

With `Strict`, the browser only sends the cookie with requests from the cookie's origin site. `Lax` is similar, except the browser also sends the cookie when the user *navigates* to the cookie's origin site (even if the user is coming from a different site). For example, by following a link from an external site. `None` specifies that cookies are sent on both originating and cross-site requests, but *only in secure contexts* (i.e., if `SameSite=None` then the `Secure` attribute must also be set). If no `SameSite` attribute is set, the cookie is treated as `Lax`.



## Session 

pass the session IDs as **a parameter in URLs or store them in the cookies**. 



**Usage**

- display a user’s preferences throughout the site. 
-  remember shopping cart  between pages
-  implement security measures and perform certain actions.



**How Do Web Sessions Work**

![image-20240502094209124](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502094209124.png)



**Difference between Cookies and Session**

| Session                                                      | Cookies                                                      |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| A session stores the variables and their values within a file in a temporary directory on the server. | Cookies are stored on the user's computer as a text file.    |
| The session ends when the user logout from the application or closes his web browser. | Cookies end on the lifetime set by the user.                 |
| It can store an unlimited amount of data.                    | It can store only limited data.                              |
| We can store as much data as we want within a session, but there is a maximum memory limit, which a script can use at one time, and it is 128 MB. | The maximum size of the browser's cookies is 4 KB.           |
| We need to call the session_start() function to start the session. | We don't need to call a function to start a cookie as it is stored within the local computer. |
| In PHP, to destroy or remove the data stored within a session, we can use the session_destroy() function, and to unset a specific variable, we can use the unset() function. | We can set an expiration date to delete the cookie's data. It will automatically delete the data at that specific time. There is no particular function to remove the data. |
| Sessions are more secured compared to cookies, as they save data in encrypted form. | Cookies are not secure, as data is stored in a text file, and if any unauthorized user gets access to our system, he can temper the data. |













# Guide to Developer Tools

https://developer.chrome.com/docs/devtools/overview?hl=zh-cn

## The tabs are:

- Elements : shows you the HTML used to build the page you’re looking at, together with any inline CSS.
- Console : deals with JavaScript. It gives you information about interactive elements on a page. In Console, you can write JavaScript to interact with the web page you’re viewing, and it also lets you write messages to yourself in the JavaScript of websites you’re building, which then show up in Console to show that the JS was executed.
- Source : shows you where all the files that were used to make the website are stored and lets you inspect them.
- Network : shows you all the files that are loading in the URL you’re looking at . You get a waterfall and deep data on all the items loaded, including initiator and time to load that element.
- Application : shows you what’s in your browser storage: in-browser databases like Web SQL, local storage, and more. It also gives you granular control over your cookies.
- Security
- Memory
- Performance
- Audits



**Important**:

You can’t change the code on the website with Developer Tools. You’d need access to the site’s backend for that. Only the code your browser uses to display the website is changed. So even if you’re a total beginner, you can do anything you like with Developer Tools with no real risk. Close the window, go back to the website, and everything is the same as it was before.



**How to open Chrome Developer Tools**



1. The keyboard shortcuts are:

   - Mac OS: **CMD+Shift+J** or **CMD+Shift+C**

   - Linux, Chromebook and Windows: **Ctrl+Shift+J**

2. From the Chrome menu:

   Open the Chrome menu and go to “More Tools” > “Developer Tools.”

3. right-click (Windows) or Ctrl-click (Mac) anything on a web page and select “Inspect Element” to open Developer Tools.



# burpsuite



## Tools

**modify HTTP requests**

https://portswigger.net/burp/documentation/desktop/getting-started/modifying-http-requests



### **target**

https://portswigger.net/burp/documentation/desktop/tools/target

The target scope tells Burp exactly which URLs and hosts you want to test. This enables you to filter out the noise generated by your browser and other sites, so you can focus on the traffic that you're interested in.



#### Site map

The site map shows the information that Burp collects as you explore your target application. It builds a hierarchical representation of the content from a number of sources. These include information from scans, and the URLs you discover as you browse the target manually. You can also see:

- A list of the contents.
- Full requests and responses for individual items.
- Full information about any security issues that Burp discovers.



### Intruder

performing highly customizable, automated attacks against websites. It enables you to configure attacks that send the same request over and over again, inserting different payloads into predefined positions each time. Among other things, you can use Intruder to:

- Fuzz for input-based vulnerabilities.
- Perform brute-force attacks.
- Enumerate valid identifiers and other inputs.
- Harvest useful data.

https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses



- configure your attack to enumerate a huge variety of identifiers, for example:

  - Enumerate usernames - Use the username generator payload type to insert a long list of possible usernames into an application's login failure message.

  - Enumerate passwords - Use the simple list payload type to insert a set of common passwords into an application's login failure message, alongside known valid usernames.

  - Enumerate order IDs - Use the custom iterator payload type to cycle through potential order IDs in a known format. You can then use these to view order details.

  - Enumerate session tokens - Use the bit flipper payload type to systematically modify a token that has been encrypted using a CBC cipher, to try to meaningfully tamper with its decrypted value.





#### **example :**

![image-20240428161015073](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428161015073.png)



1. `GET /`

   ```http
   GET / HTTP/1.1
   Host: 0aa0000e037c1b1b807bee3c00060046.web-security-academy.net
   Upgrade-Insecure-Requests: 1
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
   Sec-Fetch-Site: cross-site
   Sec-Fetch-Mode: navigate
   Sec-Fetch-User: ?1
   Sec-Fetch-Dest: document
   Sec-Ch-Ua: "Chromium";v="123", "Not:A-Brand";v="8"
   Sec-Ch-Ua-Mobile: ?0
   Sec-Ch-Ua-Platform: "Windows"
   Referer: https://portswigger.net/
   Accept-Encoding: gzip, deflate, br
   Accept-Language: zh-CN,zh;q=0.9
   Priority: u=0, i
   Connection: close
   ```

Response :

```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Set-Cookie: session=neOMJZ80oLRUkvOqqAo9VCzwBVc7g2Dh; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 8384

content ...
```



2. `GET /login`

   ```http
   GET /login HTTP/2
   Host: 0aa0000e037c1b1b807bee3c00060046.web-security-academy.net
   Cookie: session=neOMJZ80oLRUkvOqqAo9VCzwBVc7g2Dh
   Upgrade-Insecure-Requests: 1
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
   Sec-Fetch-Site: same-origin
   Sec-Fetch-Mode: navigate
   Sec-Fetch-User: ?1
   Sec-Fetch-Dest: document
   Sec-Ch-Ua: "Chromium";v="123", "Not:A-Brand";v="8"
   Sec-Ch-Ua-Mobile: ?0
   Sec-Ch-Ua-Platform: "Windows"
   Referer: https://0aa0000e037c1b1b807bee3c00060046.web-security-academy.net/
   Accept-Encoding: gzip, deflate, br
   Accept-Language: zh-CN,zh;q=0.9
   Priority: u=0, i
   
   
   ```

   response

   ```http
   HTTP/2 200 OK
   Content-Type: text/html; charset=utf-8
   X-Frame-Options: SAMEORIGIN
   Content-Length: 3075
   ```

   

3. `POST /login`

   ```http
   POST /login HTTP/2
   Host: 0aa0000e037c1b1b807bee3c00060046.web-security-academy.net
   Cookie: session=neOMJZ80oLRUkvOqqAo9VCzwBVc7g2Dh
   Content-Length: 29
   Cache-Control: max-age=0
   Sec-Ch-Ua: "Chromium";v="123", "Not:A-Brand";v="8"
   Sec-Ch-Ua-Mobile: ?0
   Sec-Ch-Ua-Platform: "Windows"
   Upgrade-Insecure-Requests: 1
   Origin: https://0aa0000e037c1b1b807bee3c00060046.web-security-academy.net
   Content-Type: application/x-www-form-urlencoded
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
   Sec-Fetch-Site: same-origin
   Sec-Fetch-Mode: navigate
   Sec-Fetch-User: ?1
   Sec-Fetch-Dest: document
   Referer: https://0aa0000e037c1b1b807bee3c00060046.web-security-academy.net/login
   Accept-Encoding: gzip, deflate, br
   Accept-Language: zh-CN,zh;q=0.9
   Priority: u=0, i
   
   username=wiener&password=xccc
   ```



4. use intruder

   ![image-20240428163701471](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428163701471.png)

![image-20240428170759962](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428170759962.png)



















**reissue requests** 

This lets you study the target website's response to different input without having to intercept the request each time.





















# python lib

```python
import urllib.request
import json

url = 'http://example.com/api/data'
data = {'key': 'value'}

# 将数据编码为 JSON 格式
data = json.dumps(data).encode('utf-8')

req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print(result)
```





```python
import requests
import json

url = 'http://example.com/api/data'
data = {'key': 'value'}

# 发送 POST 请求并将 JSON 数据传递给 data 参数
response = requests.post(url, json=data)

# 打印响应内容
print(response.text)
```







# Flask



## Flask-session



### Introduction

- **Client-side vs Server-side sessions**

  - **Client-side sessions** store session data in the client’s browser. This is done by placing it in a cookie that is sent to and from the client on each request and response. This can be any small, basic information about that client or their interactions for quick retrieval 

  - **Server-side sessions** storing session data in server-side . A cookie is also used, but it only contains the session identifier that links the client to their corresponding data on the server.



**Flask-Session sequence diagram**

![sequence diagram for flask-session](https://flask-session.readthedocs.io/en/latest/_images/sequence.webp)



### modify session data

https://overiq.com/flask-101/sessions-in-flask/

When we use sessions the data is stored in the browser as a cookie. The cookie used to store session data is known session cookie. However, unlike an ordinary cookie, Flask Cryptographically signs the session cookie. It means that anyone can view the contents of the cookie, but can't modify the cookie unless he has the secret key used to sign the cookie.

That's why it is recommended to set a long and hard to guess string as a secret key. Once the session cookie is set, every subsequent request to the server verifies the authenticity of the cookie by unsigning it using the same secret key. If Flask fails to unsign the cookie then its content is discarded and a new session cookie is sent to the browser.



**PHP vs Flask**

 In PHP, session cookie doesn't store session data instead it only stores a session id. The session id is a unique string PHP creates to associate session data with the cookie. The session data itself is stored on the server in a file. Upon receiving a request from the client, PHP uses the session id to retrieve session data and makes it available in your code. This type of sessions is known as server-side sessions and type of sessions Flask provides by default is known as client-side sessions.

By default, there isn't much difference between cookies and client-based sessions in Flask. As a result, the client-based sessions suffer from the same drawbacks the cookies have like:

- Can't store sensitive data like passwords.
- Additional payload on every request.
- Can't store data more than 4KB.
- Limit on the number of cookie per website and so on.

The only real difference between cookies and the client-based session is that Flask guarantees that the contents of the session cookie is not tempered by the user (unless he has the secret key).

If you want to use server-side sessions in Flask, you can either write your own session interface or use extensions like Flask-Session and Flask-KVSession.



```python
@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return "Total visits: {}".format(session.get('visits'))

@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)
    return 'Visits deleted'
```











### Session object

Assign session IDs to sessions for each client. Session data is stored at the top of the cookie, and the server signs it in encrypted mode.For this encryption, the Flask application requires a defined `SECRET_KEY`.



- A Session object is a dictionary object that contains key value pairs for session variables and associated values. `session['username'] = 'admin'`

- To release a session variable, use the `pop()` method.

  `session.pop('username', None)`



example:

```python
@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"


@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
```



Run the application and access the home page.(Ensure that the application’s secrett_key is set)

```
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)
app.secret_key = 'any random string’
```



