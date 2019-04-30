"""
使用cookie登录网站

1. 导入cookie处理模块http.cookiejar
2. 使用http.cookiejar.CookieJar()创建CookieJar对象
3. 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
4. 创建全局默认的opener对象
"""
import http.cookiejar
import urllib.request
import urllib.parse
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q"
postdata = urllib.parse.urlencode({
    "username" : "weisuen",
    "password" : "aA123456"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
# 使用http.cookiejar.CookieJar()创建CookieJar对象
cjar = http.cookiejar.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 将opener安装为全局
urllib.request.install_opener(opener)
file = opener.open()
data = file.read()
file = open("./3.html", "wb")
file.write(data)
file.close()
url2 = "http://bbs.chinaunix.net"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("./4.html", "wb")
fhandle.write(data2)
fhandle.close()
