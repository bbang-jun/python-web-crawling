import requests
from bs4 import BeautifulSoup # beautiful soup 라이브러리 import

url = "https://naver.com"

req = requests.get(url) # GET 방식으로 naver에 요청

html = req.text # 요청을 하여 html을 받아옴

print(html) # html 출력