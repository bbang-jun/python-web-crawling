import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

