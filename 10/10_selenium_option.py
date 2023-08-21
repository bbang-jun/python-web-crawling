from selenium import webdriver
from selenium.webdriver.chrome.options import Options

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36"

options = Options()

options.add_experimental_option("detach", True) # 브라우저 종료하지 않고 유지
options.add_argument("--start-maximized") # 브라우저 전체 화면
# options.add_argument("--headless") # 브라우저를 켜지 않고도 작업되도록 설정
# options.add_argument("--mute-audio") # 소리 끄기
options.add_argument("incognito") # 크롬 브라우저 시크릿 모드

options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 크롬 상단 자동화 메세지 제거
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 콘솔에서의 불필요한 메세지 제거

driver = webdriver.Chrome(options = options)

url = "https://naver.com"

driver.get(url)

print(driver.page_source[:1000])