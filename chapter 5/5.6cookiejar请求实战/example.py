"""
无cookie处理的登录
"""


import urllib.request
import urllib.parse
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q"
postdata = urllib.parse.urlencode({
    "username" : "weisuen",
    "password" : "aA123456"
}).encode("utf-8")  # 使用urlencode编码处理后，再设置为utf-8编码
req = urllib.request.Request(url, postdata)  #构建Request对象
req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
data = urllib.request.urlopen(url).read()  # 登录并爬取网页
fhandle = open('./1.html', 'wb')
fhandle.write(data)
fhandle.close()
url2 = "http://bbs.chinaunix.net/"  # 设置要爬取的该网站下其他网站网址
req2 = urllib.request.Request(url2, postdata)
req2.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
data2 = urllib.request.urlopen(req2).read()  #爬取该网站下的其他网页
fhandle = open('./2.html', 'wb')
fhandle.write(data2)
fhandle.close()