from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_argument("--start-maximized") # 브라우저 전체 화면
options.add_experimental_option("detach", True) # 브라우저 종료하지 않고 유지

driver = webdriver.Chrome(options = options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)