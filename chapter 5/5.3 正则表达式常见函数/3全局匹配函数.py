"""
以上的匹配中，即使源字符串有多个结果符合模式，也指挥匹配一个结果，那么，
我们如何将符合模式的内容全部都匹配出来呢？

思路如下：
1. 使用re.compile()对正则表达式进行编译
2. 编译后，使用findall()根据正则表达式从源字符串中将匹配的结果全部找出
"""
import re
string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.")  # 预编译
result = pattern.findall(string)  # 找出符合模式的所有结果
print(result)



# 将其整合以下
import re
string = "hellomypythonhispythonourpythonend"
pattern = ".python."
result = re.compile(pattern).findall(string)
print(result)
