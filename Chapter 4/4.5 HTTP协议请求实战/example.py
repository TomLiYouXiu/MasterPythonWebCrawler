# 使用get请求模拟百度搜索关键词
import urllib.request
keywd = "hello"
url = "http://www.baidu.com/s?wd=" + keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhandle = open('1.html', 'wb+')
fhandle.write(data)
fhandle.close()
