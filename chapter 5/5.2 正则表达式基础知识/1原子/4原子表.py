"""
原子表
在python中，原子表由[]表示
[xyz]py 就会匹配 xpy或ypy或zpy
[^xyz]py 就会匹配 py前面不是x也不是y也不是z的
"""

import re
pattern1 = "\w\dpython[xyz]\w"
pattern2 = "\w\dpython[^xyz]\w"
pattern3 = "\w\dpython[xyz]\W"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
print(result1)
print(result2)
print(result3)