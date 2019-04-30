"""
匹配电子邮件地址：
目的：将一串字符串里面出现的电子邮件信息提取出来，过滤掉其他无关信息
提示：1. 先确定电子邮件地址中的@符号，然后确定@符号前面可以出现哪些字符，
                @符号后面可以出现哪些字符
     2. 设置好正则表达式之后，直接使用search找到电子邮件
"""
import re
# 匹配电子邮件的表达式
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string = "<a href='http://www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqianyue.com.cn'>电子邮件地址</a>"
result = re.search(pattern, string)
print(result)