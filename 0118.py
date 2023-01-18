from urllib.request import urlopen

url = "https://tw.news.yahoo.com/"
resp = urlopen(url)

print(resp.read().decode("utf-8"))
