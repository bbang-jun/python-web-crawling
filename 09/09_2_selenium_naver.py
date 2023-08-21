from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword

print(url)

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3) # 페이지에서 소스를 완전하게 받아올 수 있는 시간을 줌
html = driver.page_source

soup = BeautifulSoup(html, "html.parser") # html을 html.parser로 분석(클래스를 통한 객체 생성)

total_area = soup.select(".total_area")
timeline_area = soup.select(".timeline_area")

if total_area:
    areas = total_area
elif timeline_area:
    areas = timeline_area
else:
    print("class 확인 요망")



for rank, area in enumerate(areas, 1):
    title = area.select_one(".api_txt_lines.total_tit")
    name = area.select_one(".sub_txt.sub_name")
    print(f"<<<{rank}>>>")
    print(name.text)
    print(title.text)
    print(title["href"])
    print()
