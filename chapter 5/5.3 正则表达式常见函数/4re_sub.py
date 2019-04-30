"""
如果我们想要根据正则表达式来实现某些字符的替换功能，可以使用re.sub()来实现
re.sub(pattern, rep, string, max)
    pattern: 对应的正则表达式
    rep: 要替换成的字符串
    string: 源字符串
    max: 可选项，代表最多替换的次数，如果忽略不写，会把符合模式的全部替换
"""

import re
string = "hellom1ispythonourpythonend"
pattern = ".python."
result1 = re.sub(pattern, "php", string)
result2 = re.sub(pattern, "php", string, 2)
print(result1)
print(result2)