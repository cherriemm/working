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



**`bytes-like object`**

An object that supports the [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects) and can export a C-[contiguous](https://docs.python.org/3/glossary.html#term-contiguous) buffer. This includes all [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray), and [`array.array`](https://docs.python.org/3/library/array.html#array.array) objects, as well as many common [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview) objects. Bytes-like objects can be used for various operations that work with binary data; these include compression, saving to a binary file, and sending over a socket.





**`base64.base64encode(s, altchars=None)`**

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) *s* using Base64 and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes).

Optional *altchars* must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) of length 2 which specifies an alternative alphabet for the `+` and `/` characters. This allows an application to e.g. generate URL or filesystem safe Base64 strings. The default is `None`, for which the standard Base64 alphabet is used.





**`base64.b64decode(s, altchars=None, validate=False)`**

Decode the Base64 encoded bytes-like object or ASCII string *s* and return the decoded bytes





### Block cipher mode of operation

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











## most cookies

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



### Analyses

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



![image-20240502202757928](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502202757928.png)













### JWT

**JSON Web Token**is a proposed Internet standard for creating data with optional signature and/or optional encryptionwhose payload holds [JSON](https://en.wikipedia.org/wiki/JSON) that asserts some number of claims. The tokens are signed either using a private secret or a public/private key.

For example, a server could generate a token that has the claim "logged in as administrator" and provide that to a client. The client could then use that token to prove that it is logged in as admin. The tokens can be signed by one party's private key (usually the server's) so that any party can subsequently verify whether the token is legitimate.



#### Structure

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





#### Base64URL

Header 和 Payload 串型化的算法是 Base64URL。这个算法跟 Base64 算法基本类似，但有一些小的不同。

JWT 作为一个令牌（token），有些场合可能会放到 URL（比如 api.example.com/?token=xxx）。Base64 有三个字符`+`、`/`和`=`，在 URL 里面有特殊含义，所以要被替换掉：`=`被省略、`+`替换成`-`，`/`替换成`_` 。这就是 Base64URL 算法。

- `base64.standard_b64decode(s)`

  Decode bytes-like object or ASCII string *s* using the standard Base64 alphabet and return the decoded bytes

- `base64.urlsafe_b64encode(s)`

  Encode bytes-like objects using the URL- and filesystem-safe alphabet, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the encoded bytes. The result can still contain` =`.

![image-20240502193128066](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240502193128066.png)

3 `=` is always a safe padding.





#### Practices

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



# js obfuscation



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
