from urllib.request import urlopen
import re

html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)

res = re.findall(r"<title>(.+?)</title>",html)
print("\nPage title is：",res[0])