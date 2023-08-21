from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = service) # web driver를 만들 때 service로 들어감

driver.get("https://google.com")
time.sleep(2)