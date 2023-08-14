import requests
from bs4 import BeautifulSoup # beautiful soup 라이브러리 import

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword

print(url)

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
} # dictionary

req = requests.get(url, headers = headers) # GET 방식으로 naver에 요청


html = req.text # 요청을 하여 html을 받아옴

soup = BeautifulSoup(html, "html.parser") # html을 html.parser로 분석(클래스를 통한 객체 생성)

# api_txt_lines total_tit _cross_trigger

results = soup.select(".api_txt_lines.total_tit._cross_trigger")

for result in results:
    print(result['href'])
    print(result.text) # result 자체는 <a> 태그임