from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# find_element()에서 사용하는 By
from selenium.webdriver.common.by import By
# enter와 같은 key를 사용하기 위한 라이브러리
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_argument("--start-maximized") # 브라우저 전체 화면
options.add_experimental_option("detach", True) # 브라우저 종료하지 않고 유지

driver = webdriver.Chrome(options = options)

url = "https://naver.com"

driver.get(url)
time.sleep(0.5)

# By.name도 똑같이 동작함
driver.find_element(By.ID, "query").send_keys("뉴진스")
time.sleep(0.5)

# CSS_SELECTOR는 ID와 CLASS 모두 다 할 수 있음(CLASS는 . ID는 #)
driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
time.sleep(0.5)

# 하위에 있는(//) 모든 것에서(*) text가 VIEW인 것을 찾기(text()="VIEW"))
driver.find_element(By.XPATH, '//*[text()="VIEW"]').click()
time.sleep(0.5)

# clear()를 통해 검색창에 남아 있는 검색어 제거
driver.find_element(By.NAME, "query").clear()
time.sleep(0.5)

driver.find_element(By.NAME, "query").send_keys("하입보이")
time.sleep(0.5)

# 처음에 검색 버튼을 클릭했던 방법 대신 enter 키를 입력하는 방법으로 검색
driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)
time.sleep(0.5)

# html의 body 태그에 페이지를 아래로 내리도록 함
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(0.5)

# 스크린샷 찍기
driver.save_screenshot("screenshot/naver.png")