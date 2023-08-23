from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

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

# nav_items = driver.find_elements(By.CLASS_NAME, "nav_item")
# for nav_item in nav_items:
#     if(nav_item.text == "멜론차트"):
#         nav_item.click()
#         break

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(1)

driver.find_elements(By.ID, "moreBtn")[1].click()
time.sleep(1)

# list_item 1위부터 100위까지 전체 수집하는 첫 번째 방법
chartList = driver.find_element(By.ID, "_chartList")
list_items = chartList.find_elements(By.CLASS_NAME, "list_item")

# list_item 1위부터 100위까지 전체 수집하는 두 번째 방법
# list_items = driver.find_elements(By.CLASS_NAME, "list_item")
#
# # selenium에서는 없는 경우에 오류를 발생시킴
# for list_item in list_items[:]:
#     try:
#         ranking_num = list_item.find_element(By.CLASS_NAME, "ranking_num")
#     except NoSuchElementException:
#         list_items.remove(list_item)

action = ActionChains(driver)



for rank, item in enumerate(list_items, 1):
    action.move_to_element(item).perform()
    title = item.find_element(By.CSS_SELECTOR, ".title.ellipsis")
    name = item.find_element(By.CSS_SELECTOR, ".name.ellipsis")

    thumb = item.find_element(By.CSS_SELECTOR, ".inner > span")
    thumb.click()
    time.sleep(1)
    album_url = driver.current_url
    driver.back()
    time.sleep(1)

    print(f"<<<{rank}>>>")
    print(title.text)
    print(name.text)
    print(f"album url : {album_url}")
    print()

# print(len(list_items))