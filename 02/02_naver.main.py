import requests
from bs4 import BeautifulSoup # beautiful soup 라이브러리 import

url = "https://naver.com"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
} # dictionary

req = requests.get(url, headers = headers) # GET 방식으로 naver에 요청
html = req.text # 요청을 하여 html을 받아옴
soup = BeautifulSoup(html, "html.parser") # html을 html.parser로 분석(클래스를 통한 객체 생성)

print(soup.h1)
print()

h1 = soup.find('h1')
print(h1)
print()

h1 = soup.select_one('h1')
print(h1)
print()

h1 = soup.find(class_="search_logo")
print(h1)
print()