from selenium import webdriver
from selenium.webdriver.chrome.options import Options

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36"

options = Options()

options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
# options.add_argument("--headless")
options.add_argument("--mute-audio")
options.add_argument("incognito")

options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options = options)

url = "https://naver.com"

driver.get(url)

print(driver.page_source[:1000])