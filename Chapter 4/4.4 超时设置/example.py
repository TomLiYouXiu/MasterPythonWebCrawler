import urllib.request
url = "http://www.google.com.hk"
for i in range(1, 100):
    try:
        # 超时设置为1秒钟，即1秒钟未响应则判定超时，并读取该网站的内容，输出获取到内容的长度
        file = urllib.request.urlopen(url, timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常" + str(e))
