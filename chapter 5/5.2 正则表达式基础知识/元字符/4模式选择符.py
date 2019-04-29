"""
模式选择符：|
"""
import re
pattern = "python|php"  # 可以设置多个模式，将会匹配python或php
string = "abcdfphp345pythony_py"
result = re.search(pattern, string)
print(result)