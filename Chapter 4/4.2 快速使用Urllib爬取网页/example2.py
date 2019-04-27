# @TODO 1. 首先 爬取一个网页并将爬取到的内容读取出来赋值给一个变量
import urllib.request
URL = "https://www.baidu.com"
file = urllib.request.urlopen(URL)
data = file.read()
# @TODO 2. 以写入的方式打开一个本地文件，命名为.html文件
fhandle = open('1.html', 'wb')
# @TODO 3. 将1中的变量中的内容写入到2中的文件
fhandle.write(data)
# @TODO 4. 关闭该文件
fhandle.close()