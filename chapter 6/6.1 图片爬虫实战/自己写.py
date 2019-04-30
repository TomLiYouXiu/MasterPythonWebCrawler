# https://search.jd.com/Search?keyword=iphone&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=iph&page=5&s=110&click=0
import re
import urllib.request
import time

pattern = '<img width="220" height="220" class="" data-img="1" source-data-lazy-img="" data-lazy-img="done" src="//(.+?\.jpg)">'
pattern = re.compile(pattern)


def get_img_from_jd(page=3):
    for i in range(page):
        url = "https://search.jd.com/Search?keyword=iphone&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=iph&page="\
              + str(page) + "&s=110&click=0"
        data = urllib.request.urlopen(url).read()
        img_url_list = pattern.findall(data)
        for j in range(len(img_url_list)):
            urllib.request.urlretrieve(img_url_list[j], str(int(time.time()*10000)))
data = '<img width="220" height="220" class="" data-img="1" source-data-lazy-img="" data-lazy-img="done" src="//img11.360buyimg.com/n7/jfs/t1/2267/5/3518/83121/5b997bf1E6409d7b2/378263542aab44a0.jpg">'
# <img width="220" height="220" class="" data-img="1" source-data-lazy-img="" data-lazy-img="done" src="//img13.360buyimg.com/n7/jfs/t10675/253/1344769770/66891/92d54ca4/59df2e7fN86c99a27.jpg">
# <img width = "220" height = "220" class ="" data-img="1" source-data-lazy-img="" data-lazy-img="done" src="//img13.360buyimg.com/n7/jfs/t10675/253/1344769770/66891/92d54ca4/59df2e7fN86c99a27.jpg">
print(pattern.findall(data))

data = urllib.request.urlopen("https://search.jd.com/Search?keyword=iphone&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=iph&page=5&s=110&click=0").read()
print(type(data))
print(urllib.request.unquote(str(data)))
# print(pattern.findall(str()))
# print(urllib.request.urlopen("https://search.jd.com/Search?keyword=iphone&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=iph&page=2&s=110&click=0").read())