import urllib.request
import re
pattern = '<div id="plist".+?<div class="page clearfix"'
pattern = re.compile(pattern)

url = "https://list.jd.com/list.html?cat=9987,653,655&page=1"
html = urllib.request.urlopen(url).read()
html_str = str(html)
result1 = pattern.findall(html_str)
print("result1:---------------------------")
print(result1)
print("-------------------------")
# img_pattern = '<img width="220" height="220" data-img="1" data-lazy-img="done" title=".{0,}" src="//(.+?\.jpg)">'
img_pattern = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
img_pattern = re.compile(img_pattern, re.S)
# data = '<img width="220" height="220" data-img="1" data-lazy-img="done" title="" src="//img14.360buyimg.com/n7/jfs/t1/12063/32/7819/422947/5c6e4f17Ec8fcb0e9/d30766d5037954f6.jpg">'
# data = '<img width="220" height="220" data-img="1" data-lazy-img="done" title="全面屏，小身材，大视野！小巧全面屏,通话大音量,柔光自拍黑夜自拍更得心应手。荣耀爆品特惠，选品质，购荣耀~" src="//img12.360buyimg.com/n7/jfs/t18982/17/2574683163/226853/fc736ec6/5afc0c37Nbdaea6fb.jpg">'
# '<img width="220" height="220" data-img="1" data-lazy-img="done" title="全面屏，4000mAh大电量，前置柔光自拍，骁龙八核处理器！小米爆品特惠，选品质，购小米！" src="//img11.360buyimg.com/n7/jfs/t14173/365/1779524313/324587/3b5a727/5a28b6eaN3c80b8c1.jpg">'
result2 = img_pattern.findall(result1[0])
print(result2[0])
print(result2[1])
print(result2[2])
print(len(result2))
# print(img_pattern.findall(result1))

