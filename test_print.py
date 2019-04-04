from urllib.request import urlopen

html = urlopen(
    "http://www.louz.club/%E8%B1%86%E7%93%A3Top100_TODO.html"
).read().decode('utf-8')
print(html)