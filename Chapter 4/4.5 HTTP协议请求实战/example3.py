#!encoding=utf-8
# POST请求案例分析
import urllib.request
import urllib.parse
# 设置URL
url = "http://www.iqianyue.com/mypost/"
# 构建表单数据，并使用urllib.parse.urlencode进行编码处理
postdata = urllib.parse.urlencode({
	"name": "yirufeng",
	"pass": "我是CEO"
}).encode('utf-8')  #将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
# 构建Request对象，参数包括URL地址和要传递的数据
req = urllib.request.Request(url, postdata)
# 使用add_header()添加头信息，模拟浏览器进行爬取
req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
# 使用urllib.requests.urlopen()打开对应的Request对象，完成信息的传递
data = urllib.request.urlopen(req).read()
# 后续处理，比如读取网页内容，将内容写入文件
fhandle = open('./post_test.html', 'wb+')
fhandle.write(data)
fhandle.close()
