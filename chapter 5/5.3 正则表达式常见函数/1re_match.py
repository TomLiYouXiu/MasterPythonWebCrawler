"""
re.match()函数:从字符串的起始位置开始进行匹配，如果遇到一个不符合就返回None

re.match(pattern, string, flag)
    pattern:代表对应的正确表达式
    string:代表对应的源字符
    flag:代表对应的标志位，用来放模式修正符等信息
"""

import re
string = "apythonhellomypythonhispythonourpythonend"
pattern = ".python."

"""
如果string = "aPythonhellomypythonhispythonourpythonend", result将会返回None
因为string中第2个字符P不匹配
"""
result = re.match(pattern, string)

# 通过span()函数可以过滤掉一些信息，只留下匹配成功的结果在源字符串的位置
result2 = re.match(pattern, string, re.I).span()
print(result)
print(result2)


