import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://www.baidusss.net")
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)