def use_proxy(proxy_addr, url):
    """
    自定义一个函数：主要实现使用代理服务器来爬取某个URL网页的功能
    :param proxy_addr:  代理服务器的地址
    :param url:         爬取网页的地址
    :return:
    """
    import urllib.request
    # urllib.request.ProxyHandler设置对应的代理服务器信息
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    # 创建一个自定义的opener()对象
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    # 为了方便，可以使用下面这行代码创建全局默认的opener对象
    # 那么在使用urlopen()将会使用我们安装的opener对象
    urllib.request.install_opener(opener)
    # 使用上面安装的opener对象打开对应网址爬取网页并读取
    data = urllib.request.urlopen(url).read().decode('utf-8')
    # 返回爬取到的数据
    return data


proxy_addr = '171.37.158.177:8123'
data = use_proxy(proxy_addr, 'http://www.baidu.com')
print(len(data))