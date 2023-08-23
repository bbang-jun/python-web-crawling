from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# find_element()에서 사용하는 By
from selenium.webdriver.common.by import By
import time

options = Options()

options.add_argument("--start-maximized") # 브라우저 전체 화면
options.add_experimental_option("detach", True) # 브라우저 종료하지 않고 유지

driver = webdriver.Chrome(options = options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)

driver.find_element()

# 네이버 검색창 html
# <input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요."
# maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">