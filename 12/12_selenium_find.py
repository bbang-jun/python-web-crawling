from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

# 화면 최대 크기
options.add_argument("--start-maximized")
# 화면이 꺼지지 않도록 유지
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)

url = "https://naver.com"

driver.get(url)
time.sleep(1)

driver.find_element(By.XPATH, '//*[@title="검색어를 입력해 주세요."]').send_keys("손흥민", Keys.ENTER)
time.sleep(1)

# driver.find_element(By.XPATH, '//*[text()="VIEW"]').click()
driver.find_element(By.LINK_TEXT, "VIEW").click()
time.sleep(1)

