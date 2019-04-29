"""
普通字符作为原子
"""
# 要使用正则表达式，所以就要导入re模块
import re
# 导入re模块之后，我们要设置正则表达式
pattern = "yue"
# 定义了一串字符串
string = "http://yum.iqianyue.com"
# 从字符串string中去匹配对应的正则表达式，若匹配成功，将匹配结果返回给result
result = re.search(pattern, string)
print(result)
