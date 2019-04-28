import urllib.request

# 1. 分别使用urllib.request.HTTPHandler()和urllib.reqeust.HTTPSHandler()将debuglevel设置为1
httphd = urllib.request.HTTPHandler(debuglevel=1)
# 2. 使用urllib.request.build_opener()创建自定义的opener对象，并使用1中设置的值作为参数
httpshd = urllib.request.HTTPSHandler(debuglevel=1)
# 3. 使用urllib.request.install_opener()创建全局默认的opener对象，这样使用urlopen()时
# 也会使用我们安装的opener对象
opener = urllib.request.build_opener(httphd, httpshd)
urllib.request.install_opener(opener)
# 4. 进行后续的操作，例如urlopen()等
data = urllib.request.urlopen("http://edu.51cto.com")


"""
有时候我们需要在程序运行过程中，边运行便打印调试信息，此时需要开启DebugLog
"""