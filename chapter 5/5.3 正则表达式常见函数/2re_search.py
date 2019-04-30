"""
re.search(pattern, string, flag)
    pattern:代表对应的正确表达式
    string:代表对应的源字符
    flag:代表对应的标志位，用来放模式修正符等信息

re.search()与re.match()最大不同就是：
    search会扫描整个字符串进行匹配，也就是在全文中进行检索和匹配，
    而match是从字符串的开始进行匹配的
"""

import re
string = "hellomypythonhispythonourpythonend"
pattern = ".python."
result = re.match(pattern, string)
result2 = re.search(pattern, string)
print(result)
print(result2)


