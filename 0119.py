import requests

url = "https://myfcu.fcu.edu.tw/main/webClientMyFcuMain.aspx#!/prog/SP3200004"

headers = {
    "User-Agemt": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)  # 反爬
print(resp)  # return status code

print(resp.text)  # 取得原代碼
