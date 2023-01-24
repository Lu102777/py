# 爬豆瓣top25
import re
import requests

url = "https://movie.douban.com/top250"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=header)
page_content = resp.text  # 頁面原代碼

# 解析數據
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)

result = obj.finditer(page_content)
for it in result:
    print(it.group("name"))
