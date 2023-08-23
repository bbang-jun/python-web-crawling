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

link_services = driver.find_elements(By.CLASS_NAME, "link_service")

for order, link_service in enumerate(link_services, 1):
    # print(order)
    # print(link_service.get_attribute("outerHTML"))
    # print(link_service.text)
    # print()
    if link_service.text == "웹툰":
        link_service.click()
        break

driver.quit()