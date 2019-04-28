import urllib.request
# 要使用URLError类，必须先导入urllib.error模块
import urllib.error
try:
    urllib.request.urlopen("https://itbook.download/")
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)
