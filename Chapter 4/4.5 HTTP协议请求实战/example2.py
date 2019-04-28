import urllib.request
keyword = input('请输入你要查找的关键词：')
# 处理输入中文编码有问题
keyword = urllib.request.quote(keyword)
print(keyword)
url = 'http://www.baidu.com/s?wd=' + keyword
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
print(data)
