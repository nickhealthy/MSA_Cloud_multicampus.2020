import requests

url = 'http://naver.com'


res = requests.get(url)
res.raise_for_status()

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

