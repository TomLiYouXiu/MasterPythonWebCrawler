"""
匹配.com或.cn后缀的URL网站

目的：将一串字符串里面以.com或.cn为域名后缀的URL网址匹配出来，过滤掉其他无关信息
"""
import re
# 自己写的代码
# pattern = "^\w*.c[(om)n]"
# 书上代码
pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern, string)
print(result)
