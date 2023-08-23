from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

# 네트워크 -> f5 -> document -> User-Agent
user_agent = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"

# user-agent
options.add_argument(f"user-agent={user_agent}")
# 화면 최대 크기
options.add_argument("--start-maximized")
# 화면이 꺼지지 않도록 유지
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)

url = "https://m2.melon.com/index.htm"

driver.get(url)
time.sleep(1)

if driver.current_url != url:
    driver.get(url)