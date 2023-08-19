import requests
from bs4 import BeautifulSoup

base_url = "https://www.coupang.com/np/search?component=&q="

keyword = input("검색할 상품을 입력하세요 : ")

search_url = base_url + keyword

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

cookie = {"a" : "b"}
req = requests.get(search_url, timeout=5, headers=headers, cookies=cookie)

print(req.status_code)

# html = req.text
#
# soup = BeautifulSoup(html, "html.parser")
