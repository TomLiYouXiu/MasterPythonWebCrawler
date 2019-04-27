# 要使用Urllib爬取网页，必须先导入对应的模块
import urllib.request
# 导入模块之后，我们需要使用urllib.request.urlopen()打开并爬取一个网页,
# 将爬取到的网页存放到变量file中
file = urllib.request.urlopen("http://www.baidu.com")
# 将对应网页中的内容提取出来，可以使用file.read()读取全部内容
print(file.read())
# 或者也可以使用file.readline()读取一行内容
print(file.readline())
# 读取网页的全部内容到列表,如果要读取全部内容，推荐使用这种方式
print(file.readlines())
