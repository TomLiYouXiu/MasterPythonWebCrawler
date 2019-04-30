"""
贪婪模式与懒惰模式的区别在于：贪婪模式总是尽可能多匹配，而懒惰模式的核心点就是尽可能少匹配
"""
import re
pattern = "p.*y"  # 贪婪模式
pattern2 = "p.*?y"  # 懒惰模式
string = "abcdfphp345pythony_py"
result1 = re.search(pattern, string)
result2 = re.search(pattern2, string)
print(result1)
print(result2)

"""
结论：懒惰模式采用的是就近匹配原则，可以让匹配更为精确，
     上面程序通过贪婪模式匹配，已经找到一个结尾的y字符了，
     但仍然不会停止搜索，直到找不到末尾的y为止
像某些情形"p.*y"默认是使用贪婪模式的，如果要转换为懒惰模式，需要在对应的".*"后面加上? 
这时将会转换为懒惰模式
"""