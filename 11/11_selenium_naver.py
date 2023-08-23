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
time.sleep(1)

# By.name도 똑같이 동작함
driver.find_element(By.ID, "query").send_keys("뉴진스")
time.sleep(1)

# CSS_SELECTOR는 ID와 CLASS 모두 다 할 수 있음(class는 . id는 #)
driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
time.sleep(1)