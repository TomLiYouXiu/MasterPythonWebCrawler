import urllib.request
URL = "https://www.baidu.com"
data = urllib.request.urlopen(URL).read()
with open('baidu_content.html', 'wb+') as f:
    f.write(data)

