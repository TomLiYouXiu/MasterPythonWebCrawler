"""
边界限制元字符：^ 匹配字符串的开始 与 $匹配字符串的结束
"""
import re
pattern1 = "^abd"
pattern2 = "^abc"
pattern3 = "py$"
pattern4 = "ay$"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)