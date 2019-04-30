"""
匹配电话号码：
目的：将一串字符串厘米出现电话号码的信息提取出来，过滤掉其他无关信息
"""
import re
# 电话号码区号有3位数和4位数，总长度为11位，区号与号码通过-连接
pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = "021-6728263653682382265236"
result = re.search(pattern, string)
print(result)