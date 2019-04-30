"""
模式修正符：所谓模式修正符，即可以在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，
从而实现一些匹配结果的调整等功能


I   匹配时忽略大小写
M   多行匹配
L   做本地化识别匹配
U   根据Unicode字符及解析字符
S   让.匹配包括换行符，即用了该模式后.可以匹配任意字符
"""
import re
pattern1 = "python"
pattern2 = "python"
string = "abcdfphp345Python_py"

# 匹配的时候区分大小写，所以不会匹配到任何东西
result1 = re.search(pattern1, string)  # 将不会匹配到任何东西
# 匹配的时候忽略大小写，所以会匹配到python
result2 = re.search(pattern2, string, re.I)  # 将会匹配到None
print(result1)
print(result2)


