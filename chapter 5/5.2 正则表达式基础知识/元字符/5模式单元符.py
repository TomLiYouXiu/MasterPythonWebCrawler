"""
模式单元符：()

可以使用()将一些原子组合成一个大原子使用，小括号括起来的部分将被当作一个整体使用
"""
import re
pattern = "(cd){1,}"  # 将会匹配至少出现1次的cd
pattern2 = "cd{1,}"  # 将会匹配cd 或 cd(d至少出现一次)
string = "abcdcdcdcdfphp345pythony_py"
result = re.search(pattern, string)
result2 = re.search(pattern2, string)
print(result)
print(result2)
