"""
限定符的使用
"""
import re
pattern1 = "py.*n"
pattern2 = "cd{2}"  # 匹配cdd
pattern3 = "cd{3}"  # 匹配cddd
pattern4 = "cd{2,}"  # 匹配cdd或cddd或cdddd后面只能跟d
string = "abcdddfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)
