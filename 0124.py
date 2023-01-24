import re

# findall:匹配字串中所有符合正則的內容
list = re.findall("\d+", "我的電話是123456789,他的電話是987654321")
print(list)

# finditer:匹配字串中所有的內容(return 選代器),拿內容需要用.group()
it = re.finditer("\d+", "我的電話是123456789,他的電話是987654321")
print(it)
for i in it:
    print(i.group())

# search 找到結果即返回,結果是match對象,拿數據需要.group()
s = re.search("\d+", "我的電話是123456789,他的電話是987654321")
print(s.group())

# match是從頭開始匹配
m = re.match("\d+", "我的電話是123456789,他的電話是987654321")
print(m.group())

# 預先加載正規表達式
obj = re.compile("\d+")
ret = obj.finditer("我的電話是123456789,他的電話是987654321")
for it in ret:
    print(it.group())
