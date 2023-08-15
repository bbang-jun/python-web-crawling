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
    title = i.select_one(".ellipsis.rank01 a").text # 정확하게 a 태그 찾기. 기존에는 div 태그가 있어서 자동 개행되었음.
    singer = i.select_one(".ellipsis.rank02 > a").text # 바로 아래에 a 태그가 있음을 의미
    print(f"{rank} : {title}") # .text는 내부에 여러 태그가 있더라도 찾아주지만 .string은 정확하게 바로 아래 태그에서만 찾음
    print(singer)
    print()