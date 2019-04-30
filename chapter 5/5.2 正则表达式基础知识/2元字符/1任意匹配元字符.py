"""
任意匹配元字符
"""
import re
# .号代表除换行符以外的任意字符
pattern = ".python..."
string = "abcdfphp345pythony_py"
result = re.search(pattern, string)
print(re.search(pattern, string))
