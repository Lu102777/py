import requests

url = "https://translate.google.com.tw/sug"  # 失效
s = input("輸入英文單字: ")

dat = {
    "kw": s
}

resp = requests.post(url, data=dat)  # 透過data猜樹進行傳遞

print(resp.json())
