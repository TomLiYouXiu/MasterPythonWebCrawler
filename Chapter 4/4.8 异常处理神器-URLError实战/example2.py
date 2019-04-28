import urllib.request
import urllib.error
try:
    urllib.request.urlopen("https://itbook.download/")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
