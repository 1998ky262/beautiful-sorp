import requests
from bs4 import BeautifulSoup
url = "https://example.com"
r = requests.get(url)
sorp = BeautifulSoup(r.content,"html.parser")
sorp = sorp.select("title")
print(sorp[0].text)
