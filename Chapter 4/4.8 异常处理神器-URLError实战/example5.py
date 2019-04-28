"""
在下面的代码中，我们首先对子类进行异常处理，若无法处理，再使用父类进行异常处理，
此时，不管发生哪种异常，都可以进行处理
"""
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.baidusss.net")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)