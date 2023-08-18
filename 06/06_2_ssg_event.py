import requests
from bs4 import BeautifulSoup  # beautiful soup 라이브러리 import

# item_issue

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}  # dictionary

url = "https://www.ssg.com/event/eventMain.ssg"

req = requests.get(url, headers=headers)  # GET 방식으로 naver에 요청
html = req.text  # 요청을 하여 html을 받아옴

soup = BeautifulSoup(html, "html.parser")  # html을 html.parser로 분석(클래스를 통한 객체 생성)

evt_osmu_lst = soup.select_one(".evt_osmu_lst")

eo_links = evt_osmu_lst.select(".eo_link")

for eo_link in eo_links:
    link = eo_link["href"]
    eo_in = eo_link.select_one(".eo_in") # 기간, 제목, 이벤트 회사를 가지고 있는 class

    text_list = eo_in.find_all(string = True)

    print(link)

    for text in text_list:
        if text != "\n":
            print(text)
    print()


    # print(f"{title} : {mall}")
    # print(f"{period} : {link}")
    # print()