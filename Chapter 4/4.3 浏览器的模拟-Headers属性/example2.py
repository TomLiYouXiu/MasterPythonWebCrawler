# 方法2：使用add_headers()添加报头
import urllib.request
# 1. 首先设置要爬取的网址
url = "http://www.baidu.com"
# 2. urllib.request.Request(url)创建一个Request对象并且赋值给变量req
req = urllib.request.Request(url)
# 3. req对象使用add_header()方法添加对应的报头信息，格式为 req对象.add_header(字段名，字段值)
req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
# 4. 使用设置好的req对象打开url链接，此时将会打开并读取网页内容赋值给data变量
data = urllib.request.urlopen(req).read()
print(data)