import urllib.request

# url = "http://blog.csdn.com/weiwei_pig/article/details/51178226"
# 定义要爬取的地址
url = "http://www.baidu.com"
file = urllib.request.urlopen(url).read()
print(file)
# 定义一个变量存储对应的Users-Agent信息，格式为("User-Agent", 具体信息)
headers = ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
# 创建自定义的opener对象并赋值给变量opener
opener = urllib.request.build_opener()
# 设置opener对象的addheaders，即设置对应的头信息
opener.addheaders = [headers]
# 设置好头部信息，就可以使用opener对象的open()方法打开对应的网址
# 此时，将会采用刚才添加的头部信息模拟浏览器打开网站
data = opener.open(url).read()
print(data)


# with open('1.html', 'wb+') as f:
#     f.write(urllib.request.urlopen(url).read())
#
# urllib.request.urlretrieve(url, '2.html')