from selenium import webdriver
import time

url = "https://section.cafe.naver.com/ca-fe"

driver = webdriver.Chrome()

driver.get(url)

# title = driver.title
#
# print(title)

html = driver.page_source
print(html)