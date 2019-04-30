"""
通用字符作为原子
通用字符：一个原子可以匹配一类字符
"""
import re
pattern = '\w\dpython\w'
string = 'abcdfphp345python_py'
result = re.search(pattern, string)
print(result)
