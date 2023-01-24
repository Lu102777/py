import requests

url = "https://movie.douban.com/j/chart/top_list"
# 重新封裝參數
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}
