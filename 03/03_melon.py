import requests
from bs4 import BeautifulSoup # beautiful soup 라이브러리 import

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
} # dictionary

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers = headers) # GET 방식으로 naver에 요청
# html = req.text # 요청을 하여 html을 받아옴
html = req.content.decode('utf-8','replace') # 한글이 깨지는 현상 발생으로 utf-8로 변경

soup = BeautifulSoup(html, "html.parser") # html을 html.parser로 분석(클래스를 통한 객체 생성)

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

top100 = lst50 + lst100

for rank, i in enumerate(top100, start=1):
    title = i.select_one(".ellipsis.rank01").text
    print(f"{rank} : {title}")
    print()