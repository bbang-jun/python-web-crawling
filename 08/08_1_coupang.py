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

html = req.text

soup = BeautifulSoup(html, "html.parser")

# items = soup.select(".search-product") # 기존 방식(포함된 모든 class들을 가져옴)
items = soup.select("[class=search-product]") # 새로운 방식(정확히 해당 class만을 가져옴)

rank = 1
for item in items:
    badge_rocket = item.select_one(".badge.rocket")
    if not badge_rocket:
        continue
    name = item.select_one(".name")
    price = item.select_one(".price-value")
    thumbnail = item.select_one(".search-product-wrap-img")
    # url = item.a["href"]
    url = item.select_one(".search-product-link")["href"]
    print(f"{rank}위")
    print(name.text)
    print(f"{price.text} 원")
    # if thumbnail["src"]:
    #     print(thumbnail["src"])
    # else if thumb
    print(thumbnail.get("data-img-src"))
    print(url)
    print()

    rank += 1

# "search-product " 27개
# "search-product search-product__ad-badge" 9개