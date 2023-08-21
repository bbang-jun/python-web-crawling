from selenium import webdriver
import time

url = "https://naver.com"

driver = webdriver.Chrome()

driver.get(url)

title = driver.title

print(title)