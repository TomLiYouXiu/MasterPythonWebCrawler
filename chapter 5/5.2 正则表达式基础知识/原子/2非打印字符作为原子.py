"""
非打印字符作为原子
"""
import re
pattern = '\n'
string = """http://yum.iquanyue.com
            http://baidu.com
         """
string1 = """http://yum.iquanyue.comhttp://baidu.com"""
print(string)
result = re.search(pattern, string)
print(result)

result1 = re.search(pattern, string1)
print(result1)  # None